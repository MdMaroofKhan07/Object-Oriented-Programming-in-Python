class Shark:

    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print("This shark has " + str(followers) + " followers")

def main():
    # First object, set up instance variables of constructor method
    sammy = Shark("Sammy", 5)
 
    print(sammy.name) # Print out instance variable name
 
    print(sammy.location) # Print out class variable location
 
    stevie = Shark("Stevie", 8) # Second object
 
    print(stevie.name) # Print out instance variable name
    # Use set_followers method and pass followers instance variable
    stevie.set_followers(77)
 
    print(stevie.animal_type) # Print out class variable animal_type

if __name__ == "__main__":
  main()
