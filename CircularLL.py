class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CSLL:
    def __init__(self):
        self.head = None

    def insert_at_start(self,some_data:int)-> None: 
        '''This function inserts data at the Start of the Circular Linked List.'''
        data = Node(some_data)
        current = self.head

        if not self.head:
            self.head = data
            data.next = self.head # type: ignore
        else:
            while current.next is not self.head:
                current = current.next
            current.next = data
            data.next = self.head
            self.head = data                
        return

    def insert_at_end(self,some_data:int) -> None:
        '''This Function inserts data at the End of the Circular Linked List.'''
        data = Node(some_data)
        current = self.head

        if not self.head:
            self.head = data
            data.next = self.head
        else: 
            while current.next is not self.head:
                current = current.next
            current.next = data
            data.next = self.head
        return

    
    def insert_at_pos(self, data: int, pos: int) -> None:
        
        '''This function inserts data at the specified position in the Circular Linked List.'''
        data = Node(data)
        current = self.head
        count = 0
        prev = None

        if not self.head:  
            self.head = data
            data.next = self.head
            return

        if pos == 0:  
            self.insert_at_start(data)
            return

        while count < pos:
            prev = current
            current = current.next
            count += 1
            if current == self.head:  
                print("There is NO such POSITION!")
                return False

        prev.next = data
        data.next = current

        return

    def TraverseCLL(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
            if current.next == self.head:
                break
        return
    
    # def insert_at_pos(self,data:int,pos:int) -> None:
    #     data = Node(data)
    #     current = self.head
    #     count = 0
    #     prev = None
    #     if not self.head:
    #         current = data
    #         data.next = self.head
    #         return
    #     if pos == 0:
    #         self.insert_at_start(data)
    #     while current is not None:
    #         count = count + 1
    #         if count == pos:
    #             data.next = current
    #             prev.next = data
    #             return
    #         prev = current
    #         current = current.next
    #     if pos > count:
    #         print("There is NO such POSITION!")
    #         return False
    #     self.head = current
    #     return
    def delete_at_start(self):
        pass
        