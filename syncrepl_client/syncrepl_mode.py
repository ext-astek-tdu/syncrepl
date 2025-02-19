from enum import Enum


class SyncreplMode(Enum):
    """
    This enumeration is used to specify the operating mode for the Syncrepl
    client.  Once a mode is set it can not be changed.  To change the mode, you
    will have to (safely) shut down your existing search, unbind and destroy
    the existing instance, and start a new instance in the new mode.
    """

    REFRESH_ONLY = "refreshOnly"
    """
    In this mode, the syncrepl search will last long enough to bring you in
    sync with the server.  Once you are in sync,
    :meth:`~syncrepl_client.Syncrepl.poll()` will return :obj:`False`.
    """

    REFRESH_AND_PERSIST = "refreshAndPersist"
    """
    In this mode, you start out doing a refresh.  Once the refresh is complete,
    subsequent calls to :meth:`~syncrepl_client.Syncrepl.poll` will be used to
    receive changes as they happen on the LDAP server.  All calls to
    :meth:`~syncrepl_client.Syncrepl.poll()` will return :obj:`True`, unless a
    timeout takes place (that will throw :class:`ldap.TIMEOUT`), you cancel the
    search (that will throw :class:`ldap.CANCELLED`), or something else goes
    wrong.

    .. note::
        When running a Syncrepl search in refresh-and-persist mode, it is
        **strongly** recommended that you run the actual search operation in a
        thread, so that you can catch signals which would otherwise cause an
        unclean termination of the Syncrepl search.

        For more information, see the :meth:`~syncrepl_client.Syncrepl.run`
        method, which is what you should use as the thread's target.
    """
