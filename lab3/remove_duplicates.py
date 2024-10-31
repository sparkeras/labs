def remove_duplicates(numbers):
    singles = set(numbers)
    unique_numbers = list(singles)

    """
    Removes duplicates from a list of numbers and returns a new list with unique elements.

    Parameters:
    ----------
    numbers : list
        A list of numbers which may contain duplicate values.

    Returns:
    -------
    list
        A new list with duplicate values removed.
    
    Example:
    --------
    remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # Output: [1, 2, 3, 4, 5]
    """
    # Hint: Convert the list to a set to remove duplicates, then convert it back to a list
    # List --> Set (remove duplicates) --> List (return the list)
    # Write your code here...

    print(unique_numbers)
    return unique_numbers
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
remove_duplicates(numbers)
