def before_all(context):
    """Executes setup operations before all tests.

    Checks if the environment is defined in userdata. If not, it defaults to 'local'.
    Initializes the Docker client and the Django template engine.

    :param context: Global context containing test configuration information.
    :type context: Context
    """


def after_all(context):
    """Executes cleanup operations after all tests have finished.

    :param context: Global context containing test configuration information.
    :type context: Context
    """


def before_feature(context, feature):
    """Executes setup operations before each feature.

    Retrieves the first tag of the feature being executed and assigns it to the context.

    :param context: Global context containing test configuration information.
    :type context: Context
    :param feature: Object representing the feature being executed.
    :type feature: Feature
    """


def after_feature(context, feature):
    """Executes cleanup operations after each feature.

    Performs necessary teardown tasks after a feature has completed execution.

    :param context: Global context containing test configuration information.
    :type context: Context
    :param feature: Object representing the feature that was executed.
    :type feature: Feature
    """


def before_scenario(context, scenario):
    """Executes setup operations before each scenario.

    Creates a directory to store the scenario logs and clears its contents if it already exists.

    :param context: Global context containing test configuration information.
    :type context: Context
    :param scenario: Object representing the scenario being executed (tags, etc.).
    :type scenario: Scenario
    """


def after_scenario(context, scenario):
    """Executes cleanup operations after each scenario.

    Ensures any temporary data created during the scenario execution is removed.

    :param context: Global context containing test configuration information.
    :type context: Context
    :param scenario: Object representing the scenario that was executed.
    :type scenario: Scenario
    """
