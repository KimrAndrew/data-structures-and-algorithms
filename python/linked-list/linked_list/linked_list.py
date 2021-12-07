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
        current = self.head
        if current.data == value:
            insert = Node(new_value,current)
            self.head = insert
            return
        while current is not None:
            if current.next.data == value:
                insert = Node(new_value,current.next)
                current.next = insert
                return
            current = current.next
        return
    
    def __str__(self) -> str:
        s = ''
        current = self.head
        while not current is None:
            s += f'{{{current.data}}} -> '
            current = current.next
        s += 'NONE'
        return s
