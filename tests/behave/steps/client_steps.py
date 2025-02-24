from behave import *
from behave import given, when, then # pylint: disable=no-name-in-module

from behave.runner import Context

@given("Client is not bind to LDAP server")
def client_is_not_bind(context: Context) -> None:
    raise NotImplementedError("STEP: Given Client is not bind to LDAP server")


@given(
    'Client connect to dn:"{dn}" as bind_dn:"{bind_dn}" password:"{password}" filter:"{search_filter}" scope: "{scope}" mode:"{mode}"'
)
@when(
    'Client connect to dn:"{dn}" as bind_dn:"{bind_dn}" password:"{password}" filter:"{search_filter}" scope: "{scope}" mode:"{mode}"'
)
def client_connect_to(
    context: Context,
    dn: str,
    bind_dn: str,
    password: str,
    search_filter: str,
    scope: str,
    mode: str,
) -> None:
    raise NotImplementedError(
        f'STEP: When Client connect to dn:"{dn}" as bind_dn:"{bind_dn}" password:"{password}" filter:"{search_filter}" scope: "{scope}" mode:"{mode}"'
    )


@then("Client has been binded to LDAP server")
def client_has_been_binded(context: Context) -> None:
    raise NotImplementedError(
        "STEP: Then Client has been binded to LDAP server"
    )


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
