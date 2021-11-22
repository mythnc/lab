class Node:
    def __init__(self, key, value, prev=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = prev

class MyHashMap:
    SIZE = 10000

    def __init__(self):
        self.ary = [None] * self.SIZE

    def put(self, key: int, value: int) -> None:
        index = key % self.SIZE

        # insert in head
        if self.ary[index] is None:
            self.ary[index] = Node(key, value)
            return

        node = self.ary[index]
        while node.next is not None and node.key != key:
            node = node.next

        # update
        if node.key == key:
            node.value = value
            return

        # insert in tail
        if node.next is None:
            node.next = Node(key, value, node)
            return

    def get(self, key: int) -> int:
        index = key % self.SIZE

        node = self.ary[index]
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return -1

        return node.value

    def remove(self, key: int) -> None:
        index = key % self.SIZE

        node = self.ary[index]
        while node is not None and node.key != key:
            node = node.next

        # not exist
        if node is None:
            return 

        if node.key == key:
            # head
            if node.prev is None:
                if node.next is None:
                    self.ary[index] = None
                else:
                    self.ary[index] = node.next
                    self.ary[index].prev = None
                return

            node.prev.next = node.next
            # not tail
            if node.next is not None:
                node.next.prev = node.prev
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

h = MyHashMap()
h.put(2,2)
h.put(2,1)
h.get(2)
