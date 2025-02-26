"""Module for managing connection status and simulating a Syncrepl client user."""

import signal
import threading
from typing import Optional
from syncrepl_client import Syncrepl
from syncrepl_client.ldap_info import LDAPInfo
from syncrepl_client.syncrepl_mode import SyncreplMode
from tests.behave.common.debug_callback import DebugCallBack
from tests.behave.common.constants import CallbackIds


class VirtualUserClient:
    """Class that emulates a user of a syncrepl client."""

    def __init__(self) -> None:
        """Initialize the virtual client user with no active connection."""
        DebugCallBack.set_virtuel_client_user(self)
        self._sync_client: Optional[Syncrepl] = None
        self._thread: Optional[threading.Thread] = None
        #                   ldap dn  attribut   values
        #                     \/        \/        \/
        self._local_dit: dict[str, dict[str, list[bytes]]] = {}
        self._stack_of_modification: list[CallbackIds] = []

    def push_callback_id(self, callback_id: CallbackIds):
        """Push a callback id to keep track of what's going on

        :id CallbackIds: id to push to the stack
        """
        self._stack_of_modification.append(callback_id)

    def is_event_has_happened(self, callback_id: CallbackIds) -> bool:
        """Says if an event has happended or not

        :callback_id CallbackIds: Event we search
        :return bool: True if event happened, False otherwise
        """
        return callback_id in self._stack_of_modification

    def set_local_dit(self, new_dit: dict[str, dict[str, list[bytes]]]):
        """Set a new local dit

        :new_dit dict[str, dict[str, list[bytes]]]: futur local dit know by virtual user
        """
        self._local_dit = new_dit

    def connect_to_ldap(
        self, data_path: str, ldap_info: LDAPInfo, starttls: bool
    ):
        """Instanciate, a Syncrepl client

        :data_path str: Data_path from the syncrepl database
        :ldap_info LDAPinfo: LDAPinfo necessary to the conection the LDAP server
        :starttls bool:
        """
        self._sync_client = Syncrepl(
            data_path, DebugCallBack, ldap_info, starttls
        )
        if ldap_info.mode is SyncreplMode.REFRESH_AND_PERSIST:

            def _stop_thread(_signal, _frame):
                self._sync_client.please_stop()

            self._thread = threading.Thread(target=self._sync_client.run)
            signal.signal(signal.SIGHUP, _stop_thread)
            signal.signal(signal.SIGINT, _stop_thread)
            signal.signal(signal.SIGTERM, _stop_thread)
            self._thread.start()
        elif ldap_info.mode is SyncreplMode.REFRESH_ONLY:
            ...  # Nothing to do in REFRESH_ONLY
        else:
            raise ValueError(f"{ldap_info.mode} is not implemented")

    def stop_client(self):
        """stop gently the syncrepl client"""
        if self._sync_client is None:
            return
        if (
            self._sync_client.ldap_info.mode is SyncreplMode.REFRESH_AND_PERSIST
            and self._thread is not None
        ):
            self._thread.join()
            self._sync_client.db_reconnect()
        self._sync_client.unbind()

    def poll_client(self):
        """Poll the client until the end"""
        if self._sync_client.ldap_info.mode is not SyncreplMode.REFRESH_ONLY:
            return
        loop_result = True
        while loop_result:
            loop_result = self._sync_client.poll()
