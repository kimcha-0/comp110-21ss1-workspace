from lessons.ls30_node import Node, includes, min

def test_min_empty() -> None:
    assert min(None) is None

def test_min_one() -> None:
    assert min(Node(3, None)) == 3

def test_min_two() -> None:
    assert min(Node(3, Node(1, None))) == 1

def test_empty_list() -> None:
    """Tests for an empty list."""
    assert not includes(None, 5) 

def test_includes_single_elt() -> None:
    """Tests that list has two nodes."""
    assert includes(Node(5, None), 5)

def test_includes_two_elts() -> None:
    """Tests that list has three nodes."""
    assert includes(Node(4, Node(5, None)), 5)

def test_includes_two_elts_2() -> None:
    assert not includes(Node(4, Node(5, None)), 3)

def test_includes_3_elts() -> None:
    assert includes(Node(4, Node(5, Node(3, None))), 3)

