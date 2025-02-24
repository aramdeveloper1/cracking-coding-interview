class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Creating a tree
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")

root.add_child(child1)
root.add_child(child2)

print(root.value)  # A
for child in root.children:
    print(child.value)  # B, C
