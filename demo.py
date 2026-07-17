class Animal:
    def __init__(self, name, reg_no):
        self.name = name

    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog("Buddy", "123")
print(my_dog.speak())
           


        