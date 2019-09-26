'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4



By:shenqiti
2019/9/26

'''
'''
This problem keeps moving the most frequently used node to the head, and delete the node before tail node.
The double linked list takes constant time O(1) to add and remove nodes from the head or tail, and the node can remove itself without other references.
#add node in doubly linked list right after head.
head  <====  (node)  ====>  head.next
# node.prev = head           node.next = head.next
head <------  node    ------>  head.next
# head.next.prev = node
head          node    <------  head.next
# head.next  = node
head ------ > node    <=====>  head.next
# remove node in doubly linked list:

previous node   ====  node  ====  next node
prev = node.prev                   new = node.next
prev ---------------------------------> new
prev <--------------------------------- new


Use the dictionary here is to count the frequency of a node. Use the information saved in the dictionary to determine which node to delete when the size of the Double linked list exceeds the capacity.

'''

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self


class LRUCache:

    def __init__(self, capacity):
        self.dic = dict()  # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.dic:  # similar to get()        
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value  # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)
