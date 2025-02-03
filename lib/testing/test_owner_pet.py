from lib.owner_pet import Pet, Owner

def test_pet_creation():
    pet1 = Pet("Buddy", "dog")
    pet2 = Pet("Fluffy", "cat")
    
    # Check if the pets are created successfully
    assert pet1.name == "Buddy"
    assert pet2.pet_type == "cat"
    assert len(Pet.all) == 2

def test_invalid_pet_type():
    try:
        pet = Pet("Nibbles", "hamster")
    except Exception as e:
        assert str(e) == "hamster is not a valid pet type!"

def test_owner_creation():
    owner = Owner("Alice")
    assert owner.name == "Alice"
    assert len(owner.pets()) == 0

def test_add_pet_to_owner():
    owner = Owner("Alice")
    pet = Pet("Buddy", "dog")
    
    owner.add_pet(pet)
    assert len(owner.pets()) == 1
    assert owner.pets()[0].name == "Buddy"
    assert owner.pets()[0].owner == owner

def test_sorted_pets():
    owner = Owner("Alice")
    pet1 = Pet("Zoe", "dog")
    pet2 = Pet("Max", "dog")
    
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    
    sorted_pets = owner.get_sorted_pets()
    assert sorted_pets[0].name == "Max"
    assert sorted_pets[1].name == "Zoe"
