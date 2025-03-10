class Dog:
    def makeSound(self):
        return "Woof!"

class Cat:
    def makeSound(self):
        return "Meow"

def processSound(sound_object):
    print(sound_object.makeSound())

dog = Dog()
cat = Cat()

processSound(dog)
processSound(cat)
