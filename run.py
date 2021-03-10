# Import modules
import os
import subprocess

# Actual code Pog
run = "python app.py"# Will run python script
path = "C:\\Users\\bruh\\Desktop\\VSC\\Python"# Search for the script

# Open up windows cmd
def openCMD():
    os.chdir(path) 
    os.system(f'cmd /k {run}')   
openCMD()    
