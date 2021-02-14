# First  focus we're gonna put on is SOLID "S", single responsability principle. 
# This principle says that a class should have only one reason to be changed.
# In the main.py file we had a Animal class with two methods, make_sound and fly. 
# Hence, that class have two reasons to change, wich is the opposite of SRP.
# Bellow we have an example of how to apply SRP accordingly

class AnimalSound:
  name = ''

  def __init__(self, name):
    self.name = name

  def make_sound(self):
    if(self.name == "lion"):
      print("Roar")
    elif(self.name == "dog"):
      print("Woof")
    elif(self.name == "bird"):
      print("Tweet")
    return

class AnimalFlyBehavior:
  name = ''

  def __init__(self, name):
    self.name = name

  def fly(self):
    if(self.name == "bird"):
      print("Fly!")
    else:
      print(f"{self.name} doesn't fly!")


class Animal:
  name = ''
  age = ''

  def __init__(self, name, age):
    self.name = name
    self.age = age


bird = Animal("bird", "10")
print(bird.__dict__)
birdSound = AnimalSound(bird.name)
birdSound.make_sound()
birdFlyBehavior = AnimalFlyBehavior(bird.name)
birdFlyBehavior.fly()

dog = Animal("dog", "10")
print(dog.__dict__)
dogSound = AnimalSound(dog.name)
dogSound.make_sound()
dogFlyBehavior = AnimalFlyBehavior(dog.name)
dogFlyBehavior.fly()

lion = Animal("lion", "10")
print(lion.__dict__)
lionSound = AnimalSound(lion.name)
lionSound.make_sound()
lionFlyBehavior = AnimalFlyBehavior(lion.name)
lionFlyBehavior.fly()