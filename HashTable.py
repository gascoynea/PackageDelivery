# Self adjusting algorithm in form of hashtable
class Hashtable:
    def __init__(self):
        self.size = 64
        self.hashmap = [[] for _ in range(0, self.size)]

    # hashes the key
    def hash_func(self, key):
        hashing_key = hash(key) % self.size
        return hashing_key

    # Used to insert data from packages
    def insert(self, key, value):
        hash_key = self.hash_func(key)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k,v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    # Used to get information on whichever package
    def get(self, key):
        hash_key = self.hash_func(key)
        bucket = self.hashmap[hash_key]
        if not bucket:
            raise KeyError("Key not found")
        for kv in bucket:
            k, v = kv
            if key == k:
                return v

    # if needed can remove a package from the hashtable
    def remove(self, key):
        hash_key = self.hash_func(key)
        bucket = self.hashmap[hash_key]
        if not bucket:
            raise KeyError("Key not found")
        for kv in bucket:
            k, v = kv
            if key == k:
                bucket.remove(kv)

# instantiating the hash table as H
H = Hashtable()

