# A hash table that stores key-value pairs using an array of buckets.
# Keys are hashed to an index; collisions are handled via chaining —
# each bucket is a linked list of Nodes. Automatically doubles capacity
# when the load factor exceeds 0.75.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hashtable:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self._size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        # Map any key to a valid bucket index
        return hash(key) % self.capacity

    def _resize(self):
        # Double capacity and re-insert all existing nodes into the new bucket array
        self.capacity *= 2
        self._size = 0                      
        old_buckets = self.buckets
        self.buckets = [None] * self.capacity
        for bucket in old_buckets:
            current_node = bucket
            while current_node is not None:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next

    def put(self, key, value):
        # Add a new key-value pair, or update the value if the key already exists
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = Node(key, value)
            self._size += 1
        else:
            current_node = self.buckets[index]
            while current_node.next is not None and current_node.key != key:
                current_node = current_node.next
            if current_node.key == key:
                current_node.value = value   # Key exists — update in place, no size change
            else:
                current_node.next = Node(key, value)
                self._size += 1
        if self._size / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        # Return the value for key, or None if key doesn't exist
        index = self._hash(key)
        current_node = self.buckets[index]
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None

    def remove(self, key):
        # Remove and return the value for key, or None if key doesn't exist
        index = self._hash(key)
        current_node = self.buckets[index]
        if current_node is None:
            return None
        if current_node.key == key:
            self.buckets[index] = current_node.next
            self._size -= 1
            return current_node.value
        while current_node.next is not None and current_node.next.key != key:
            current_node = current_node.next
        if current_node.next is None:
            return None                      # Key not found
        removed = current_node.next
        current_node.next = removed.next
        self._size -= 1
        return removed.value

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0


# Sanity check
ht = Hashtable()
ht.put('name', 'Alice')
ht.put('temp', 98.6)
ht.put('age', 30)

ht.put('temp', 99.1)            # update existing key
print(ht.get('temp'))           # 99.1

print(ht.remove('temp'))        # 99.1 — returns removed value
print(ht.get('temp'))           # None — key is gone
print(ht.remove('missing'))     # None — graceful, no crash

print(ht.size())                # 2
print(ht.is_empty())            # False
