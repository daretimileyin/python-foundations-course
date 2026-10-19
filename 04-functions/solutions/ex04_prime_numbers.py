def is_prime(n):
    if n < 2:
        return False
    # Checking up to the square root is enough: if n = a * b, one of a or b
    # must be <= sqrt(n).
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]


assert is_prime(2) is True
assert is_prime(17) is True
assert is_prime(1) is False
assert is_prime(15) is False
assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
print("✅ All checks passed!")
