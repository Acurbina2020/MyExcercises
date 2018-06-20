planets = {
"Earth": "Class M",
"Mars": "Class K",
"Venus": "Class N",
"Vulcan": "Class M",
"Qo'noS": "Class M",
"Mercury": "Class B",
"Jupiter": "Class J",
"Saturn": "Class J",
"Uranus": "Gas Giant",
"Neptune": "Gas Giant",
"Pluto": "Class C"
}

def SpaceCowboy():
    user_input = input("Welcome, Space Cowboy! Are you ready to explore the universe?...the Star Trek style, of course! (Yes!/Nah)\n")
    if user_input == "Yes!":
        Planets(),
    if user_input == "Nah":
        pass;

def Planets():
    user_input = input("Find out the class of your planet. Write a name here:\n")
    if user_input in planets:
        print (planets[user_input]),
    if user_input in planets and planets[user_input] == "Class M" and user_input != "Earth":
        print ((planets[user_input]) and "Same as our Earth!"),
    if user_input in planets and "Class" not in planets[user_input]:
        print ("Undetermined Class"),
    if user_input not in planets:
        print ("Please write the name of a planet (Example: 'Earth')")
        Planets()
