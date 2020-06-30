# While Loops

L = []

while len(L) < 5:
    New_Name = input("Enter Your Name: ").strip().capitalize()
    L.append(New_Name)
    
print("Sorry List is full")
print(L)

# For Loops

students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

