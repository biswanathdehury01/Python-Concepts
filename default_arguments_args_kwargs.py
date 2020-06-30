# Default Arguments 

def about(name, age, likes):
    print("{} is about {} years old and likes {}".format(name, age, likes))
    
about("ram", 23, "Football")

def about(name, age, likes="Vedio Games"):
    print("{} is about {} years old and likes {}".format(name, age, likes))
    
about("ram", 23)


def about(name , age = 28, likes="Vedio Games"):
    print("{} is about {} years old and likes {}".format(name, age, likes))
    
about("ram")
    
def about(name ="hari" , age = 28, likes="Vedio Games"):
    print("{} is about {} years old and likes {}".format(name, age, likes))
    
about()

# ========================================

# Packing and Un Packing using *args and **kwargs


numbers = [1,2,3,4,5]

print(*numbers)

print(*"abcdef")

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)

print(add(2,4,6,8))

dictionary = {"name":"Bibhu", "age": 28, "likes":"Football"}

# Implementing  **kwargs
# ===============================

about(**dictionary) 

def details(**kwargs):
    for key,value in kwargs.items():
        print("{} : {}".format(key,value))

print(details(**dictionary))

details(ram= 3, place="harda")
    

