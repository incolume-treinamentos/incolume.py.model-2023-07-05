"""Module test."""

import logging

import pytest


def test_void(capsys):
    """Test void."""
    print('oi')
    out, err = capsys.readouterr()
    assert out.strip() == 'oi'
    assert err == ''


@pytest.mark.parametrize(
    'entrance',
    (
        'oi',
        'hi',
        'python',
    ),
)
def test_none(capsys, entrance):
    """Test none."""
    print(entrance)
    out, err = capsys.readouterr()
    logging.debug('%s, %s', out, err)
    assert out.strip() == entrance


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        pytest.param("1+7", 8, marks=pytest.mark.basic),
        pytest.param("2+4", 6, marks=pytest.mark.basic, id="basic_2+4"),
        pytest.param(
            "6*9", 42,
            marks=[pytest.mark.basic, pytest.mark.xfail],
            id="basic_6*9"
        ),
    ],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
