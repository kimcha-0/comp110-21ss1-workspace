"""Unit tests for list_utils."""

import pytest
from lessons.ls28_list_utils import max, concat


def test_concat_edge_1() -> None:
    """Testing concat with a empty."""
    assert concat([], [2]) == [2]

def test_concat_edge_2() -> None:
    """Testing concat with b empty."""
    assert concat([1], []) == [1]


def test_concat_edge_3() -> None:
    """Testing concat with bothy empty."""
    assert concat([], []) == []


def test_concat_use_1() -> None:
    """Testing conccat with 1 elt each."""
    assert concat([1], [2]) == [1, 2]

def test_concat_use_2() -> None:
    assert concat([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


def test_max_1() -> None:
    """Tests max with a single element."""
    assert max([110]) == 110


def test_max_2() -> None:
    """Tests max with a multiple element."""
    assert max([1, 5, 2]) == 5


def test_max_edge_case() -> None:
    """Testing max with empty list."""
    with pytest.raises(ValueError):
        max([])