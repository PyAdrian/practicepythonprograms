# Recursive Iterative
def factorial(n):
    # single line to find the factorial
    return 1 if (n == 1 or n == 0) else n*factorial(n - 1)

# Driver code
num = 5
print("Factorial of",num,"is",factorial(num))
