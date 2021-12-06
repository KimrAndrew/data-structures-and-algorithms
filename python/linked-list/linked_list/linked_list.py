class Node():
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next

class Linked_List():
    def __init__(self) -> None:
        self.head = None