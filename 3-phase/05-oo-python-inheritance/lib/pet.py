#!/usr/bin/env python3
import ipdb

class Pet:

    all_pets = []

    def __init__(self,name, age, breed, temperament, is_cool=True):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.is_cool = is_cool
        Pet.add_pet(self)
 
    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    def print_self(self):
        print(self)

    # ! CLASS METHODS
    @classmethod
    def test_class_method(cls):
        print(cls == Pet)

    @classmethod
    def add_pet(cls, new_pet):
        cls.all_pets.append(new_pet)

    @classmethod
    def count_pets(cls):
        return len(Pet.all_pets)
    
    @classmethod
    def print_all_pets(cls):
        for pet in cls.all_pets:
            pet.print_pet_details()

    @classmethod
    def total_age(cls):
        age_list = [pet.age for pet in cls.all_pets]
        return sum(age_list)
    
    @classmethod
    def average_age(cls):
        return cls.total_age() / cls.count_pets()
    
    @classmethod
    def show_certain_breed(cls, search_breed):
        # return [ pet for pet in cls.all_pets if pet.breed == search_breed ]
        matching = []
        for pet in cls.all_pets:
            if pet.breed == search_breed:
                matching.append(pet)
        return matching
        
        


    