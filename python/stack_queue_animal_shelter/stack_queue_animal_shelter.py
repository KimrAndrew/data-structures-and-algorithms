from stack_and_queue.stack_and_queue import Node, Stack, Queue

class Animal():
    pass

class Dog(Animal):
    def __str__(self):
        return 'Dog'

class Cat(Animal):
    def __str__(self):
        return 'Cat'

class PlaceHolder():
    def __str__(self):
        return "PlaceHolder"

class AnimalShelter():
    
    def __init__(self):
        self.line = Queue()
        
    def enqueue(self,value):
        self.line.enqueue(value)
    
    # Need to ask what to return if pref not in queue
    # Need to ask how to handle if called on empty AnimalShelter
    def dequeue(self,pref=None):

        self.enqueue(PlaceHolder())

        if pref == "cat":
            if not self.line.is_empty():
                dq = self.line.dequeue()
                while not isinstance(dq, Cat) and not isinstance(dq,PlaceHolder):
                    self.line.enqueue(dq)
                    dq = self.line.dequeue()
                if  not isinstance(dq,PlaceHolder):
                    # get rid of PlaceHolder
                    current = self.line.dequeue()
                    # cycle back to and remove PlaceHolder
                    while not isinstance(current,PlaceHolder):
                        self.line.enqueue(current)
                        current = self.line.dequeue()
                return dq
            return None

        elif pref == "dog":
            if not self.line.is_empty():
                dq = self.line.dequeue()
                while not isinstance(dq, Dog) and not isinstance(dq,PlaceHolder):
                    self.line.enqueue(dq)
                    dq = self.line.dequeue()
                    self.line.enqueue(dq)
                if  not isinstance(dq,PlaceHolder):
                    # get rid of PlaceHolder
                    current = self.line.dequeue()
                    # cycle back to and remove PlaceHolder
                    while not isinstance(current,PlaceHolder):
                        self.line.enqueue(current)
                        current = self.line.dequeue()
                return dq
            return None
        else:
            return None
            


