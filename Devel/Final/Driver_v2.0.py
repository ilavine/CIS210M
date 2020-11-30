'''
Project Name:  Final CIS 210 M
Program Name:  Driver_v2.0.py
Date:          10 November 2020
Synopsis:      This is to get screens
Written by:    Iuliia lavine
'''
import Setup as sp
import FileReader as fr
import os 
import sys

fr.readFile(sp.getWelcome())
os.system('cls')
    
class Menu:
    #Display a menu and respond to choices when run
    def __init__(self):
        
        self.choices = {
                "W": self.welcome,
                "Y": self.main_menu,
                "F": self.factor,
                "L": self.lists,
                "I": self.postfix,
                "Q": self.queue,
                "R": self.array,
                "T": self.timer,
                "Z": self.exit
                }
        
    def display(self): #this line will always display at the bottom of each screen
        print("""
Press Y To Proceed To Main Menu \n
Press Z To Exit The Application       
""")

        

    def run(self):
        #Display the menu and respond to choices
        while True:
            self.display()
            os.system('cls')
            choice = input("Make a selection: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                
    def welcome(self):
        return fr.readFile(sp.getWelcome())
        os.system('cls')

    def main_menu(self):
        
        return fr.readFile(sp.getMainMenu())
        os.system('cls')
         
    def factor(self):
        return fr.readFile(sp.getFactor())
        os.system('cls')

    def lists(self):
        return fr.readFile(sp.getLists())
        os.system('cls')

    def postfix(self):
        return fr.readFile(sp.getPostfix())
        os.syste,('cls')
    
    def queue(self):
        return fr.readFile(sp.getQueue())
        os.system('cls')
    
    def array(self):
        return fr.readFile(sp.getArray())
        os.system('cls')
    
    def timer(self):
        return fr.readFile(sp.getTimer())
        os.system('cls')

    def exit(self):
        print("Thank you and see you again soon!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
