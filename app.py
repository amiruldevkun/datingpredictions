# Dating Prediction

# Import some mods

import random
import mods.module1

# Variables
invalid_name = True
persona = False 

# percentage = random.randint(1,100)
                   # depressed     # adventurer  # introvert     # extrovert     # self-dicipline
personalityTraits = ["neuroticism", "openness", "agreeableness", "extraversion", "conscientiousness"]
userInputsBoy = {"name" : mods.module1.boy["name"],"age": mods.module1.boy["age"],"personality": mods.module1.boy["personality"]}
userInputsGirl = {"name" : mods.module1.girl["name"],"age": mods.module1.girl["age"],"personality": mods.module1.girl["personality"]}

# Questions to fill up the module

usergender = input("What is your gender?\n")# User put in their gender
if usergender == "boy":
    mods.module1.boy["gender"] = usergender
    userInputsBoy["name"] = input("What is your name?\n")# Asks for user's name
    userInputsBoy["age"] = int(input("What is your age, " + userInputsBoy["name"] + "?\n"))# Asks for user's age
    print(personalityTraits)# Print variable (Seek line 9)
    userInputsBoy["personality"] = input("What is your personality, " + userInputsBoy["name"] + "?\n")# Asks for the user's personality
else:
    mods.module1.girl["gender"] = usergender
    userInputsGirl["name"] = input("What is your name?\n")
    userInputsGirl["age"] = int(input("What is your age, " + userInputsGirl["name"] + "?\n"))
    print(personalityTraits)
    userInputsGirl["personality"] = input("What is your personality, " + userInputsGirl["name"] + "?\n")
    
crushgender = input("What is your crush's gender?\n")

if crushgender == "boy":
   userInputsBoy["name"] = input("What is the name of the boy?\n")# Asks for the crush's name
   userInputsBoy["age"] = int(input("What is "+ userInputsBoy["name"] + "'s age?\n"))# Asks for crush's age
   print(personalityTraits)
   userInputsBoy["personality"] = input("What do you think "+ userInputsBoy["name"] + "'s personality?\n")# Asks for crush's personality
else:
    userInputsGirl["name"] = input("What is the name of the girl?\n")
    userInputsGirl["age"] = int(input("What is "+ userInputsGirl["name"] + " age?\n"))
    print(personalityTraits)
    userInputsGirl["personality"] = input("What do you think is " + userInputsGirl["name"] + "'s personality?\n")

# Prediction Results 
   
# Good prediction
    
if userInputsBoy["personality"] == "neuroticism" or "agreeableness" and userInputsGirl["personality"] == "neuroticism" or "agreeableness":
 persona = True
 
    
elif  userInputsBoy["personality"] == "openness" or "agreeableness" and userInputsGirl["personality"] == "openness" or "agreeableness":
 print("You will have a chance to be with her/him. Take the chance when you see it.")# Curious and introvert
    
elif userInputsBoy["personality"] == "openness" or "extraversion" and userInputsGirl["personality"] == "openness" or "extraversion":
 print("You will have a chance to be with her/him. Take the chance when you see it.")# Curious and extrovert
    
elif userInputsBoy["personality"] == "conscientiousness" or "agreeableness" and userInputsGirl["personality"] == "conscientiousness" or "agreeableness":
 print("You will have a chance to be with her/him. Take the chance when you see it.")# Self-diciplined and introvert
   
elif userInputsBoy["personality"] == "conscientiousness" or "extraversion" and userInputsGirl["personality"] == "conscientiousness" or "extraversion":
 print("You will have a chance to be with him/her. Take the chance when you see it.")# Self-diciplined and extrovert 

# Bad predictions        
    
elif userInputsBoy["personality"] == "neuroticism" or "extraversion" and userInputsGirl["personality"] == "neuroticism" or "extraversion":
 print("You still have a chance. But, its very slim.")# Depressed and extrovert
   
elif userInputsBoy["personality"] == "extraversion" or "agreeableness" and userInputsGirl["personality"] == "extraversion" or "agreeableness":
 print("You still have a chance. But, its very slim.")# Extrovert and introvert
   
elif userInputsBoy["personality"] == "openness" or "conscientiousness" and userInputsGirl["personality"] == "openness" or "conscientiousness":
 print("Yous still have a chance. But, its very slim.")# Curious and self-diciplined
    
elif userInputsBoy["personality"] == "conscientiousness" or "neuroticism" and userInputsGirl["personality"] == "conscientiousness" or "neuroticism":
 print("You still have a chance. But, its very slim.")# Self-diciplined and depressed 

# Age predictions (Work In Progress)

#if (12 < userInputsBoy["age"] < 17) and (12 < userInputsGirl["age"] < 17):
    #if persona == True:
     #print("PogU")

#if (12 < userInputsBoy["age"] < 22) and (12 < userInputsGirl["age"] < 22):
    #if persona == True:
        #print("WeirdChamp")
#print("You can now exit the program") 


                            
   
# twitter.com/amirulplays
# instagram.com/amirulpants



