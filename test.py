# Dating Prediction

# Import some mods

import random
import mods.module1

# Variables
name = "What is your name?\n"

# percentage = random.randint(1,100)
                   # depressed     # adventurer  # introvert     # extrovert     # self-dicipline
personalityTraits = ["neuroticism", "openness", "agreeableness", "extraversion", "conscientiousness"]
userInputsBoy = {"name" : mods.module1.boy["name"],"age": mods.module1.boy["age"],"personality": mods.module1.boy["personality"]}
userInputsGirl = {"name" : mods.module1.girl["name"],"age": mods.module1.girl["age"],"personality": mods.module1.girl["personality"]}

# Questions to fill up the module

usergender = input("What is your gender?\n")# User put in their gender
if usergender == "boy":
    mods.module1.boy["gender"] = usergender
    userInputsBoy["name"] = input(name)# Asks for user's name
    while userInputsBoy["name"] == None:
        print("Oi! Ya still havent input your name yet!\n Please enter your name to continue.\n")
        print(name)
    else: 
        pass  