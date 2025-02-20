
from dataclasses import dataclass
from typing import Union

import ldap
import ldapurl

from syncrepl_client.syncrepl_mode import SyncreplMode


@dataclass
class LDAPInfo:
    '''This class is use to contain LDAP information, and build a ldapurl.LDAPUrl object
    '''
    dn: str
    bind_dn: str
    password: str
    search_filter: str
    host_port: str
    scope: Union["ldap.SCOPE_BASE", "ldap.SCOPE_ONELEVEL", "ldap.SCOPE_SUBTREE"]
    mode: SyncreplMode

    def get_ldap_url(self) -> ldapurl.LDAPUrl:
        '''This method build a ldapurl.LDAPUrl ready to use
        '''
        if self.scope == ldap.SCOPE_BASE:
            scope_str = "base"
        elif self.scope == ldap.SCOPE_ONELEVEL:
            scope_str = "one"
        elif self.scope == ldap.SCOPE_SUBTREE:
            scope_str = "sub"
        else:
            raise ValueError("scope is not ldap.SCOPE_BASE or ldap.SCOPE_BASE or ldap.SCOPE_BASE")

        filter_and_ext = f"?{self.search_filter}"
        scope_and_other = f"??{scope_str}{filter_and_ext}"
        dn_and_other = f"{self.dn}{scope_and_other}"
        credentials = f"bindname={self.bind_dn},X-BINDPW={self.password}"
        ldap_url = f"ldap://{self.host_port}/{dn_and_other}?{credentials}"

        return ldapurl.LDAPUrl(ldap_url)
