import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)

        relative_node = None
        hunt_node = self
        while relative_node is None:
            if hunt_node.value > value:
                if hunt_node.left is not None:
                    hunt_node = hunt_node.left
                else:
                    relative_node = hunt_node
            else:
                if hunt_node.right is not None:
                    hunt_node = hunt_node.right
                else:
                    relative_node = hunt_node
        
        if relative_node.value < value:
            relative_node.right = new_node
        else:
            relative_node.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def seek(cur_node):
            if cur_node.value == target:
                return True

            if cur_node.value > target:
                if cur_node.left is None:
                    return False
                else:
                    return seek(cur_node.left)
            elif cur_node.value < target:
                if cur_node.right is None:
                    return False
                else:
                    return seek(cur_node.right)

        return seek(self)

bst = BSTNode("Logan Van Hook")

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
