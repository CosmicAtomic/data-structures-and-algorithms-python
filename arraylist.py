# A dynamic array that grows automatically as elements are added.
# Unlike a plain Python list, this simulates a fixed-size backing array (self.data)
# with a separate capacity, doubling it whenever it fills up — the same strategy
# used by Java's ArrayList / C++'s vector, which gives amortized O(1) appends.
class MyArrayList:
    def __init__(self, initial_capacity=10):
        self._size = 0                          # Number of elements actually stored
        self.capacity = initial_capacity
        self.data = [None] * initial_capacity   # Fixed-size backing array

    def add(self, element):
        if self._size == self.capacity:
            self._resize(self.capacity * 2)  # Grow before we run out of room
        self.data[self._size] = element
        self._size += 1

    def insert(self, index, element):
        if index < 0 or index > self._size:
            raise IndexError("Invalid index")
        if self._size == self.capacity:
            self._resize(self.capacity * 2)

        # Shift everything from index onward one slot right to make room
        for i in range(self._size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = element
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Invalid index")
        return self.data[index]

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Invalid index")
        res = self.data[index]
        # Shift everything after index one slot left to close the gap
        for i in range(index, self._size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self._size - 1] = None
        self._size -= 1
        return res

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _resize(self, new_capacity):
        # Allocate a bigger backing array and copy the existing elements over
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity


# Example Usage (for testing)
arr_list = MyArrayList()
arr_list.add(5)
