# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        str1 = ''
        str2 = ''
        
        temp1 = None
        temp2 = None
        
        while l1:
            temp1 = l1.next
            l1.next = temp2
            temp2 = l1
            l1 = temp1
        
        while temp2:
            str1 += str(temp2.val)
            temp2 = temp2.next
        
        temp1 = None
        temp2 = None
        
        while l2:
            temp1 = l2.next
            l2.next = temp2
            temp2 = l2
            l2 = temp1
        
        while temp2:
            str2 += str(temp2.val)
            temp2 = temp2.next
        
            
        sum1 = int(str1) + int(str2)
        
        previousNode = None
        first = None
        
        for i in str(sum1):
            currentNode = ListNode(i)
            if first is None:
                first = currentNode
            if previousNode is not None:
                previousNode.next = currentNode
            previousNode = currentNode
        
        
        temp5 = None
        temp6 = None
        
        while first:
            temp5 = first.next
            first.next = temp6
            temp6 = first
            first = temp5
        
        return temp6