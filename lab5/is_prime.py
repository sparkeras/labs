def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...

    if num == 1:
        return False
    if num == 2:
        return True
    for x in range(2,num):
        if num % x == 0:
            boolean = False
            return boolean
        else:
            boolean = True
    return boolean
# # # Run code example
boolean = is_prime(10)  # returns True
print(boolean)
  
