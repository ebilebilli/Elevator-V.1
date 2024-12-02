import os
import platform

def clear_screen():
    system_name = platform.system().lower()
        
    if system_name == "windows":
        os.system("cls")  
    else:
        os.system("clear")  