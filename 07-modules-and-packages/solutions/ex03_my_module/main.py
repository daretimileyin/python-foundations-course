from mathtools import average, factorial, is_prime

numbers = list(range(1, 21))
print("Primes:", [n for n in numbers if is_prime(n)])
print("10! =", factorial(10))
print("Average of 1..20:", average(numbers))
