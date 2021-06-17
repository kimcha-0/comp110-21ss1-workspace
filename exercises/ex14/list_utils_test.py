"""Unit tests for functions defined in 6/14's class."""

import pytest
from exercises.ex14.list_utils import max, all, sub, concat

__author__ = "730407570"


def test_example() -> None:
    """2 + 2 = 4."""
    assert 2 + 2

# TODO: Write your unit tests here!


# normal case
def test_max_1_elt() -> None:
    """Testing max function with a list of one element."""
    assert max([1]) == 1

# normal case


def test_max_2_elt() -> None:
    """Testing max with a list of two elements."""
    assert max([1, 2])


# edge case
def test_max_edge_case() -> None:
    """Testing max with empty list."""
    with pytest.raises(ValueError):
        max([])


# normal case
def test_all_1_elt() -> None:
    """Testing all function with list of one element."""
    assert all([1], 1) is True


# normal case
def test_all_multiple_elt() -> None:
    """Testing with list of multiple elements."""
    assert all([1, 1, 1, 1], 1) is True


# normal case
def test_all_multiple_diff_elt() -> None:
    """Testing with list of elements different from needle."""
    assert all([1, 2, 1, 1], 1) is False


# edge case
def test_all_empty() -> None:
    """Testing with empty list."""
    assert all([], 1) is False


# normal case
def test_sub_2_elt() -> None:
    """Testing with lists of 2 elt. Start/stop of entire list."""
    assert sub([1, 2], 0, 3) == [1, 2]


# normal case
def test_sub_multi_elt() -> None:
    """Testing with list of multiple elements."""
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]


# edge case
def test_sub_empty() -> None:
    """Testing with empty list."""
    assert sub([], 0, 5) == []


# edge cases
def test_concat_edge_1() -> None:
    """Testing concat with a empty."""
    assert concat([], [2]) == [2]


def test_concat_edge_2() -> None:
    """Testing concat with b empty."""
    assert concat([1], []) == [1]


def test_concat_edge_3() -> None:
    """Testing concat with bothy empty."""
    assert concat([], []) == []

# normal case


def test_concat_use_1() -> None:
    """Testing conccat with 1 elt each."""
    assert concat([1], [2]) == [1, 2]


def test_concat_use_2() -> None:
    """Testing concat with w lists of different lengths."""
    assert concat([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]