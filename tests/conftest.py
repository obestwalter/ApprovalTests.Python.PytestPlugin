import pytest

import approvaltests

pytest_plugins = 'pytester'

_DEFAULT_REPORTER = approvaltests.get_default_reporter()


@pytest.fixture(autouse=True)
def reset_approvaltests_config(request):
    approvaltests.set_default_reporter(_DEFAULT_REPORTER)
    for option_name in [o for o in vars(request.config.option) if "approvaltests" in o]:
        setattr(request.config.option, option_name, None)
