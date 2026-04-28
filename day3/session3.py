# Basic Function
def greet():
    print("Hello, World!")

greet()

# Function with Parameters
def greet(name):
    print("Hello", name)

greet("Ali")

# Return Values
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

#another example 
def calculate_discount(price):
    return price * 0.9

print(calculate_discount(100))

# ======================
# Scope (Local vs Global)
def test():
    x = 10
    print(x)

test()
# print(x) ❌ Error
x = 5

def show():
    print(x)

show()

# Modifying Global Variables
x = 5

def update():
    global x
    x = 10

# ======================
# Error Handling (Try/Except)

try:
    x = int("abc")
except:
    print("Error occurred")

# ======================
# Real-World Example
def login(username, password):
    if username == "admin" and password == "1234":
        return "Success"
    else:
        return "Fail"

try:
    user = input("Username: ")
    pwd = input("Password: ")
    print(login(user, pwd))
except Exception as e:
    print("Error:", e)