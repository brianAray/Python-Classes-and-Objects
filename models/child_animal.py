from models import parent_animal

class Dog(parent_animal.Animal):
  def __init__(self, name, age, color, size, breed):
    super().__init__(4, age, "Omnivore")
    self.name = name
    self.color = color
    self.size = size
    self.breed = breed

  def speak(self, noise="Woof!"):
    print(noise)

  def eats(self):
    print("Implement me")

  def __repr__(self):
    return "Implement me"


# Implement these classes
    
class Cat(parent_animal.Animal):
  pass

class Monkey(parent_animal.Animal):
  pass

class Cow(parent_animal.Animal):
  pass
