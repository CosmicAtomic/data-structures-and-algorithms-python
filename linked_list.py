# A singly linked list where each node points to the next one in the chain.
# Unlike a regular list, there's no indexing — you traverse from the head node forward.
class LinkedList:

    # Each node stores a value and a pointer to the next node.
    # next is None by default, meaning "end of the list".
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None  # Will be updated when a node is linked to another

    def __init__(self):
        self.length = 0    # Tracks how many nodes are in the list
        self.head = None   # Points to the first node; None means the list is empty

    def is_empty(self):
        return self.length == 0

    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            # If the list is empty, the new node becomes the head
            self.head = node
        else:
            # Otherwise, walk to the last node and attach the new one there
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head

        # Walk the list until we find the element or reach the end
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            # Element wasn't found — nothing to remove
            return
        elif previous_node is not None:
            # Middle or tail node: skip over the current node
            previous_node.next = current_node.next
        else:
            # Head node: move head forward to the next node
            self.head = current_node.next
        self.length -= 1

my_list = LinkedList()
print(my_list.is_empty())  # True — list starts empty

my_list.add(1)
my_list.add(2)
print(my_list.is_empty())  # False — list now has elements
print(my_list.length)      # 2
