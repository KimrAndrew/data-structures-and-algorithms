from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Animal, Cat, Dog

def test_import():
    assert AnimalShelter()

def test_dog():
    assert Dog()

def test_cat():
    assert Cat()

def test_animal():
    assert Animal()

def test_dog_is_animal():
    dog = Dog()
    assert isinstance(dog,Animal)

def test_cat_is_animal():
    cat = Cat()
    assert isinstance(cat,Animal)

def test_enqueue_to_empty():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    dq = shelter.line.dequeue()
    assert isinstance(dq,Cat)