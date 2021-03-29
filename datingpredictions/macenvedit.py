# Dating Prediction

# Import some mods

import random

# Variables
invalid_name = True
persona = False 
boy = {
    "name" : "",
    "age" : "",
    "personality" : ["neuroticism", "openness", "agreeableness", "extraversion", "conscientiousness"],
    "gender" : ""
}

girl = {
    "name" : "",
    "age" : "",
    "personality" : ["neuroticism", "openness", "agreeableness", "extraversion", "conscientiousness"],
    "gender" : ""
}
# percentage = random.randint(1,100)
                   # depressed     # adventurer  # introvert     # extrovert     # self-dicipline
personalityTraits = ["neuroticism", "openness", "agreeableness", "extraversion", "conscientiousness"]
userInputsBoy = {"name" : boy["name"],"age": boy["age"],"personality": boy["personality"]}
userInputsGirl = {"name" : girl["name"],"age": girl["age"],"personality": girl["personality"]}

# Questions to fill up the module

usergender = raw_input("What is your gender?\n")# User put in their gender
if usergender == "boy":
    boy["gender"] = usergender
    userInputsBoy["name"] = raw_input("What is your name?\n")# Asks for user's name
    userInputsBoy["age"] = int(raw_input("What is your age, " + userInputsBoy["name"] + "?\n"))# Asks for user's age
    print(personalityTraits)# Print variable (Seek line 9)
    userInputsBoy["personality"] = raw_input("What is your personality, " + userInputsBoy["name"] + "?\n")# Asks for the user's personality
else:
    girl["gender"] = usergender
    userInputsGirl["name"] = raw_input("What is your name?\n")
    userInputsGirl["age"] = int(raw_input("What is your age, " + userInputsGirl["name"] + "?\n"))
    print(personalityTraits)
    userInputsGirl["personality"] = raw_input("What is your personality, " + userInputsGirl["name"] + "?\n")   

if usergender == "boy":
   userInputsGirl["name"] = raw_input("What is the name of the girl?\n")# Asks for the crush's name
   userInputsGirl["age"] = int(input("What is "+ userInputsGirl["name"] + "'s age?\n"))# Asks for crush's age
   print(personalityTraits)
   userInputsGirl["personality"] = raw_input("What do you think "+ userInputsGirl["name"] + "'s personality?\n")# Asks for crush's personality
else:
    userInputsBoy["name"] = raw_input("What is the name of the boy?\n")
    userInputsBoy["age"] = int(raw_input("What is "+ userInputsBoy["name"] + " age?\n"))
    print(personalityTraits)
    userInputsBoy["personality"] = raw_input("What do you think is " + userInputsBoy["name"] + "'s personality?\n")

# Prediction Results 
   
# Good prediction
    
if userInputsBoy["personality"] == "neuroticism" or "agreeableness" and userInputsGirl["personality"] == "neuroticism" or "agreeableness":
 if userInputsBoy["age"] == userInputsGirl["age"]:
   print("You will have a chance to be with her/him. Take the chance when you see it. :)")
 else:
   print('Dude, your age man, weirdo.') 
    
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

#if userInputsBoy["age"] == userInputsGirl["age"]:
  #print("pagchamp")

#elif userInputsBoy["age"] <> userInputsGirl["age"]:
  #print("linusWeirdChamp")

#print("You can now exit the program") 


                            
   
# twitter.com/amirulplays
# instagram.com/amirulpants



