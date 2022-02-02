"""
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and 
contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, 
then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""
from typing import Deque
from collections import deque


class LRU_Cache(object):

    def __init__(self, cache_size: int):
        self.cache_size: int = cache_size
        self.values = {}
        self.cache_queue: Deque = deque()

    def set(self, key: str, val):
        # Really should add logic for existing key (update)
        self.cache_queue.append(key)
        if len(self.cache_queue) > self.cache_size:
            del self.values[self.cache_queue.popleft()]
        self.values[key] = val

    def get(self, key: str):
        if key in self.values:
            self.cache_queue.append(self.cache_queue.pop(self.cache_queue.index(key)))
            return self.values[key]
        else:
            return None


cache: LRU_Cache = LRU_Cache(2)
cache.set("husband", "Caleb")
cache.set("wife", "Tessa")
cache.set("child", "Elliot")

print(cache.get("husband"))
print(cache.get("wife"))
print(cache.get("child"))
