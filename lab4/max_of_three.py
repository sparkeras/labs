def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...
    
    if num1 >= num2:
        if num1 >= num3:
            maximum = num1
        else:
            maximum = num3
    else:
        if num2 >= num3:
            maximum = num2
        else:
            maximum = num3

    return maximum

print("this code accepts three integers and provides the maximum value. please enter them below")
num1 = int(input("provide your first value "))
num2 = int(input("provide your second value "))
num3 = int(input("provide your third value "))

maximum = max_of_three(num1,num2,num3)
print(maximum,"is the maximum value of the numbers you have provided")
# # You are out of the body function where you can test your code.
# Example usage:
# maximum = max_of_three(10, 20, 30)
# print(maximum, "is the maximum")
