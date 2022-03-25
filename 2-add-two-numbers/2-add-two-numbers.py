# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        
        dummy = ListNode()
        node = dummy
        carry = 0
        
        while l1 or l2:
            Sum = 0
            
            if l1:
                Sum += l1.val
                l1 = l1.next
            if l2:
                Sum += l2.val
                l2 = l2.next
            
            Sum += carry
            carry, remainder = divmod(Sum,10)
            node.next = ListNode(remainder)
            node = node.next
            
        if carry > 0:
            node.next = ListNode(carry)
            
        return dummy.next
        