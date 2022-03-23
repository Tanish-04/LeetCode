# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
        
        
#         p1 = list1
#         p2 = list2
#         dummynode = ListNode(-1)
#         p3 = dummynode
#         while(p1 != None and p2 != None):
            
#             if p1.val < p2.val:
#                 p3.next = p1
#                 p1 = p1.next
#             else:
#                 p3.next = p2
#                 p2 = p2.next
#             print(p3)
#             p3 = p3.next
            
#         while(p1 != None):
#             p3.next = p1
#             p1=p1.next
#             p3=p3.next
            
            
#         while(p2 != None):
#             p3.next = p2
#             p2=p2.next
#             p3=p3.next
            
            
#         return p3.next