class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0
        

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.count:
            return -1
        
        current = self.head
        for _ in range(0,index):
            current = current.next
        
        return current.val
        

    def addAtHead(self, val: int) -> None:
        
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        
        self.addAtIndex(self.count,val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.count:
            return
         
        temp = self.head
        newNode = Node(val)
        
        if index == 0:
            newNode.next = temp
            self.head = newNode
        else:
            for _ in range(index-1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
        self.count += 1
            
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return -1
        
        temp = self.head
        
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0,index-1):
                temp = temp.next
            temp.next = temp.next.next
        self.count -= 1
        
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)