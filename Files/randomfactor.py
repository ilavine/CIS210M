"""
Program Name:   Random number generator and factor program


Written by:      Iuliia Lavine


Date:           13 September 2020


Synopsis:      This program will generate 10 random numbers from 0 to 1000000.
               Then it will find numbers that are divisible by 3. 
                
"""

#import
from random import randint
#def
#First we need to generate 10 random numbers 

def numberList():
    numberList = [randint(0, 1000000) for i in range(0, 10)]
    return numberList

#Then we find random numbers that are divisible by 3

def getMessage1(parm):
    message = "This number parm1 is divisible by 3."
    message = message.replace("parm1", str(parm))
    return message

def getMessage2(parm):
    message = "This number parm1 is not divisible by 3."
    message = message.replace("parm1", str(parm))
    return message

#We apply divisibility rule by 3
def check3(parm1, line):
    total = 0
    for digit in str(i):
        total = total + int(digit)
#If the total of all digits contain more than 1 digit, repeat this process through a recursive call
    if total>=10:
        return check3(total)
    else:
        if total==3 or total==6 or total==9:
            return getMessage1(parm1)
        else:
            return getMessage2(parm1)


theList = numberList()
line = ""
for i in range(0, len(theList)):
    message = check3(theList[i], line)
    print(message)