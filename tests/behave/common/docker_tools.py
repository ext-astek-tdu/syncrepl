"""
Module that give tools to manage the openLDAP container
"""

from datetime import datetime
from time import sleep
import os
import docker
from docker.models.containers import Container

CONTAINER_NAME = "behave_open_ldap_prov"
LDIF_PATH = os.path.abspath("./tests/ldifs")
ACTIONS_LDIF_PATH = os.path.abspath("./tests/actions_ldifs")
MAX_WAITING_SECONDS = 5
COOLDOWN = 0.2

IMAGE = "docker.io/bitnami/openldap:2.6"
USER = "root"
LDAP_ROOT = "dc=openldapprov,dc=com"
LDAP_ADMIN_USERNAME = "admin"
LDAP_ADMIN_PASSWORD = "admin"
LDAP_CUSTOM_LDIF_DIR = "/ldifs"
LDAP_ENABLE_SYNCPROV = "yes"


def start_openldap() -> Container:
    """
    Start the openLDAP container

    :return Container:
    """
    client = docker.from_env()
    container = client.containers.run(
        image=IMAGE,
        name=CONTAINER_NAME,
        user=USER,
        environment={
            "LDAP_ROOT": LDAP_ROOT,
            "LDAP_ADMIN_USERNAME": LDAP_ADMIN_USERNAME,
            "LDAP_ADMIN_PASSWORD": LDAP_ADMIN_PASSWORD,
            "LDAP_CUSTOM_LDIF_DIR": LDAP_CUSTOM_LDIF_DIR,
            "LDAP_ENABLE_SYNCPROV": LDAP_ENABLE_SYNCPROV,
        },
        ports={"1389/tcp": 389, "1636/tcp": 636},
        auto_remove=True,
        volumes={
            LDIF_PATH: {"bind": "/ldifs"},
            ACTIONS_LDIF_PATH: {"bind": "/actions_ldifs"},
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
        container = client.containers.get(CONTAINER_NAME)
        print("OpenLDAP is stopping...")
        container.stop()
        print("OpenLDAP stopped.")
    except docker.errors.NotFound:
        print("Nothing to stop. Container does not exist.")


def wait_for_ldap_server_to_be_ready() -> None:
    """Wait until the ldap server is up and running"""
    print("waiting for openLDAP server to start")
    client = docker.from_env()
    container = client.containers.get(CONTAINER_NAME)
    start_time = datetime.now()
    exit_code = 255
    while exit_code != 0:
        answer = container.exec_run(
            'ldapsearch -x -H ldap://localhost:1389 -b "" -s base "(objectclass=*)"'
        )
        exit_code = answer.exit_code
        if exit_code != 0:
            sleep(COOLDOWN)
        elif (datetime.now() - start_time).seconds < MAX_WAITING_SECONDS:
            raise TimeoutError(
                f"openLDAP server hasn't been able to start in less than {MAX_WAITING_SECONDS}s"
            )
    print("openLDAP server ready")


def get_ldap_container() -> Container:
    """
    Return the openLDAP container.

    :return Container:
    """
    client = docker.from_env()
    container = client.containers.get(CONTAINER_NAME)
    return container
