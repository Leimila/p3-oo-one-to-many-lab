class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type!")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} is not a valid Pet instance!")
        pet.owner = self
        self.pets_list.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
