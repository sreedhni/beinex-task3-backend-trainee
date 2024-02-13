# Write a Python program to create Fibonacci series up to n using Lambda. 

fibonacci_series = lambda n: [0, 1] if n == 2 else fibonacci_series(n - 1) + [fibonacci_series(n - 1)[-1] + fibonacci_series(n - 1)[-2]]

def fibonacci(n):
    fibonacciseries = fibonacci_series(n)
    print("Fibonacci series up to", n, ":")
    print(fibonacciseries)
num=int(input("enter a num"))
fibonacci(num)
