# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        firstNode = lastNode = head
        
        for _ in range(n):
            lastNode = lastNode.next
            
        if lastNode == None:
            return head.next
        
        while lastNode.next != None:
            lastNode = lastNode.next
            firstNode = firstNode.next
            
        firstNode.next = firstNode.next.next
        
        return head
        