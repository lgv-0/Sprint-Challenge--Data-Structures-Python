class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if (self.head is None):
            return

        node_list_forward = []

        def down(node):
            node_list_forward.append(node)

            if node.next_node is None:
                return
            else:
                return down(node.next_node)

        down(self.head)

        for i in range(len(node_list_forward), 0, -1):
            current_node = node_list_forward[i - 1]

            if i - 2 < node_list_forward.__len__() and (i - 2) > -1:
                next_node = node_list_forward[i - 2]
                current_node.set_next(next_node)

        self.head = node_list_forward[node_list_forward.__len__() - 1]