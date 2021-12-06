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
        while not current is None:
            if current.data == search:
                return True
            current = current.next
        return False
    
    def __str__(self) -> str:
        s = ''
        current = self.head
        while not current is None:
            s += f'{{{current.data}}} -> '
            current = current.next
        s += 'NONE'
        return s
