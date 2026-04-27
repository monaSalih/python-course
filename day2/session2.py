# Lists
numbers = [10, 20, 30, 40]
names = ["Ali", "Sara", "John"]

print(numbers[0])   # 10
print(names[-1])    # John

# Modify List
numbers.append(50)
numbers.remove(20)
numbers[1] = 25

# Loop Through List
for n in numbers:
    print(n)


# Tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
print(coordinates[0])  # 10 Access

# Immutable => coordinates[0] = 50 ❌ Error

# Dictionaries (Key-Value Pairs)
user = {
    "name": "Ali",
    "age": 25,
    "is_active": True
}
# 🔍 Access Values
print(user["name"])

user["age"] = 26
user["email"] = "ali@mail.com"

# LOOP
for key, value in user.items():
    print(key, value)

# Sets (Unique & Unordered)
numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1,2,3,4}
# Operations
numbers.add(5)
numbers.remove(2)
# 🔁 Loop
for n in numbers:
    print(n)

# 🔄 Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)