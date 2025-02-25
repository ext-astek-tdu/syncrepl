"""
Contains a callback class to register informations related to behave tests
"""

from syncrepl_client.callbacks import BaseCallback
from tests.behave.common.virtual_user_client import VirtualUserClient


class DebugCallBack(BaseCallback):
    """
    Callback class to register informations related to behave tests.
    """

    v_client_user: VirtualUserClient

    @classmethod
    def set_virtuel_client_user(cls, client: VirtualUserClient) -> None:
        """Set parent VirtualClientUser of the class
        :param VirtualClientUser: Futur parent of the class
        """
        cls.v_client_user = client

    # TODO: Implement all methods and all tests feature
    @classmethod
    def bind_complete(cls, ldap, cursor):
        """"""
        sc = cls.v_client_user.get_status_con()
        sc.connect()

    @classmethod
    def refresh_done(cls, items, cursor):
        """"""

    @classmethod
    def record_add(cls, dn, attrs, cursor):
        """"""

    @classmethod
    def record_delete(cls, dn, cursor):
        """"""

    @classmethod
    def record_rename(cls, old_dn, new_dn, cursor):
        """"""

    @classmethod
    def record_change(cls, dn, old_attrs, new_attrs, cursor):
        """"""

    @classmethod
    def cookie_change(cls, cookie):
        """"""
