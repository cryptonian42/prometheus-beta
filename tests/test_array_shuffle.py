import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of an array."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that all original elements are present
    assert set(shuffled) == set(original)
    
    # Check that the order is different (with high probability)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty array."""
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    """Test shuffling an array with a single element."""
    arr = [42]
    assert shuffle_array(arr) == arr

def test_shuffle_array_different_types():
    """Test shuffling an array with different types of elements."""
    original = [1, 'a', True, None, 3.14]
    shuffled = shuffle_array(original)
    
    assert set(shuffled) == set(original)
    assert shuffled != original

def test_shuffle_array_preserves_original():
    """Ensure the original array is not modified."""
    original = [1, 2, 3, 4, 5]
    _ = shuffle_array(original)
    
    assert original == [1, 2, 3, 4, 5]

def test_shuffle_array_invalid_input():
    """Test that invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)

def test_shuffle_randomness():
    """Test that multiple shuffles produce different orders."""
    original = list(range(10))
    
    # Set a seed for reproducibility of this test
    random.seed(42)
    
    # Perform multiple shuffles
    shuffles = [shuffle_array(original) for _ in range(10)]
    
    # Check that not all shuffles are identical
    assert len(set(tuple(shuffle) for shuffle in shuffles)) > 1