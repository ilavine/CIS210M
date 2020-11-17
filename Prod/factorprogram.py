"""
Program Name:   Factor program


Writen by:      Iuliia Lavine


Date:           13 September 2020


Synopsis:      This program will pick numbers from a previously generated list 
               which are evenly divisible by 3.
                
"""
#def

def numberList():
    numberList = [875246, 464504, 765051, 829131, 771898, 160460, 19338, 120846, 829814, 386287]
    return numberList

#To find numbers that are evenly divisible by 3, divisibily rule by 3 is applied

def getMessage1(parm):
    message = "This number parm1 is divisible by 3."
    message = message.replace("parm1", str(parm))
    return message

def getMessage2(parm):
    message = "This number parm1 is not divisible by 3."
    message = message.replace("parm1", str(parm))
    return message

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
    
    