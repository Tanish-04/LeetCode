# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''result act as a pointer after comparing element of list1 and list2
        and every element which point in the result will also add into dummy variable
        a complete linked list will be generated into dummy node
        '''
        dummy = ListNode(-1)
        result = dummy
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
                
        result.next = list1 if list1 != None else list2
        
            
        return dummy.next
        