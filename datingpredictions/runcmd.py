# Import modules
import os
import subprocess


# Actual code Pog
#run = "python app.py"# Will run python script
#path = "C:\\Users\\bruh\\Desktop\\VSC\\Python"# Search for the script

# file searching func

def find_files(filename, search_path):
     result = []

    # Will search for the file itself

     for root, dir, files in os.walk(search_path): 
      if filename in files:
           result.append(os.path.join(root, filename))
     return result
     #os.chdir(result) 
     

# Found file
find_files("app.py","C:")
print("Running Dating Prediction by AmirulPants")
os.system('cmd /k "python app.py"')
    
