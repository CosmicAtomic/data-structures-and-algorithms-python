# A hash table that stores key-value pairs.
# Keys are converted to a numeric hash to determine where to store the value.
# Collisions (different keys with the same hash) are handled via chaining —
# each bucket is itself a dict that can hold multiple keys.
class HashTable:
    def __init__(self):
        # The outer dict maps a hash number to a bucket.
        # Each bucket is an inner dict mapping the original key to its value.
        self.collection = {}

    def hash(self, string):
        # Converts a string key into a number by summing the Unicode value of each character.
        # e.g. 'golf' → ord('g')+ord('o')+ord('l')+ord('f') = 418
        # Note: different strings can produce the same sum (a "collision").
        unicode_sum = sum(ord(char) for char in string)
        return unicode_sum

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            # First time seeing this hash — create a new bucket for it
            self.collection[hashed_key] = {}
        # Store the key-value pair inside the bucket (handles collisions naturally)
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            # No bucket for this hash — key was never added
            return
        if key not in self.collection[hashed_key]:
            # Bucket exists but the specific key isn't in it
            return
        # Remove the key from its bucket
        self.collection[hashed_key].pop(key)

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            # No bucket for this hash — key doesn't exist
            return None
        elif key not in self.collection[hashed_key]:
            # Bucket exists but key isn't in it (was never added or was removed)
            return None
        else:
            return self.collection[hashed_key][key]


table = HashTable()

# 'golf', 'read', and 'dear' all have a Unicode sum of 418 — they collide!
# All three will end up in the same bucket, demonstrating chaining.
table.add('golf', 'sport')
table.add('read', 'book')
table.add('dear', 'friend')

print(table.collection)       # {418: {'golf': 'sport', 'read': 'book', 'dear': 'friend'}}
print(table.lookup('golf'))   # 'sport'
