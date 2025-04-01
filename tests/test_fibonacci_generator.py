import pytest
from src.fibonacci_generator import generate_fibonacci_sequence

def test_fibonacci_sequence_basic():
    """Test basic Fibonacci sequence generation"""
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_sequence_zero_terms():
    """Test generating 0 terms"""
    assert generate_fibonacci_sequence(0) == []

def test_fibonacci_sequence_one_term():
    """Test generating 1 term"""
    assert generate_fibonacci_sequence(1) == [0]

def test_fibonacci_sequence_two_terms():
    """Test generating 2 terms"""
    assert generate_fibonacci_sequence(2) == [0, 1]

def test_fibonacci_sequence_ten_terms():
    """Test generating 10 terms"""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert generate_fibonacci_sequence(10) == expected

def test_fibonacci_negative_input():
    """Test that negative input raises ValueError"""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_fibonacci_non_integer_input():
    """Test that non-integer input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence("5")