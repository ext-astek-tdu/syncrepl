"""Environement file from behave framework"""

from behave.runner import Context
from behave.model import Scenario  # , Feature

from tests.behave.common.docker_tools import (
    start_openldap,
    stop_openldap,
)
from tests.behave.common.singleton import Singleton
from tests.behave.common.virtual_user_client import VirtualUserClient


def before_all(context: Context) -> None:
    """Executes setup operations before all tests.

    Checks if the environment is defined in userdata. If not, it defaults to 'local'.
    Initializes the Docker client and the Django template engine.

    :param context: Global context containing test configuration information.
    :type context: Context
    """
    stop_openldap()


def after_all(context: Context) -> None:
    """Executes cleanup operations after all tests have finished.

    :param context: Global context containing test configuration information.
    :type context: Context
    """


def before_scenario(context: Context, scenario: Scenario) -> None:
    """Executes setup operations before each scenario.

    Set up all potential needed object.

    :param context: Global context containing test configuration information.
    :type context: Context
    :param scenario: Object representing the scenario being executed (tags, etc.).
    :type scenario: Scenario
    """
    Singleton.virtual_user_client = VirtualUserClient()
    ldap_container = start_openldap()
    Singleton.ldap_container = ldap_container



# def after_scenario(context: Context, scenario: Scenario) -> None:
#     """Executes cleanup operations after each scenario.

#     Delete all potential used object

#     :param context: Global context containing test configuration information.
#     :type context: Context
#     :param scenario: Object representing the scenario that was executed.
#     :type scenario: Scenario
#     """
#     Singleton.virtual_user_client.stop_client()
#     stop_openldap()


# def before_feature(context: Context, feature: Feature) -> None:
#     """Executes setup operations before each feature.

#     Retrieves the first tag of the feature being executed and assigns it to the context.

#     :param context: Global context containing test configuration information.
#     :type context: Context
#     :param feature: Object representing the feature being executed.
#     :type feature: Feature
#     """


# def after_feature(context: Context, feature: Feature) -> None:
#     """Executes cleanup operations after each feature.

#     Performs necessary teardown tasks after a feature has completed execution.

#     :param context: Global context containing test configuration information.
#     :type context: Context
#     :param feature: Object representing the feature that was executed.
#     :type feature: Feature
#     """
