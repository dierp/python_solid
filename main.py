class Animal:
  name = ''
  age = ''

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def make_sound(self):
    if(self.name == "lion"):
      print("Roar")
    elif(self.name == "dog"):
      print("Woof")
    elif(self.name == "bird"):
      print("Tweet")
    return

  def fly(self):
    if(self.name == "bird"):
      print("Fly!")
    else:
      print(f"{self.name} doesn't fly!")
    return

bird = Animal("bird", "10")
print(bird.__dict__)
bird.make_sound()
bird.fly()

dog = Animal("dog", "10")
print(dog.__dict__)
dog.make_sound()
dog.fly()

lion = Animal("lion", "10")
print(lion.__dict__)
lion.make_sound()
lion.fly()