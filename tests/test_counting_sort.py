import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting of a list of integers"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = [1, 2, 2, 3, 3, 4, 8]
    assert counting_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted_list():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == expected

def test_large_list_with_duplicates():
    """Test sorting a larger list with duplicates"""
    input_list = [10, 5, 3, 8, 3, 5, 10, 1, 8, 2]
    expected = [1, 2, 3, 3, 5, 5, 8, 8, 10, 10]
    assert counting_sort(input_list) == expected

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_non_integer_elements():
    """Test that a list with non-integer elements raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, "3", 4])

def test_negative_numbers():
    """Test that a list with negative numbers raises a ValueError"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, 2, -3, 4])