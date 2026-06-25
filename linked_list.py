# A singly linked list with a tail pointer, so add() and removing the head
# stay O(1); insert/get/remove at an arbitrary index still have to walk from
# the head, so those stay O(n).
class Node:
    def __init__(self, data=None):
        self.data = data    # Store the actual data
        self.next = None    # Pointer to the next Node object (None by default)

    def __repr__(self):
        # Print the node's data instead of its memory address
        return f"Node({self.data})"


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    # Tracks the last node so add() doesn't need to walk the list
        self._size = 0      # Underscore avoids clashing with the size() method below

    def add(self, element):
        # Append to the end of the list — O(1) thanks to self.tail
        new_node = Node(element)
        if self.size() == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def insert(self, index, element):
        # Insert at index (0..size inclusive); index == size behaves like add()
        if index > self.size() or index < 0:
            raise IndexError()
        new_node = Node(element)
        pos = 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # Walk to the node just before index, then splice new_node in after it
            prev_node = self.head
            while pos + 1 < index:
                prev_node = prev_node.next
                pos += 1
            new_node.next = prev_node.next
            prev_node.next = new_node
        if new_node.next is None:
            self.tail = new_node   # Inserted at the end — update tail
        self._size += 1

    def get(self, index):
        # Retrieve the element at index (0..size-1) by walking from the head
        if index >= self.size() or index < 0:
            raise IndexError()
        current_node = self.head
        pos = 0
        while pos < index:
            current_node = current_node.next
            pos += 1
        return current_node.data

    def remove(self, index):
        # Remove and return the element at index (0..size-1)
        if index >= self.size() or index < 0:
            raise IndexError()
        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = self.head   # List is now empty — clear tail too
        else:
            # Walk to the node just before index, then splice the target node out
            prev_node = self.head
            pos = 0
            while pos + 1 < index:
                prev_node = prev_node.next
                pos += 1
            current_node = prev_node.next
            if current_node.next is None:
                self.tail = prev_node   # Removed the last node — update tail
            prev_node.next = current_node.next
            removed_data = current_node.data
        self._size -= 1
        return removed_data

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0


# Sanity check
ll = MyLinkedList()
print(ll.is_empty())   # True — list starts empty

ll.add(10)
ll.add(20)
ll.add(30)
print(ll.size())        # 3
print(ll.get(1))         # 20

ll.insert(1, 15)
print(ll.get(1))         # 15 — newly inserted
print(ll.get(2))         # 20 — shifted right by the insert

print(ll.remove(0))      # 10 — removed element is returned
print(ll.get(0))         # 15 — new head
print(ll.tail.data)      # 30 — tail unaffected by removing the head

ll.remove(0)
ll.remove(0)
print(ll.remove(0))      # 30 — removing the last element
print(ll.is_empty())     # True
print(ll.tail)            # None — tail correctly cleared once the list is empty
