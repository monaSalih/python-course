# Classes & Objects
class Person:
    pass
# 🧪 Create Object
p1 = Person()
print(p1)

# ======================
# Attributes & Constructor
# 🧠 __init__ Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ali", 25)
print(p1.name)
# ======================
# 🧩 What is a Method?
# A function inside a class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p1 = Person("Sara")
p1.greet()
# ======================
# Example with Logic
class Student:
    def __init__(self, score):
        self.score = score

    def is_passed(self):
        return self.score >= 50
    
# ======================
# Encapsulation (Basic Idea)
# Keep data inside objects
# Control access via methods
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# ======================
# Inheritance
# Child class inherits from parent
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def bark(self):
        print("Woof")

d = Dog()
d.speak()  # inherited
d.bark()

# ======================
# Method Overriding
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Real-World Example
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self):
        return self.price * 0.9

p = Product("Laptop", 1000)
print(p.discount())
# ======================
