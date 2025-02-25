"""File containing a class to handle singletons"""

from docker.models.containers import Container
from tests.behave.common.virtual_user_client import VirtualUserClient


class Singleton:
    """Class containing singletons"""

    ldap_container: Container
    virtual_user_client: VirtualUserClient
