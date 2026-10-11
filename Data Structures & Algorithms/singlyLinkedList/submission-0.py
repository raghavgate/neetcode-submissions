class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current == None:
                return -1
            current = current.next
        if current == None:
            return -1
        return current.val
        

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head     

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        if self.head is None:
            self.head = new_tail
            return
        current = self.head 
        while current.next is not None:
            current = current.next
        current.next = new_tail
        
    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        current = self.head
        for i in range(index - 1):
            if current is None:
                return False
            current = current.next
        if current == None or current.next is None:
            return False
        current.next = current.next.next
        return True

    def getValues(self) -> List[int]:
        values_list = []
        current = self.head
        while current is not None:
            values_list.append(current.val)
            current = current.next
        return values_list
            
        
