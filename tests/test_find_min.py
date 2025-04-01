import pytest
from src.find_min import find_min

def test_find_min_basic():
    """Test finding minimum in a standard list of numbers."""
    assert find_min([5, 2, 9, 1, 7]) == 1

def test_find_min_negative_numbers():
    """Test finding minimum with negative numbers."""
    assert find_min([-1, -5, 0, 3, -10]) == -10

def test_find_min_floats():
    """Test finding minimum with floating point numbers."""
    assert find_min([1.5, 2.3, 0.1, 4.7]) == 0.1

def test_find_min_single_element():
    """Test finding minimum in a single-element list."""
    assert find_min([42]) == 42

def test_find_min_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum in an empty array"):
        find_min([])

def test_find_min_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_min("not a list")

def test_find_min_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_min([1, 2, "three", 4])

def test_find_min_mixed_numeric_types():
    """Test finding minimum with mixed numeric types (int and float)."""
    assert find_min([5, 2.5, 3, 1.1]) == 1.1