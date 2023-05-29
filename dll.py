class Node:
    def __init__(self,data:int):
        '''Creates Node, `Remainder: For Deletion No Need to Create a Node`'''
        self.data = data
        self.next = None
        self.prev = None
        
class DLL:
    def __init__(self):
        self.head = None
        

    def insert_at_start(self,some_data:int):
        '''This Function adds entered data at the start of the DoublyLinkedList.'''
        data = Node(some_data)
        current = self.head
        prev = None
        while current:
            if current.prev == None:
                temp = current
                self.head = data
                data.next = temp
                temp.prev = data
            return

    def insert_at_end(self,some_data:int):
        '''This function adds entered data at the End of the DoublyLinkedList.'''
        data = Node(some_data)
        current = self.head
        
        if self.head == None:
            self.head = data


        else:
            while current.next is not None:
                current = current.next
            current.next = data
            data.prev = current

        

    def insert_anywhere(self,some_value,pos:int):
        '''Will Insert the given value at required Position, FOLLOW INDEXING.'''
        data = Node(some_value)
        current = self.head
        count = 0
        prev=None
        if pos == 0: # Inserting at Start            
            self.head=data
            data.next=current
            current.prev=data

        else:
            while current is not None:
                if count !=pos:
                    count+=1
                    prev=current
                    current=current.next
                elif count==pos:
                    prev.next=data
                    data.next=current
                    current.prev=data
                    data.prev=prev
                    return
                 
    def delete_at_start(self):
        if self.head.prev == None:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
         
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None

    def delete_data(self,data:int):
        '''This Function deletes the desired element...'''
        current = self.head
    
        while current is not None:
            if current.data == data:
                if current.prev is None:
                    self.delete_at_start()
                elif current.next is None:
                    self.delete_at_end()
                else:
                        current.next.prev = current.prev
                        current.prev.next = current.next
           
            current = current.next    


    def TraverseDLL(self):
        '''This Function Prints all the elements in the Doubly LinkedList from both left to right and right to left...'''
        
        print("\nTraversing from Left to Right: \n")


        current = self.head
        while current:
            print(current.data)
            current = current.next
        
        print("\nTraversing from Right to Left: \n")

        temp = self.head

        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data)
            temp = temp.prev

        # current = self.head
        # prev = None
        # if data == self.head.data:
        #         # print(f"current.next.prev: {current.next.prev.data}")
        #         # print(f"current.next.prev.prev: {current.next.prev.prev}")
        #         # print(f"current.next.data: {current.next.data}")
        #         self.head = current.next
        #         current = current.next
        #         # print(f"self.head: {self.head.data}")
        #         # print(f"current.data: {current.data}")
        #         current.prev = None  
        # while current is not None:
        #     if  current.data == data:
        #         if prev is None:
        #             prev = current
        #             current.next.prev = None
        #         print(f"current.next.data: {current.next.data}")
        #         prev.next = current.next
        #         current.next = prev
        #         return
        #     prev = current
        #     current = current.next    



        # while current:   osthundi
        #     if current.data==data:
        #         if current.prev == None:
        #             self.head = current.next
        #             current.next.prev = None
        #         else:
        #             current.prev = current.next
        #             current.next.prev = current.prev
        #     else:
        #         current = current.next 
        
        
                 
        # prev = current.prev
        # print(f"Current.next.data : {current.next.data}")
        # print(f"Current.data: {current.data}")

        # while current is not None:
        #     # print(f"1st while is:{current.data}")
        #     if current.data==data:
        #         if current.prev is None:
        #             if current.next:
        #                 self.head = current.next
        #                 current.next.prev= None
        #         prev.next = current.next
        #         current.next.prev = prev.prev
        #         break         
            
        #     prev = current
        #     current = current.next
            
        # if current.prev is None:
        #     # Delete at Start
        #     # print(f"2nd while/if loop:{current.prev}")
        #         self.head = current.next
        #         current.next.prev = None 
        #         current = self.head
        #         break
                                                                 


dll = DLL()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(4)
dll.insert_anywhere(3,2)
dll.insert_at_start(0)
dll.delete_at_start()
dll.delete_at_end()
dll.TraverseDLL()
dll.delete_data(3)
print("\n")
dll.TraverseDLL()



