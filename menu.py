from os import system
from modules import LOGO
from modules import main_LOGO
from modules import PRIMARY_COLOR_DEFINE
from modules import AVAILABLE_USER_SELECT
from rely import READ_HELP_DOUCUMENTS
from BDirectory import BDirectory
from Burp_Fuzz import Burp_Fuzz
#test
def MAIN_MENU():
    #system("cls")
    USER_SELECTION='UNDEFINED'
    while USER_SELECTION not in AVAILABLE_USER_SELECT:
        main_LOGO()
        print("#-- Dir8urp is an Penetration testing tool, Which uses for WEB Penetration test --#")
        print("#-- THIS TOOL IS DEVELOPED BY JeffyLapter, alazymechnaic, HC1024 , NothingH")
        print("#-- Any unauthorized attack is "+PRIMARY_COLOR_DEFINE.WRONG("ILLEGAL")+", and the developer of the program is not liable for any legal disputes arising therefrom. --#")
        print('#-- TYPE "HELP" TO CHECK OUT HOW TO USE THIS TOOL --#')
        try:
            USER_SELECTION=input() #USER`S SELECTION
        except Exception:
            exit(0)
        if AVAILABLE_USER_SELECT.get(USER_SELECTION) == 1:
            READ_HELP_DOUCUMENTS()
        elif AVAILABLE_USER_SELECT.get(USER_SELECTION) == 2:
            BDirectory()
        elif AVAILABLE_USER_SELECT.get(USER_SELECTION) == 3:
            Burp_Fuzz()
        elif USER_SELECTION == 'exit':
            exit(0)
        else:
            print("Maybe you can try to type 'HELP' for help\n")
        
while True:
    #system('cls')
    MAIN_MENU()
    
