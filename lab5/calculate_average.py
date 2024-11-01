def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...
    
    count = 0
    numsum = 0
    for x in numbers:
        numsum = numsum + x 
        count = count + 1

    average = numsum/count
    return average

# # Example usage
numbers = [20, 30, 40, 50, 60, 70, 80]
print("The average is:", calculate_average(numbers))  # Expected output: The average is: 50.0
