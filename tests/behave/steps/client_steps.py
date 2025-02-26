"""Contain steps related to client testing"""

from behave import *  # pylint: disable=wildcard-import, unused-wildcard-import
from behave import given, when, then  # pylint: disable=no-name-in-module

from behave.runner import Context
import ldap

from syncrepl_client.ldap_info import LDAPInfo
from syncrepl_client.syncrepl_mode import SyncreplMode
from tests.behave.common.constants import CallbackIds, LDAPConst
from tests.behave.common.singleton import Singleton


@given("Client is not bind to LDAP server")
def client_is_not_bind(_context: Context) -> None:
    """check if client hasn't ever been binded"""
    vuc = Singleton.virtual_user_client
    is_event = vuc.is_event_has_happened(CallbackIds.BIND)
    assert not is_event, "Client has already been bind"


@given(
    'Client connect to dn:"{dn}" as bind_dn:"{bind_dn}" password:"{password}" filter:"{search_filter}" scope: "{scope}" mode:"{mode}"'
)
@when(
    'Client connect to dn:"{dn}" as bind_dn:"{bind_dn}" password:"{password}" filter:"{search_filter}" scope: "{scope}" mode:"{mode}"'
)
def client_connect_to(
    _context: Context,
    dn: str,
    bind_dn: str,
    password: str,
    search_filter: str,
    scope: str,
    mode: str,
) -> None:
    """Connect client via LDAPInfo class"""
    scope_level = {
        "SCOPE_BASE": ldap.SCOPE_BASE,  # pylint: disable=no-member
        "SCOPE_ONELEVEL": ldap.SCOPE_ONELEVEL,  # pylint: disable=no-member
        "SCOPE_SUBTREE": ldap.SCOPE_SUBTREE,  # pylint: disable=no-member
    }.get(scope, None)

    if scope_level is None:
        raise ValueError(
            f"Scope has not been set correctly. Scope giver: {scope}"
        )

    sync_mode = {
        "REFRESH_AND_PERSIST": SyncreplMode.REFRESH_AND_PERSIST,
        "REFRESH_ONLY": SyncreplMode.REFRESH_ONLY,
    }.get(mode, None)

    if sync_mode is None:
        raise ValueError("scope has not been set correctly")

    ldap_info = LDAPInfo(
        dn,
        bind_dn,
        password,
        search_filter,
        LDAPConst.HOST_PORT,
        scope_level,
        sync_mode,
    )

    Singleton.virtual_user_client.connect_to_ldap(
        LDAPConst.DATA_PATH, ldap_info, LDAPConst.STARTTLS
    )


@then("Client has been binded to LDAP server")
def client_has_been_binded(_context: Context) -> None:
    """Check if client has been connected"""
    vuc = Singleton.virtual_user_client
    has_event_happenned = vuc.is_event_has_happened(CallbackIds.BIND)
    assert has_event_happenned, "Bind has not been register by the callback"


@when(
    'I do a "{ldap_action}" on the openLDAP serveur, with this ldif file "{ldif_file_name}"'
)
def do_ldap_action_with_file(
    context: Context, ldap_action: str, ldif_file_name: str
) -> None:
    raise NotImplementedError(
        f'STEP: When I do a "{ldap_action}" on the openLDAP serveur, with this ldif file "{ldif_file_name}"'
    )


@then('Client changed his infos according to ldif file "{ldif_file_name}"')
def is_clilent_has_been_updated(context: Context, ldif_file_name: str) -> None:
    raise NotImplementedError(
        f'STEP: Then Client changed his infos according to ldif file  "{ldif_file_name}"'
    )
