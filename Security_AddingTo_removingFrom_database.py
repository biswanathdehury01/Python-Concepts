# Security Adding 

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("My name is Travis!")
    name = input("What's your name?: ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed from the system(y/n)?: ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
            
        elif remove == "n":
            print("I don't want you to leave anyway!")
            
    else:
        print("I dont think i have met you yet {}".format(name))
        add_me = input("Would you like to be added into the system(y/n)?: ").strip().lower()
        
        if add_me == "y":
            known_users.append(name)
            
        elif add_me == "n":
            print("No worries! See you again :)")
            
            