"""
⭐⭐ Exercise 4 – Prime Numbers

A prime number is greater than 1 and can only be divided evenly by 1
and itself: 2, 3, 5, 7, 11, 13 ...

Hint for is_prime: try dividing n by every number from 2 up to n - 1.
If any divides evenly (n % d == 0) it's not prime.
Bonus: you only need to check up to the square root of n. Why?
"""


def is_prime(n):
    """Return True if n is a prime number."""
    # TODO
    pass


def primes_up_to(limit):
    """Return a list of all primes from 2 up to and including limit."""
    # TODO (reuse is_prime!)
    pass


assert is_prime(2) is True
assert is_prime(17) is True
assert is_prime(1) is False
assert is_prime(15) is False
assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
print("✅ All checks passed!")
