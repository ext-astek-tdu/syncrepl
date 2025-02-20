#!python
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 et

# syncrepl_client demo program.
#
# Refer to the AUTHORS file for copyright statements.
#
# This file is made available under the terms of the BSD 3-Clause License,
# the text of which may be found in the file `LICENSE.md` that was included
# with this distribution, and also at
# https://github.com/akkornel/syncrepl/blob/master/LICENSE.md
#
# The Python docstrings contained in this file are also made available under the terms
# of the Creative Commons Attribution-ShareAlike 4.0 International Public License,
# the text of which may be found in the file `LICENSE_others.md` that was included
# with this distribution, and also at
# https://github.com/akkornel/syncrepl/blob/master/LICENSE_others.md
#


# Python 2 support
from __future__ import print_function

from argparse import ArgumentParser
import signal
import sys

import ldap
from syncrepl_client import Syncrepl
from syncrepl_client.callbacks import LoggingCallback
from syncrepl_client._version import __version__
from sys import argv, exit

from syncrepl_client.ldap_info import LDAPInfo
from syncrepl_client.syncrepl_mode import SyncreplMode


DN = "dc=openldapprov,dc=com"
BIND_DN = "cn=admin,dc=openldapprov,dc=com"
CREDENTIAL = "admin"
SEARCH_FILTER = "(objectClass=*)"
HOST_PORT = "localhost:389"
SCOPE = ldap.SCOPE_SUBTREE
MODE = SyncreplMode.REFRESH_ONLY

LDAP_INFO = LDAPInfo(
    DN, BIND_DN, CREDENTIAL, SEARCH_FILTER, HOST_PORT, SCOPE, MODE
)

DATA_PATH = "./prefix/data.db/"

STARTTLS = False


# If persist mode is use, check for thread support.

if MODE is SyncreplMode.REFRESH_AND_PERSIST:
    try:
        import threading
    except ImportError:
        print("Your Python does not support threads!")
        print("Please run without --persist, or change your Python.")
        sys.exit(1)

# Print out prefix and search mode.

print("Data files will be stored here:", DATA_PATH)

print(
    (
        "Refresh-and-persist"
        if MODE is SyncreplMode.REFRESH_AND_PERSIST
        else "Refresh-only"
    ),
    "mode will be used",
)

# Set up the client.
# The arguments are simple, because the LDAP URL contains most of the info.

print("CLIENT SETUP START")
client = Syncrepl(DATA_PATH, LoggingCallback, LDAP_INFO, STARTTLS)

print("CLIENT SETUP COMPLETE!")

# What we do now depends on our mode.

if MODE is SyncreplMode.REFRESH_AND_PERSIST:
    # In persist mode, we should use threading.
    # Out main thread will watch for signals, and safely stop the Syncrepl.

    print("THREAD SETUP START")
    thread = threading.Thread(target=client.run)
    print("THREAD SETUP COMPLETE")

    # We need to make sure that signals don't cause us to exit uncleanly.
    print("SIGNAL SETUP START")

    # Define a simple signal-handler, which calls the (thread-safe)
    # `please_stop` method, to ask the Syncrepl client to end the search
    # safely.
    def stop_handler(signal, frame):
        print("STOP REQUEST START")
        client.please_stop()
        print("STOP REQUEST COMPLETE")

    # Set our handler to catch common signals that we might receive.
    # * SIGHUP is sent if the terminal closes while we are running.
    # * SIGINT is the signal we get by pressing Control-C.
    # * SIGTERM is the default signal that `kill` sends us.
    signal.signal(signal.SIGHUP, stop_handler)
    signal.signal(signal.SIGINT, stop_handler)
    signal.signal(signal.SIGTERM, stop_handler)
    print("SIGNAL SETUP COMPLETE")

    # Launch the thread, and then wait for it to exit.
    # Signal interruptions would happen in here.

    print("THREAD START")
    thread.start()
    thread.join()
    print("THREAD END")

else:
    # In refresh-only mode, no threading is needed, because we just run
    # until the end.

    while True:
        # We call `poll()`, and take note of the result.
        print("CLIENT LOOP START")
        loop_result = client.poll()
        print("CLIENT LOOP END")
        print("\tLoop Result:", loop_result)

        # If the loop is False, then there is nothing else to do.
        # Otherwise, some work has been done, but the server has more.
        if loop_result is False:
            print("CLIENT LOOP COMPLETE!")
            break

# Clean up and exit

print("CLIENT EXIT START")
if MODE is SyncreplMode.REFRESH_AND_PERSIST:
    client.db_reconnect()
client.unbind()
print("CLIENT EXIT COMPLETE!")
exit(0)
