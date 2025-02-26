"""File containing constants"""

import os
from enum import Enum, auto


class CallbackIds(Enum):
    """Enum of callbacks ids"""

    BIND = auto()
    REFRESH = auto()
    RECORD_ADD = auto()
    RECORD_DELETE = auto()
    RECORD_RENAME = auto()
    RECORD_CHANGE = auto()
    COOKIE_CHANGE = auto()


class DockerConst:
    """Constants related to the openLDAP docker"""

    CONTAINER_NAME = "behave_open_ldap_prov"
    LDIF_PATH = os.path.abspath("./tests/ldifs")
    ACTIONS_LDIF_PATH = os.path.abspath("./tests/actions_ldifs")
    MAX_WAITING_SECONDS = 5
    COOLDOWN = 0.2

    IMAGE = "docker.io/bitnami/openldap:2.6"
    USER = "root"


class LDAPConst:
    """Global constants"""

    LDAP_ADMIN_USERNAME = "admin"
    LDAP_ADMIN_PASSWORD = "admin"
    LDAP_DN = "dc=openldapprov,dc=com"
    LDAP_ADMIN_BIND = f"cn={LDAP_ADMIN_USERNAME},{LDAP_DN}"
    LDAP_CUSTOM_LDIF_DIR = "/ldifs"
    LDAP_ENABLE_SYNCPROV = "yes"
    HOST_PORT = "localhost:389"

    DATA_PATH = "./prefix/data.db/"
    STARTTLS = False
