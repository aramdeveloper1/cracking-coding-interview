class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists for collision handling
        print(self.table)
    def hash(self, key):
        # Simple hash function (sum of ASCII values modulo table size)
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        # Check if the key already exists, and update value if so
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If the key doesn't exist, append new pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # If key not found

# # Example usage:
# hash_table = HashTable(10)
# hash_table.insert("name", "Alice")
# print(hash_table.get("name"))  # Output: Alice
# # hash_table.insert("name", "Bob")
# # print(hash_table.get("name"))  # Output: Bob


class ArrayList:
    def __init__(self):
        self.array = []
    
    def add(self, element):
        self.array.append(element)  # O(1) on average
    
    def get(self, index):
        return self.array[index] if index < len(self.array) else None

# Example usage:
# array_list = ArrayList()
# array_list.add(1)
# array_list.add(2)
# array_list.add(3)
# print(array_list.get(0))  # Output: 1
# print(array_list.get(2))  # Output: 3

class ArrayList:
    def __init__(self):
        self.array = []
    def add(self,element):
        self.array.append(element)  
    def get(self,index):
        return self.array[index] if index < len(self.array) else None
    def remove(self,index):
        if index < len(self.array):
            self.array.pop(index)
            return True
        return False

# # Example usage:    
# array_list = ArrayList()
# array_list.add(1)
# array_list.add(2)
# array_list.add(3)
# print(array_list.get(0))  # Output: 1
# print(array_list.get(2))  # Output: 3
# array_list.remove(0)
# print(array_list.get(0))  # Output: 2

def join_words(words):
    new_string = ""
    for word in words:
        new_string += word + " "
    return new_string.strip()

# Example usage:
# print(join_words(["hello", "world"]))  # Output: "hello world"

# Inefficient concatenation: If you were to use the + operator repeatedly (like in the first version of joinWords), the time complexity would grow as O(n²) because each concatenation creates a new string.
def join_words(words):
    sentence = []  # Use a list to collect the words
    for w in words:
        sentence.append(w)  # Append each word (O(1) operation)
    return ' '.join(sentence)  # Efficiently join the list into a single string

# Example usage:
# words = ["hello", "world", "from", "python"]
# result = join_words(words)
# print(result)  # Output: helloworldfrompython
# # The time complexity of this implementation is O(n), where n is the total number of characters in the input words.Efficient concatenation: By using a list to store intermediate results and calling join() at the end, the time complexity becomes O(n), where n is the total number of characters.

def is_unique(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# Example usage:
# print(is_unique("abcdef"))  # Output: True
# print(is_unique("aabbcc"))  # Output: False

def check_permutations(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

# Example usage:
# print(check_permutations("abc", "cba"))  # Output: True
# print(check_permutations("abc", "def"))  # Output: False

def urlify(s, length):
    # Replace spaces with %20
    return s.replace(" ", "%20")

# Example usage:
# s = "hello world"
# length = 11
# result = urlify(s, length)
# print(result)  # Output: "hello%20world"

def urlify(s, true_length):
    return s[:true_length].replace(" ", "%20")

# Example usage:
# print(urlify("Mr John Smith ", 13))  # Output: "Mr%20John%20Smith"
from collections import Counter

def palindrome_permutation(s):
    s = s.replace(" ", "").lower() 
    print("s *",s)
    char_count = Counter(s)
    print("char_count *",char_count)
    odd_count = sum(2 for count in char_count.values() if count % 2 == 0)
    print("odd_count *",odd_count)
    return odd_count <= 2

# Example usage:
# print(palindrome_permutation("Tact Coa"))  # Output: True
# print('________________')  # Output: False
# print(palindrome_permutation("ara aram khasrok"))  # Output: False

def one_away(s1, s2):
    print("abs(len(s1) - len(s2)) *",abs(len(s1) - len(s2)))
    print("** len(s1) == len(s2) *",len(s1) == len(s2))
    print("-- len(s1) + 1 == len(s2) *",len(s1) + 1 == len(s2))
    print("++ len(s2) + 1 == len(s1) *",len(s2) + 1 == len(s1))
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        return sum(1 for a, b in zip(s1, s2) if a != b) <= 1
    elif len(s1) + 1 == len(s2):
        return s1 == s2[:-1]
    elif len(s2) + 1 == len(s1):  # Corrected condition
        return s1[:-1] == s2
    return False

# print(one_away("pale", "ple"))  # Output: True
# print(one_away("pale", "bake"))  # Output: False
# print(one_away("pales", "pale")) # Output: True
# print(one_away("pale", "bale")) # Output: True
def string_compression(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            print("s[i] *",s[i],"s[i-1] *",s[i-1])
            count += 1
            print("count *",count)
        else:
            compressed.append(s[i - 1] + str(count))
            print("compressed *",compressed)
            count = 1
    print("********* compressed ",compressed)
    compressed.append(s[-1] + str(count))  # Append last character
    compressed_string = ''.join(compressed)
    return compressed_string if len(compressed_string) < len(s) else s

# Example usage:
# print(string_compression("aabcccccaaa"))  # Output: "a2b1c5a3"
# print(string_compression("abcd"))  # Output: "abcd"
# print(string_compression("aaabbbccc"))  # Output: "a3b3c3"


def rotate_matrix(matrix):
    n = len(matrix)
    print("n *",n)
    # Transpose
    for i in range(n):
        print("i *",i)
        for j in range(i + 1, n):
            print("j *",j)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print("matrix *",matrix)
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 0, 6],
#     [7, 8, 9]
# ]
# rotate_matrix(matrix)
# print(matrix)
def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    print("zero_rows *",zero_rows)
    print("zero_cols *",zero_cols)
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                print("i *",i)
                print("j *",j)
                print("matrix[i][j] *",matrix[i][j])
                matrix[i][j] = 0
    return matrix

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
# print(zero_matrix(matrix))
# # print(matrix)