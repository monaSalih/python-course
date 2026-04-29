# def greet():
#     print("Hello, World!")  
# greet()

# def greet(name):#parameter
#     print ("hello",name)

# greet("Ali")#argument

# def add(a,b):
#     return a + b
# result = add(5,3)
# print ("result=",result)

#=================>
# def calcut_dis(price):
#    return price * 0.9#print || return
# print(calcut_dis(15))

# =================>
# def multi(a,b):
#     return a * b
# print (multi(4,77))

#=====================>
# Global vs local value

# def local_val():
#    a= 10
#    print(a)

# print(a) 
#=====================>
# a=10 #global value
# def Global_val():
#     print(a)
# a=5
# print(a)
#=====================>
#try and except
# try:
#     x=int("abc")
# except:
#     print("error occurred")

#=====================>
def login (username,password):
    if username == "admin" and password == "1234":#T and T => t
        return "success"
    else:
        return "failure"
    

try:
    banana= input("please enter your username: ")
    pas= input("please enter your password: ")
    print(login(banana,pas))
except Exception as e:
    print("An error occurred:", e)