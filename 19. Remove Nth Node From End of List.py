'''
19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.


by:shenqiti
2019/7.31
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        index = length - n # the parent node of the removed node
        print(index)

        start = ListNode(0)
        start.next = head
        cur = start
        i = 0
        while i < index:
            cur = cur.next
            i += 1
        x = cur.next
        y = x.next
        cur.next = y

        return start.next


