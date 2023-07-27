"""Configure switch test."""
import pytest


@pytest.fixture
def semver_regex():
    regex = r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'
    return regex
