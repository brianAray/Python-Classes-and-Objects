from models import child_animals

# Function to display thea available animals
def available_animals(animals):
  for animal in animals:
    print(animal)
  print("\n")


# Function to create a chosen Animal
# Finsih this implementation
def create_animal(animals):
  user_choice = input("Choose animal\n")
  if user_choice in animals:
    if user_choice == "Dog":
      return child_animals.Dog(input("Name: "), input("Age: "), input("Color: "), input("Size: "), input("Breed: "))


# An example of a created object
dog1 = child_animals.Dog("Spot", 3, "Brown", "Medium", "Retriever")

# Put animals inside this list that are to be displayed
animals = ["Dog", "Cat", "Monkey", "Cow"]


available_animals(animals)
print(create_animal(animals))
