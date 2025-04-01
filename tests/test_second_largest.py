import pytest
from src.second_largest import find_second_largest

def test_normal_array():
    """Test finding second largest in a normal array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_array_with_duplicates():
    """Test finding second largest with duplicate elements."""
    assert find_second_largest([5, 5, 4, 3, 2, 1]) == 4

def test_single_unique_number():
    """Test array with only one unique number."""
    assert find_second_largest([1, 1, 1]) is None

def test_empty_array():
    """Test empty array."""
    assert find_second_largest([]) is None

def test_two_element_array():
    """Test array with two elements."""
    assert find_second_largest([1, 2]) == 1

def test_negative_numbers():
    """Test array with negative numbers."""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_float_numbers():
    """Test array with float numbers."""
    assert find_second_largest([1.5, 2.7, 3.1, 4.2]) == 3.1

def test_invalid_input_type():
    """Test with invalid input type."""
    with pytest.raises(TypeError):
        find_second_largest("not a list")

def test_non_numeric_elements():
    """Test with non-numeric elements."""
    with pytest.raises(ValueError):
        find_second_largest([1, 2, "three", 4])

def test_mixed_number_types():
    """Test array with mixed number types."""
    assert find_second_largest([1, 2.5, 3, 4.7]) == 3