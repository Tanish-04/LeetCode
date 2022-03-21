# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # Time Complexity O(n)
        # Space Complexity O(1)
        
        temp_1 = None
        temp_2 = None
        
        while (head != None):
            temp_2 = head.next
            head.next = temp_1
            temp_1 = head
            head = temp_2
 
        head = temp_1
    
        return head