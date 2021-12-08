class Node():
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next

class Linked_List():
    def __init__(self) -> None:
        self.head = None

    def insert(self,data) -> None:
        self.head = Node(data,self.head)

    def contains(self,search) -> bool:  
        current = self.head
        while current is not None:
            if current.data == search:
                return True
            current = current.next
        return False

    def get_index(self,search_index):
        if type(search_index) is not int:
            raise TypeError("Search Index must be of type int")

        if search_index < -1:
            raise IndexError('Search Index must be a positive integer')

        current = self.head
        i = 0
        while i <= search_index:
            if current is None:
                raise IndexError('Index out of bounds')
            if i == search_index:
                return current.data
            current = current.next
            i += 1

    def insert_before(self,value,new_value):
        self.empty_head_raises_exception()
        current = self.head
        if current.data == value:
            insert = Node(new_value,current)
            self.head = insert
            return
        while current.next is not None:
            if current.next.data == value:
                insert = Node(new_value,current.next)
                current.next = insert
                return
            current = current.next
        raise ValueError("Value not found")

    def insert_after(self,value,new_value):
        self.empty_head_raises_exception
        current = self.head
        while current is not None:
            if current.data == value:
                insert = Node(new_value, current.next)
                current.next = insert
                return
            current = current.next
        raise ValueError("Value not found")

    def append(self, value):
        current = self.head
        if current is None:
            self.head = Node(value)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    
    def __str__(self) -> str:
        s = ''
        current = self.head
        while not current is None:
            s += f'{{{current.data}}} -> '
            current = current.next
        s += 'NONE'
        return s

    def kth_from_end(self,k):
        if k < 0:
            raise IndexError('k must be a positive int value')
        self.empty_head_raises_exception()
        output = self.head
        look_ahead = self.head
        for _ in range(0,k-1):
            look_ahead = look_ahead.next
            if look_ahead is None:
                raise IndexError("No kth from end index")
        while look_ahead.next is not None:
            output = output.next
            look_ahead = look_ahead.next
        return output.data
    
    def empty_head_raises_exception(self):
        if self.head == None:
            raise ValueError("Head empty")