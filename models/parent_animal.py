class Animal:
  def __init__(self, legs, age, diet):
    self.legs = legs
    self.age = age
    self.diet = diet

  def eats(self):
    print(f"Animal has a {self.diet} diet")

  def speak(self, noise):
    print(noise)
