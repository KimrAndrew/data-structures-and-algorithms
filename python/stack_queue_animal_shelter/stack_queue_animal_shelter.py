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
