# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Not there")

# child classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

    
dog = Dog("Buddy")
cat = Cat("Whiskers")

    
print(dog.speak())
print(cat.speak())