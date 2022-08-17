# In order to apply Open Closed Principle accordingly, we have to change make_sound and fly method. 
# To achieve that goal we must overwrite the method behavior by implementing an interface in an animal class.

class IAnimal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class IAnimalSound:
  def make_sound(self):
    pass

class AnimalFlyBehavior:
  def fly(self):
    print("Fly!")

class Lion(IAnimal, IAnimalSound):
  def make_sound(self):
    print("Roar")

class Dog(IAnimal, IAnimalSound):
  def make_sound(self):
    print("Woof")

class Bird(IAnimal, IAnimalSound, AnimalFlyBehavior):
  def make_sound(self):
    print("Tweet")



bird = Bird("Bird", 5)
print(bird.__dict__)
bird.make_sound()
bird.fly()

dog = Dog("Dog", 5)
print(dog.__dict__)
dog.make_sound()

lion = Lion("Lion", 10)
print(lion.__dict__)
lion.make_sound()

# class IAnimalSound:
#   def execute(self):
#     pass

# class BirdSound(IAnimalSound):
#   def execute(self):
#     print("Tweet")

# class DogSound(IAnimalSound):
#   def execute(self):
#     print("Woof")

# class LionSound(IAnimalSound):
#   def execute(self):
#     print("Roar")
    
# class AnimalSound():
#   def __init__(self, name, sound: IAnimalSound):
#     self.name = name
#     self.sound = sound

#   def make_sound(self):
#     self.sound.execute(self)
#     return


# class IAnimalFlyBehavior():
#   def execute(self):
#     pass

# class BirdFlyBeahvior(IAnimalFlyBehavior):
#   def execute(self):
#     print("Fly")

# class DogFlyBeahvior(IAnimalFlyBehavior):
#   def execute(self):
#     print("Dog doesn't fly!")

# class LionFlyBeahvior(IAnimalFlyBehavior):
#   def execute(self):
#     print("Lion doesn't fly!")

# class AnimalFlyBehavior:
#   def __init__(self, flyBehavior: IAnimalFlyBehavior):
#     self.flyBehavior = flyBehavior

#   def fly(self):
#     self.flyBehavior.execute(self)


# class Animal:
#   name = ''
#   age = ''

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age


# bird = Animal("bird", "10")
# print(bird.__dict__)
# birdSound = AnimalSound(bird.name, BirdSound)
# birdSound.make_sound()
# birdFlyBehavior = AnimalFlyBehavior(BirdFlyBeahvior)
# birdFlyBehavior.fly()

# dog = Animal("dog", "10")
# print(dog.__dict__)
# dogSound = AnimalSound(dog.name, DogSound)
# dogSound.make_sound()
# dogFlyBehavior = AnimalFlyBehavior(DogFlyBeahvior)
# dogFlyBehavior.fly()

# lion = Animal("lion", "10")
# print(lion.__dict__)
# lionSound = AnimalSound(lion.name, LionSound)
# lionSound.make_sound()
# lionFlyBehavior = AnimalFlyBehavior(LionFlyBeahvior)
# lionFlyBehavior.fly()
