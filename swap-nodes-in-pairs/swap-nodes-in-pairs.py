# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        temp = head
        current = temp.next
        Next = current.next
        
        current.next = temp
        temp.next = self.swapPairs(Next)

        return current