'''
Project Name:  Final CIS 210 M
Program Name:  Driver_v2.0.py
Date:          10 November 2020
Synopsis:      This is a driver program
Written by:    Iuliia lavine
'''
import Setup as sp
import FileReader as fr
import os 
import sys
import time

class Menu:
    #Display a menu and respond to choices when run
    def __init__(self):
        
        self.choices = {
                'W': self.welcome,
                '11': self.info,
                'Y': self.main_menu,
                'Z': self.exit,
                '1': self.bubble, 
                '2': self.factor, 
                '3': self.list, 
                '4': self.postfix, 
                '5': self.prime, 
                '6': self.queue, 
                '7': self.array, 
                '8': self.stack, 
                '9': self.sieve, 
                '10': self.timer   
                }
        
    
    def run(self):
        self.welcome()
        #Display the menu and respond to choices
        while True:
            choice = input(">>> ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
   

    def welcome(self):
        return fr.readFile(sp.getWelcome())  

    def main_menu(self):
        os.system('cls')
        return fr.readFile(sp.getMainMenu())
           
    def info(self):
        os.system('cls')
        return fr.readFile(sp.getInfo())

    def bubble(self):
        os.system('cls')
        exec(open("bubblesort.py").read(), globals())
        print("\nPress Y To Return To Main Menu")

    def list(self):
        os.system('cls')
        exec(open("lists.py").read(), globals())
        print("\nPress Y To Return To Main Menu")
   
    def factor(self):
        os.system('cls')
        exec(open("factorprogram.py").read(), globals())
        print("\nPress Y To Return To Main Menu")

    def postfix(self):
        os.system('cls')
        exec(open("PostfixEvaluation.py").read(), globals())
        print("\nPress Y To Return To Main Menu")

    def prime(self):
        os.system('cls')
        exec(open('prime_numbers.py').read(), globals())
        print("\nPress Y To Return To Main Menu")

    def queue(self):
        os.system('cls')
        exec(open('QueueProgram.py').read(), globals())
        print("\nPress Y To Return To Main Menu")
    
    def array(self):
        os.system('cls')
        exec(open('randomarray.py').read(), globals())
        print("\nPress Y To Return To Main Menu")

    def stack(self):
        os.system('cls')
        exec(open('StackProgram.py').read(), globals())
        print("\nPress Y To Return To Main Menu")

    def sieve(self):
        os.system('cls')
        exec(open('sieve.py').read(), globals())
        print("\nPress Y To Return To Main Menu")

    def timer(self):
        os.system('cls')
        exec(open('timer.py').read(), globals())
        print("\nPress Y To Return To Main Menu")

    def exitScrn(self):
        return fr.readFile(sp.getExit())
        
    def exit(self):
        os.system('cls')
        self.exitScrn()
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
