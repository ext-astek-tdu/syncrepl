"""
Contains a callback class to register informations related to behave tests
"""

from syncrepl_client.callbacks import BaseCallback


class DebugCallBack(BaseCallback):
    """
    Callback class to register informations related to behave tests.
    """

    # TODO: Implement all methods and all tests feature
    @classmethod
    def bind_complete(cls, ldap, cursor):
        """"""

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
