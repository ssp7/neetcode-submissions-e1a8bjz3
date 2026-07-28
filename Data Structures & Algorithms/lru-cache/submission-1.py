class Node:
    def __init__(self, key, val):
        self.prev = self.next = None
        self.key, self.val = key, val
        
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev = self.left
        self.left.next = self.right
    
    # remove node
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # add node at the end
    def add(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
       
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        
        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

        
        
