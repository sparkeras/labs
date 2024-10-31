#include <stdio.h>
// Function to calculate the factorial of a number
long factorial(int n) {
    long result = 1;
    for(int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
int main() {
    int number;
    // Get input from user
    printf("Enter a positive integer: ");
    scanf("%d", &number);
    // Check if number is non-negative
    if (number < 0) {
        printf("Please enter a non-negative integer.\n");
    } else {
        printf("Factorial of %d = %ld\n", number,
               factorial(number));
    }
    return 0;
}
