import random

class PetShop:
     """ A pet shop"""

     def __init__(self, animal_factory =None):
          """pet_factoryis our abstract factory.
     	We can set it at will."""

          self.pet_factory = animal_factory

     def show_pet(self):
          """Creats and shows a pet using the abstract factory"""
          pet = self.pet_factory.get_pet()
          print("This is lovely",pet)
          print("It says",pet.speak())
          print("It eats",self.pet_factory.get_food())


class Dog:
     def speak(self):
         return "woof"

     def __str__(self):
         return "Dog"

class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"

class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()


if __name__ == "__main__":
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)
