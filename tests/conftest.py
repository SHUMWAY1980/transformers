# tests directory-specific settings - this file is run automatically
# by pytest before any tests are run

import sys
import warnings
from os.path import abspath, dirname, join


# allow having multiple repository checkouts and not needing to remember to rerun
# 'pip install -e .[dev]' when switching between checkouts and running tests.
git_repo_path = abspath(join(dirname(dirname(__file__)), "src"))
sys.path.insert(1, git_repo_path)


# silence FutureWarning warnings in tests since often we can't act on them until
# they become normal warnings - i.e. the tests still need to test the current functionality
warnings.simplefilter(action="ignore", category=FutureWarning)


def pytest_configure(config):
    config.addinivalue_line("markers", "is_pipeline_test: mark test to run only when pipeline are tested")
    config.addinivalue_line(
        "markers", "is_pt_tf_cross_test: mark test to run only when PT and TF interactions are tested"
    )
