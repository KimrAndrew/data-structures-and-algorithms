class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def get(self,key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def add(self,key,value):
        current = self.head
        if current is None:
            self.head = Node(key,value)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(key,value)


class HashTable():
    def __init__(self):
        self.storage = [None] * 1024

    def hash(self,key):
        num = 0

        # sum ASCII values
        for char in key:
            num += ord(char)

        # multiply by a prime number
        num *= 599

        # modulo length of storage array
        num = num % 1024

        return num

    def add(self, key:str, value):
        index = self.hash(key)
        if self.storage[index] is None:
            self.storage[index] = LinkedList()
        node_at_key = self.storage[index].get('key')
        # Check if key already exists
        # TODO: make this bit work ¯\_(ツ)_/¯
        if node_at_key is not None:
            node_at_key.value = value
            return
        self.storage[index].add(key,value)

    def get(self,key:str):
        index = self.hash(key)
        if self.storage[index] is None:
            raise ValueError('Key Does Not Exist')
        return self.storage[index].get(key)