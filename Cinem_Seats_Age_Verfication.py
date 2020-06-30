# Cinem_Seats_Age_Verfication (while, if-else, user input)

movies = {
        "Finding Nemo":[3,5],
        "Gully Boy":[15,4],
        "Sex and City":[18,2]
        }


while True:
    
    choice = input("Which film you would like to watch?: ").strip().title()
    
    if choice in movies:
        age = int(input("How old are you?").strip())
        
        # check Use age
        
        if age >= movies[choice][0]:
            
            # check for seats availability
            num_seats = movies[choice][1]
            
            if num_seats > 0:
                print("Enjoy the film...! :)")
                movies[choice][1] = movies[choice][1]-1
                
            else:
                print("Sorry... All seats are sold out for this movie")
        
        else:
            print("You are too young to see this movie!")
            
    else:
        print("We don't have that movie...")
                      
                    