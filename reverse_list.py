# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        
        new_head = self.reverseList(head.next)
        b = head.next
        b.next = head
        head.next = None
        return new_head
