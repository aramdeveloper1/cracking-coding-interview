# def prime_factors(n):
#     factors = []
#     # Check divisibility by 2 first
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2
    
#     # Check divisibility by odd numbers
#     i = 3
#     while i * i <= n:
#         while n % i == 0:
#             factors.append(i)
#             n //= i
#         i += 2
    
#     if n > 2:  # If n is prime
#         factors.append(n)
    
#     return factors

# # Test
# print(prime_factors(84))  # Output: [2, 2, 3, 7]



def is_prime_naive(n):
    if n < 2:
        return False
    for i in range(2, n):
        print(f"Checking {n} % {i}")
        if n % i == 0:
            print(f"{n} is not prime")
            return False
    return True

# print(is_prime_naive(7))  # Output: True
print(is_prime_naive(10))  # Output: False
