import random


random.seed(1024160035)

numbers = [random.randint(100, 900) for _ in range(100)]
print(numbers)
odd_numbers = [num for num in numbers if num % 2 != 0]

print("\nOdd Numbers:")
print(odd_numbers)
print("Number of odd numbers:", len(odd_numbers))

even_numbers = [num for num in numbers if num % 2 == 0]

print("\nEven Numbers:")
print(even_numbers)
print("Number of even numbers:", len(even_numbers))

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

prime_numbers = [num for num in numbers if is_prime(num)]

print("\nPrime Numbers:")
print(prime_numbers)
print("Number of prime numbers:", len(prime_numbers))

from collections import Counter
frequency = Counter(numbers)

most_frequent_number, occurrence_count = frequency.most_common(1)[0]

print("\nMost Frequently Occurring Number:", most_frequent_number)
print("Number of occurrences:", occurrence_count)