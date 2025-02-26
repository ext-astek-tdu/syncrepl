"""
Contains a callback class to register informations related to behave tests
"""

from syncrepl_client.callbacks import BaseCallback
from tests.behave.common.constants import CallbackIds
import tests.behave.common.virtual_user_client as vuc


class DebugCallBack(BaseCallback):
    """
    Callback class to register informations related to behave tests.
    """

    v_client_user: "vuc.VirtualUserClient"

    @classmethod
    def set_virtuel_client_user(cls, client: "vuc.VirtualUserClient") -> None:
        """Set parent VirtualClientUser of the class
        :param VirtualClientUser: Futur parent of the class
        """
        cls.v_client_user = client

    @classmethod
    def bind_complete(cls, ldap, cursor):
        """Called when the bind has been done"""
        cls.v_client_user.push_callback_id(CallbackIds.BIND)

    @classmethod
    def refresh_done(cls, items, cursor):
        """Called when the refresh is completed"""
        cls.v_client_user.push_callback_id(CallbackIds.REFRESH)
        ldap_objects: dict[str, dict[str, list[bytes]]] = {}
        for item in items:
            attrs = items[item]
            ldap_objects[item] = attrs

        cls.v_client_user.set_local_dit(ldap_objects)

    @classmethod
    def record_add(cls, dn, attrs, cursor):
        """Called when a record has been added"""
        cls.v_client_user.push_callback_id(CallbackIds.RECORD_ADD)

    @classmethod
    def record_delete(cls, dn, cursor):
        """Called when a record has been deleted"""
        cls.v_client_user.push_callback_id(CallbackIds.RECORD_DELETE)

    @classmethod
    def record_rename(cls, old_dn, new_dn, cursor):
        """Called when a record has been renamed"""
        cls.v_client_user.push_callback_id(CallbackIds.RECORD_RENAME)

    @classmethod
    def record_change(cls, dn, old_attrs, new_attrs, cursor):
        """Called when a record has been changed"""
        cls.v_client_user.push_callback_id(CallbackIds.RECORD_CHANGE)

    @classmethod
    def cookie_change(cls, cookie):
        """Called when the cookie has been added"""
        cls.v_client_user.push_callback_id(CallbackIds.COOKIE_CHANGE)
