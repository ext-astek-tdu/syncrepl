from behave import *
from behave import given, when, then  # pylint: disable=no-name-in-module


@given("Client is not bind to LDAP server")
def client_is_not_bind(context):
    raise NotImplementedError("client_is_not_bind()")


@then("Client has been binded to LDAP server")
def is_client_has_been_binded_to_LDAP_server(context):
    raise NotImplementedError("is_client_bind_to_LDAP_server()")


@given(
    'Client connect to dn:"{dn}" as bind_dn:"{bind_dn}" password:"{password}" filter:"{search_filter}" scope: "{scope}" mode:"{mode}"'
)
@when(
    'Client connect to dn:"{dn}" as bind_dn:"{bind_dn}" password:"{password}" filter:"{search_filter}" scope: "{scope}" mode:"{mode}"'
)
def client_connect_with_ldap_info(
    context,
    dn: str,
    bind_dn: str,
    password: str,
    search_filter: str,
    scope: str,
    mode: str,
):
    raise NotImplementedError(
        f"client_connect_with_ldap_info() {dn} {bind_dn} {password} {search_filter} {scope} {mode}"
    )


@when('Client connect to "{ldap_url}" on "{mode}" mode')
def client_connect_with_ldap_url(context, ldap_url: str, mode: str):
    raise NotImplementedError(
        f"client_connect_with_ldap_url(), {ldap_url} {mode}"
    )
