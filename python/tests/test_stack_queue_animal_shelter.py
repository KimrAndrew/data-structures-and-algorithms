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

def test_enqueue_to_nonempty():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    assert isinstance(shelter.line.dequeue(),Cat)
    assert isinstance(shelter.line.dequeue(),Dog)

def test_dequeue_first_cat():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    assert isinstance(shelter.dequeue('cat'),Cat)
    shelter.line.dequeue()
    shelter.line.dequeue()
    assert shelter.line.is_empty()

def test_dequeue_not_first_cat():
    shelter = AnimalShelter()
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    assert isinstance(shelter.dequeue('cat'),Cat)
    shelter.line.dequeue()
    shelter.line.dequeue()
    shelter.line.dequeue()
    assert shelter.line.is_empty()