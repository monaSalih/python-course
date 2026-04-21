# download python from https://www.python.org/downloads/
# choose Download Python install manager
# answer all qwestions on cmd with y but double cheack the question

name = "Ali" # string
age = 25 # integer
price = 19.99 # float
is_active = True # boolean

age_str = str(25)
number = int("10")

#+  -  *  /  %
# ==  #equal to
# !=  #not equal to
# > #greater than
#  < #less than
#   >=  #greater than or equal to
# <= #less than or equal to


# if condition:
#     # code
# elif condition:
#     # code
# else:
#     # code


age = 20

if age >= 18:
    print("Adult")
else:
 print("Minor")



count = 0

while count < 5:
    print(count)
    count += 1

for i in range(5):
    print(i)

names = ["Ali", "Sara", "John"]

for name in names:
    print(name)

for i in range(5):
    if i == 3:
        break

for i in range(5):
    if i == 2:
        continue

# Combining Conditionals + Loops
numbers = [10, 15, 20, 25]

for n in numbers:
    if n % 2 == 0:
        print(n, "Even")
    else:
        print(n, "Odd")