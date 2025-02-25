"""Module for managing connection status and simulating a Syncrepl client user."""

from typing import Optional
from syncrepl_client import Syncrepl
from syncrepl_client.ldap_info import LDAPInfo
from tests.behave.common.debug_callback import DebugCallBack


class ConnectionStatus:
    """Class that stores connection status flags."""

    IS_CONNECTED = 0b01
    WAS_SYNCHED_BEFORE = 0b10

    def __init__(self):
        """Initialize the connection status as disconnected."""
        self._status = 0b00

    def connect(self) -> None:
        """Set the connection status to connected."""
        self._status |= self.IS_CONNECTED

    def disconnect(self) -> None:
        """Mark the connection as disconnected and record past sync."""
        self._status &= ~self.IS_CONNECTED
        self._status |= self.WAS_SYNCHED_BEFORE

    def is_connected(self) -> bool:
        """Check if the connection is currently active."""
        return bool(self._status & self.IS_CONNECTED)

    def has_been_connected(self) -> bool:
        """Check if a connection has ever been established before."""
        return bool(self._status & self.WAS_SYNCHED_BEFORE)


class VirtualUserClient:
    """Class that emulates a user of a syncrepl client."""

    def __init__(self) -> None:
        """Initialize the virtual client user with no active connection."""
        DebugCallBack.set_virtuel_client_user(self)

        self._sync_client: Optional[Syncrepl] = None
        self._connection_status = ConnectionStatus()

    def get_status_con(self) -> ConnectionStatus:
        """Return current status connection
        :return ConnectionStatus:
        """
        return self._connection_status

    def connect_to_ldap(self, data_path: str, ldap_info: LDAPInfo, starttls: bool):
        client = Syncrepl(data_path, DebugCallBack, ldap_info, starttls)

