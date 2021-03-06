from modulefinder import STORE_NAME
import re

class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def get(self,key):
        """
        Returns Node if key exists
        Returns None if key does not exist
        """
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

        #Raises key error if key already exists in hashmap
        if self.storage[index].get(key):
            raise KeyError(f'Value already stored at key:{key}')
        
        self.storage[index].add(key,value)

    def get(self,key:str):
        index = self.hash(key)
        if self.storage[index] is None:
            raise ValueError(f'Key Does Not Exist at key: {key}')
        return self.storage[index].get(key)

    def contains(self,key:str):
        index = self.hash(key)
        if self.storage[index] is None:
            return False
        if self.storage[index].get(key):
            return True
        return False

    def repeated_word(self,string:str):
        string = string.lower()
        # Get list of all words with punctuation stripped
        words = re.findall(r'[a-z]+',string)
        print(words)
        for word in words:
            try:
                self.add(word,word)
            except(KeyError):
                return word
        return ''

    def get_values(self):
        stored_values = []
        for bucket in range(len(self.storage)):
            if self.storage[bucket] is not None:
                current = self.storage[bucket].head
                while current is not None:
                    stored_value = [None,None]
                    stored_value[0] = current.key
                    stored_value[1] = current.value
                    stored_values.append(stored_value)
                    current = current.next
        return stored_values
