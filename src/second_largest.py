def find_second_largest(arr):
    """
    Find the second largest number in an array.

    Args:
        arr (list): A list of numbers to search through.

    Returns:
        int or None: The second largest number in the array, 
                     or None if the array has fewer than 2 unique numbers.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-numeric elements.

    Examples:
        >>> find_second_largest([1, 2, 3, 4, 5])
        4
        >>> find_second_largest([5, 5, 4, 3, 2, 1])
        4
        >>> find_second_largest([1, 1, 1])
        None
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(arr) < 2:
        return None
    
    # Validate all elements are numbers
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    # Return second element if exists, else None
    return unique_sorted[1] if len(unique_sorted) > 1 else None