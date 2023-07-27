"""Configure switch test."""
import pytest


@pytest.fixture(scope='session')
def semver_regex():
    regex = r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'
    return regex
