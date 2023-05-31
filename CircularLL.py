class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None

    def insert_at_start(self,some_data:int)-> None: 
        data = Node(some_data)
        current = self.head
        Temp= None
        if current:
            Temp = current
            self.head = data
            data.next = Temp

    def insert_at_end(self,some_data):
        
        data = Node(some_data)
        current = self.head
        
        if self.head == None:
            self.head = data
        else:
            while current.next is not None:
                current = current.next
            current.next = data
            data.next = self.head
    
    def insert_anywhere(self,some_value,pos :int):
        '''Consider the Concept of Indexing and Enter the Pos value from 0'''
        new_value = Node(some_value)
        current = self.head
        count = 0
        if pos == 0: # inserting at start
            new_value.next = self.head
            self.head = new_value
            
        else:
            while current is not None:
                count +=1
                if count == pos:
                    new_value.next = current.next
                    current.next = new_value
                    return
                elif count != pos:
                     current = current.next

    def delete(self,some_value):
        key = some_value
        current = self.head
        prev = None
        while current is not None:
            if current.data == key:
                if prev is None: # Delete at the Start
                    self.head = current.next  
                    current = self.head
                else: 
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next    

    def PrintLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next        
    
    def Reversal(self):
        prev = None
        current = self.head
        while current is not None:
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        self.head = prev; 

                       

ll = SLL()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(4)
ll.insert_anywhere(3,2)
print("\n After Insertion: \n")
ll.PrintLL()
ll.delete(4)
print("\n After Deletion: \n")
ll.PrintLL()
ll.insert_anywhere(4,3)
ll.insert_at_start(0)
print("\n After Addding at First \n")
ll.PrintLL()
ll.Reversal()
print("\n After Reversal: \n")
ll.PrintLL()

