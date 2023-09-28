#Write a Python generator that produces prime numbers indefinitely
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Example usage:
prime_generator = generate_primes()
for _ in range(10):  # Generate the first 10 prime numbers
    print(next(prime_generator))

