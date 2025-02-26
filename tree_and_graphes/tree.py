class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# # Creating a tree
# root = TreeNode("A")
# child1 = TreeNode("B")
# child2 = TreeNode("C")

# root.add_child(child1)
# root.add_child(child2)

# print(root.value)  # A
# for child in root.children:
#     print(child.value)  # B, C
def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    print("first row and first column",dp)
    for j in range(n):
        dp[0][j] = 1
    for i in range(m):
        dp[i][0] = 1
    print("seocond row and second column",dp)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            print("dp[",i,",",j,"] = dp[",i-1,",",j,"] + dp[",i,",",j-1,"]",dp[i][j])
    print("final result",dp[m-1][n-1])
    return dp[m-1][n-1]
# print(uniquePaths(3,2))



from collections import deque

def bfs(graph, start, end):
    """Check if a path exists from 'start' to 'end' using BFS"""
    if start == end:
        return True  # If start and end are the same, return True

    queue = deque([start])  # Initialize queue with start node
    visited = set()  # Keep track of visited nodes
 
    while queue:
        current_node = queue.popleft()  # Dequeue the first node
        print("current_node",current_node)
        if current_node == end:
            print("Found the target node")
            return True  # Found the target node

        visited.add(current_node)  # Mark as visited
        print("visited ",visited)
        # Add unvisited neighbors to the queue
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)  
                print("queue ",queue)

    return False  # No path found

# Example Graph
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Test the function
# print(bfs(graph, "A", "F"))  # Output: True (A → C → E → F)
# print(bfs(graph, "A", "D"))  # Output: True (A → B → D)
# print(bfs(graph, "A", "Z"))  # Output: False (Z is not in the graph)


# # Check if there is a route from A to F
# print(bfs(graph, "A", "F"))  # True
# print(bfs(graph, "A", "D"))  # True
# print(bfs(graph, "B", "C"))  # False

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minimal_tree(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = minimal_tree(arr[:mid])
    root.right = minimal_tree(arr[mid+1:])
    return root

# Helper function to print in-order traversal
def inorder(root):
    if root:
        inorder(root.left)
        print("root left",root.value, end=" ")
        print(root.value, end=" ")
        inorder(root.right)
        print("root right", root.value, end=" ")

# Example usage
# sorted_array = [1, 2, 3, 4, 5, 6, 7]
# root = minimal_tree(sorted_array)
# inorder(root)  # Output: 1 2 3 4 5 6 7

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.value, end=" ")  # Visit root
        preorder(root.left)
        preorder(root.right)

# Example Tree
# root = TreeNode("A")
# root.left = TreeNode("B")
# root.right = TreeNode("C")
# root.left.left = TreeNode("D")
# root.left.right = TreeNode("E")

# preorder(root)  # Output: A B D E C
# n = 10000000000
# m = 10011
# s = 2
# t = 5
# new_n = "".join(str(n))
# for i in range(len(new_n)):
#     print(new_n[i])
#     if i == s:
#         new_n = new_n[:i] + str(t) + new_n[i+1:]
#         print("new_n",new_n)
def binary_to_string(num):
    if num <= 0 or num >= 1:
        return "ERROR"
    
    result = "0."
    while num > 0:
        if len(result) >= 34:  # 2 for "0." + 32 bits
            return "ERROR"
        
        num *= 2
        if num >= 1:
            result += "1"
            num -= 1
        else:
            result += "0"
    
    return result

print(binary_to_string(0.72))  # Likely to return "ERROR"
print(binary_to_string(0.5))   # "0.1"
print(binary_to_string(0.1))   # "0.000110011001101"