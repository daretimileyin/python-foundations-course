def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


if __name__ == "__main__":
    print("is_prime(7):", is_prime(7))
    print("factorial(5):", factorial(5))
    print("average([1, 2, 3]):", average([1, 2, 3]))
