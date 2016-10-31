import os

class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"

class Human(object):
    def __init__(self):
        self.name = "Humman"

    def speak(self):
        return "'hello'"

class Car(object):
    def __init__(self):
        self.name ="Car"

    def make_noise(self, octane_level):
        return "vroom%s" % ("!" *octane_level)

class Adpater(object):
    """
    Adapats an object by replacing methods:
    Usage:
    Dog = Dog
    dog = Adapter(dog, dict(make_noise =dog.bark))
    """
    def __init__(self,obj,adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All no-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

def main():
    objects = []
    dog = Dog()
    objects.append(Adpater(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adpater(cat, dict(make_noise=cat.meow)))
    human=Human()
    objects.append(Adpater(human,dict(make_noise=human.speak)))
    car=Car()
    car_noise=lambda: car.make_noise(3)
    objects.append(Adpater(car,dict(make_noise=car_noise)))

    for obj in objects:
        print("A",obj.name, "goes", obj.make_noise())


if __name__ == "__main__":
    main()
