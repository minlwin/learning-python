import re


def fibo(n:int) -> list[int]:
    """Return a list of Fibonacci numbers up to n."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    fibs = [0, 1]
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n+1]

def is_prime(n:int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True