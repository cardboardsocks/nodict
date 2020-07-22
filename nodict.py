#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Ben Mckenzie, google, keith garcia'


class Node:
    def __init__(self, key, value=None):
        """Node class should hash its own key, 
        and keep that hash value as an instance attribute,"""
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """key/value info"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """if equal/compare itself to other Node objects"""
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """init NoDict class"""
        self.buckets = [[] for i in range(num_buckets)]

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """accept a new key and value, and store it into the NoDict instance.
         However, this method should not allow duplicate keys"""
        new_node = Node(key, value)
        index = new_node.hash % len(self.buckets)
        for node in self.buckets[index]:
            if node == new_node:
                self.buckets[index].remove(node)
        self.buckets[index].append(new_node)

    def get(self, key):
        """perform a key-lookup in the NoDict class. It should accept just one parameter: The key to look up. 
        If the key is found in the NoDict class, return its associated value. If the key is not found,
         raise a KeyError exception."""
        node_locator = Node(key)
        index = node_locator.hash % len(self.buckets)
        for node in self.buckets[index]:
            if node == node_locator:
                return node.value
        raise KeyError(f'{key} not located')

    def __getitem__(self, key):
        """enable square-bracket reading behavior"""
        return self.get(key)

    def __setitem__(self, key, value):
        """enable square-bracket assignment behavior"""
        self.add(key, value)