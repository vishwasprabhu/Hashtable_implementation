"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""


class HashTable:
    def __init__(self, nbuckets):
        self.nbuckets = nbuckets
        self.table = [[] for i in range(nbuckets)]

    def __len__(self):
        length = 0
        for bucket in self.table:
            length += len(bucket)
        return length

    def hashcode(self, key):
        return hash(key) % len(self.table)

    def bucket_indexof(self, table, key):
        """
        You don't have to implement this, but I found it to be a handy function.
        Return the index of the element within a specific bucket; the bucket is:
        table[hashcode(key) % len(table)]. You have to linearly
        search the bucket to find the tuple containing key.
        """
        bucket = table[self.hashcode(key) % len(self.table)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return i
        return None

    def __setitem__(self, key, value):
        bucket = self.table[self.hashcode(key) % len(self.table)]
        tuple_index = self.bucket_indexof(self.table, key)
        if tuple_index is None:
            bucket.append((key, value))
        else:
            bucket[tuple_index] = (key, value)

    def __getitem__(self, key):
        bucket = self.table[self.hashcode(key) % len(self.table)]
        tuple_index = self.bucket_indexof(self.table, key)
        if tuple_index is not None:
            return bucket[tuple_index][1]
        return None

    def __contains__(self, key):
        if self.__getitem__(key):
            return True
        return False

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        return [key for bucket in self.table for key, _ in bucket]

    def items(self):
        return [(key, value) for bucket in self.table for key, value in bucket]

    def __repr__(self):
        s = ''
        for i in range(len(self.table)):
            s += f"{i:04d}->"
            if len(self.table[i]) == 0:
                s += "\n"
            else:
                pairs = [f"{d[0]}:{d[1]}" for d in self.table[i]]
                s += ', '.join(pairs) + '\n'
        return s

    def __str__(self):
        pairs = []
        for i in range(len(self.table)):
            for d in self.table[i]:
                pairs.append(f"{d[0]}:{d[1]}")
        return '{' + ", ".join(pairs) + '}'
