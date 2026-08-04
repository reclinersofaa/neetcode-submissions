class Node:
    def __init__(self, k, v):
        self.key, self.value = k, v
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {} #{ key : ptr to node }
        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    #HELPERS:
    def insert(self, node): #insert at right
        prv = (self.right).prev
        (self.right).prev = prv.next = node
        node.next, node.prev = self.right, prv
    
    def remove(self, node): 
        (node.next).prev = node.prev
        (node.prev).next = node.next

    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key] = Node(key, value)
        self.insert(self.hm[key])

        if len(self.hm) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hm[lru.key]
