'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

_______________________________________________
Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
______________________________________________
By : shenqiti
2019/7/28
'''


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3h = ListNode(0)
        l3 = l3h
        temps = 0

        while l1 or l2 or temps:
            if l1:
                temps += l1.val
                l1 = l1.next
            if l2:
                temps += l2.val
                l2 = l2.next
            l3.next = ListNode(temps % 10)
            l3 = l3.next
            temps = temps // 10
        return l3h.next
