# Runtime Complexity: O(N)
def foo(array):
    sum_value = 0
    product = 1

    for num in array:
        sum_value += num

    for num in array:
        product *= num

    print(f"{sum_value}, {product}")

# Example usage
# foo([1, 2, 3, 4])

# Runtime Complexity: O(N²)
def print_pairs(array):
    for i in array:
        for j in array:
            print(f"{i},{j}")

# Example usage
# print_pairs([1, 2, 3])

# Runtime Complexity: O(A × B)
def print_unordered_pairs(arrayA, arrayB):
    for a in arrayA:
        for b in arrayB:
            if a < b:
                print(f"{a},{b}")

# Example usage
# print_unordered_pairs([1, 2, 3], [3, 4, 5])


# Runtime Complexity: O(A × B)

def print_unordered_pairs_large(arrayA, arrayB):
    for a in arrayA:
        for b in arrayB:
            for _ in range(100000):  # Constant time
                print(f"{a},{b}")

# Example usage (commented out to avoid excessive output)
# print_unordered_pairs_large([1, 2], [3, 4])



# Runtime Complexity: O(N)
# The loop runs only half the length of the array, but in Big-O, O(N/2) simplifies to O(N).
def reverse_array(array):
    n = len(array)
    for i in range(n // 2):
        other = n - i - 1
        array[i], array[other] = array[other], array[i]

    return array

# Example usage
# print(reverse_array([1, 2, 3, 4, 5]))

# import math

# N = 1000
# M = 2000
# P = 500

# print(f"O(N + P) -> O({N} + {P}) = {N + P} ≈ O(N)")
# print(f"O(2N) -> O(2 × {N}) = {2 * N} ≈ O(N)")
# print(f"O(N + logN) -> O({N} + log({N})) = {N + math.log(N)} ≈ O(N)")
# print(f"O(N + M) -> O({N} + {M}) = {N + M} (No simplification)")


def sort_strings(arr):
    sorted_arr = [''.join(sorted(s)) for s in arr]
    print("sorted_arr: ", sorted_arr)
    sorted_arr.sort()
    return sorted_arr

# Example usage
arr = ["cat", "dog", "tac", "god", "act"]
# print(sort_strings(arr))



# sorted_arr = []
# for s in arr:
#     sorted_s = sorted(s)
#     print("sorted_s: ", sorted_s)
#     sorted_s_joined = ''.join(sorted_s)
#     print("sorted_s_joined: ", sorted_s_joined)
    
#     sorted_arr.append(sorted_s_joined)

# print("sorted_arr: ", sorted_arr)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

def sum_tree(node):
    if node is None:
        return 0
    return sum_tree(node.left) + node.value + sum_tree(node.right)

# Example usage
# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# print(sum_tree(root))  # Output: 30

# rage d ja n
# Time Complexity Analysis
def is_prime(n):
    if n < 2:
        return False
    print("n ** 0.5: ", int(n ** 0.5) + 1)
    print("n ** 0.5: ", int(n ** 0.5) + 1)
    for x in range(2, int(n ** 0.5) + 1):
        print("*** x: ", x)
        if n % x == 0:
            print("n: ", n, "x: ", x)
            return False
    return True

# Example usage
# print(is_prime(35))  # Output: True



# recursive function to calculate the factorial of a number
# Time Complexity Analysis
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
# print(factorial(5))  # Output: 120


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Example usage
# print(fib(10))  # Output: 55

# Time Complexity Analysis
def fib_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    prev_prev = 0
    prev = 1
    for i in range(2, n + 1):
        curr = prev_prev + prev
        prev_prev = prev
        prev = curr
    return curr

# Example usage
# print(fib_iterative(10))  # Output: 55

# Total Complexity: 
# 𝑂
# (
# 2
# 𝑁
# )
# O(2 
# N
#  ).
def all_fib(n):
    for i in range(n):
        print(f"{i}: {fib(i)}")

# Example usage
# all_fib(10)


def product(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result

# print(product(10, 4))  



def mod(a, b):
    if b <= 0:
        return -1  # Error case
    div = a // b
    return a - div * b

print(mod(10, 3))  # Output: 1
