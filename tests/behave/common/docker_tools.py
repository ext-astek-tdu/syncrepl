"""
Module that give tools to manage the openLDAP container
"""

from datetime import datetime
from time import sleep
import docker
from docker.models.containers import Container
from tests.behave.common.constants import LDAPConst, DockerConst


def start_openldap() -> Container:
    """
    Start the openLDAP container

    :return Container:
    """
    client = docker.from_env()
    container = client.containers.run(
        image=DockerConst.IMAGE,
        name=DockerConst.CONTAINER_NAME,
        user=DockerConst.USER,
        environment={
            "LDAP_ROOT": LDAPConst.LDAP_DN,
            "LDAP_ADMIN_USERNAME": LDAPConst.LDAP_ADMIN_USERNAME,
            "LDAP_ADMIN_PASSWORD": LDAPConst.LDAP_ADMIN_PASSWORD,
            "LDAP_CUSTOM_LDIF_DIR": LDAPConst.LDAP_CUSTOM_LDIF_DIR,
            "LDAP_ENABLE_SYNCPROV": LDAPConst.LDAP_ENABLE_SYNCPROV,
        },
        ports={"1389/tcp": 389, "1636/tcp": 636},
        volumes={
            DockerConst.LDIF_PATH: {"bind": "/ldifs"},
            DockerConst.ACTIONS_LDIF_PATH: {"bind": "/actions_ldifs"},
        },
        detach=True,
    )
    print(f"OpenLDAP started with ID : {container.id}")

    wait_for_ldap_server_to_be_ready()
    return container


def stop_openldap():
    """Stop the openLDAP container"""
    client = docker.from_env()
    try:
        container = client.containers.get(DockerConst.CONTAINER_NAME)
        print("OpenLDAP is stopping...")
        container.stop()
        print("OpenLDAP stopped.")
        print("OpenLDAP is removing...")
        container.remove()
        while DockerConst.CONTAINER_NAME in client.containers.list(True):
            sleep(0.2)

        print("OpenLDAP is being removed.")
    except docker.errors.NotFound:
        print("Nothing to stop. Container does not exist.")


def wait_for_ldap_server_to_be_ready() -> None:
    """Wait until the ldap server is up and running"""
    print("waiting for openLDAP server to start")
    client = docker.from_env()
    container = client.containers.get(DockerConst.CONTAINER_NAME)
    start_time = datetime.now()
    exit_code = 255
    while exit_code != 0:
        sleep(DockerConst.COOLDOWN)
        passed_time = (datetime.now() - start_time).seconds
        bind_dn = f"{LDAPConst.LDAP_ADMIN_BIND}"
        conn_args = f'-D "{bind_dn}" -w {LDAPConst.LDAP_ADMIN_PASSWORD}'
        answer = container.exec_run(
            f'ldapsearch -x -H ldap://localhost:1389 {conn_args} -b "{LDAPConst.LDAP_DN}" "(objectClass=*)"'
        )
        exit_code = answer.exit_code
        if passed_time >= DockerConst.MAX_WAITING_SECONDS and exit_code:
            raise TimeoutError(
                f"openLDAP server hasn't been able to start in less than {DockerConst.MAX_WAITING_SECONDS}s"
            )
    print("openLDAP server ready")


def get_ldap_container() -> Container:
    """
    Return the openLDAP container.

    :return Container:
    """
    client = docker.from_env()
    container = client.containers.get(DockerConst.CONTAINER_NAME)
    return container
