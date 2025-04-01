def counting_sort(arr):
    """
    Implement Counting Sort algorithm for sorting a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list with the same elements as the input.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if not arr:
        return []
    
    # Check for non-integer elements or negative numbers
    if any(not isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Counting sort only works with non-negative integers")
    
    # Find the maximum value to determine the range
    max_val = max(arr)
    
    # Create counting array initialized with zeros
    count = [0] * (max_val + 1)
    
    # Count occurrences of each unique object
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of each object
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output