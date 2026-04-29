# Read File
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# 📌 Read Line by Line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
# ======================

with open("output.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Python File I/O")

# Append Data
with open("output.txt", "a") as file:
    file.write("\nNew Line Added")
  
