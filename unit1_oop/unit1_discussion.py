"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Entity:

    active = True

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def announce_self(self):
        print(f"Hello, I am {self.name}!")
        print(f"I am at {self.location}.")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Monster(Entity):

    color = "Brown"

    def __init__(self, name: str, location: str, height: float, weight: float):
        super().__init__(name, location)

        if (height >= 0):
            self.height = height
        else:
            self.height = 0

        if (height >= 0):
            self.weight = weight
        else:
            self.weight = 0

    def announce_self(self):
        super().announce_self()
        print(f"I am {self.height}cm and {self.weight}kg.")
        print(f"I am also a Monster!")

    def change_location(self, location: str):
        old_location = self.location
        self.location = location
        print(f"Location of {self.name} changed from {old_location} to {self.location}!")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():

    print(f"__CREATING TWO INSTANCES OF THE SAME OBJECT TYPE__")
    monster_a = Monster("Henry", "Ugly Dungeon", 30.4, 12.8)
    monster_a.announce_self()

    monster_b = Monster("Crunchy", "Pretty Palace", 23.2, 10.2)
    monster_b.announce_self()

    print("\n=== Namespace Demonstration ===")

    print(f"-Accessing class variable through class itself-")
    print(f"{monster_a.name} is {Monster.color}")
    print(f"{monster_b.name} is also {Monster.color}")

    print(f"-Modifying class variable through class itself-")
    print(f"Changing Monster.color from Brown to Pink")
    Monster.color = "Pink"
    print(f"{monster_a.name} is {Monster.color}")
    print(f"{monster_b.name} is also {Monster.color}")

    print(f"-Accessing class variable through object instance-")
    print(f"{monster_a.name} is {monster_a.color}")
    print(f"{monster_b.name} is also {monster_b.color}")

    print(f"-Modifying class variable through class itself-")
    print(f"Changing monster_b.color (monster_b is {monster_b.name}) from Pink to Yellow")
    monster_b.color = "Yellow"
    print(f"{monster_a.name} is {monster_a.color}")
    print(f"{monster_b.name} is {monster_b.color}")

    print(f"-Adding new attribute 'royalty' to an instance-")
    monster_b.royalty = "King"
    print(f"Did I mention {monster_b.name} is a {monster_b.royalty}!?")

    print(f"-Displaying object namespaces-")
    print(f"{monster_a.name}'s namespace: {monster_a.__dict__}")
    print(f"{monster_b.name}'s namespace: {monster_b.__dict__}")

    print(f"-Displaying class namespace-")
    print(f"The Monster namespace: {Monster.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():

    # Original to be copied
    original = [[1,2],[3,4],[5,6]]

    # Shallow copy of original
    # Is a copy of the references at a high level in the original at the time of copying
    shallow_copy = original.copy()

    # Deep copy of original
    # Is a separate copy of the references at a deeper level at the time of copying
    deep_copy = deepcopy(original)

    print("\n=== Copy Demonstration ===")

    print(f"Before any changes:")
    print(f"Original: {original}")
    print(f"Shallow Copy:{shallow_copy}")
    print(f"Deep Copy:{deep_copy}")

    original[0] = [7,8]

    # Since this is changing a shallow object being referenced in original, only
    # original should change
    print(f"After changing high level array 'original[0] = [7,8]'")
    print(f"Original: {original}")
    print(f"Shallow Copy:{shallow_copy}")
    print(f"Deep Copy:{deep_copy}")

    original[1][0] = 9

    # Since this is changing a deep object being referenced in original, both
    # original and shallow should change
    # Shallow and original are both referencing the same object containing [3,4],
    # and when one of those values get changed to 9, both collections will reflect
    # that change
    # Deep has unique references to separate objects on both the shallow and low level,
    # so the references it is using are unchanged
    print(f"After changing value in low level array 'original[1][0] = 9'")
    print(f"Original: {original}")
    print(f"Shallow Copy:{shallow_copy}")
    print(f"Deep Copy:{deep_copy}")



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print(f"-Entity (The 'Parent Class' Demonstration-")
    e = Entity("Georgie", "Home")
    print(f"Entitie's 'announce_self' method")
    e.announce_self()

    print(f"-Monster (The 'Child Class' Demonstration-")
    c = Monster("Snoozie", "Salad Land", 345.2, 78.9)
    print(f"Monster's 'announce_self' method")
    c.announce_self()
    print(f"Monster's extra method 'change_location' method")
    c.change_location("Smelly Woods")
    c.announce_self()

    print(f"")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()