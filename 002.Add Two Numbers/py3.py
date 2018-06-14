# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = 0
        tens = 1
        while l1 or l2:
            if l1:
                s += l1.val * tens
                l1 = l1.next
            if l2:
                s += l2.val * tens
                l2 = l2.next
            tens *= 10
        return [int(char) for char in str(s)[::-1]]
            
