"""
Program Name:    prime_numbers.py


Written by:      Iuliia Lavine


Date:           25 November 2020


Synopsis:      This program finds out whether a randomly generated number is prime
               by implementing a recursive function.
                
"""


from random import randint

def numberList():
    numberList = [randint(1, 100) for i in range(0, 10)]
    return numberList

def getMessage1(parm):
    message = "Number parm1 is prime."
    message = message.replace("parm1", str(parm))
    return message

def getMessage2(parm):
    message = "Number parm1 is not prime."
    message = message.replace("parm1", str(parm))
    return message

def isPrime(number, line): #recursive function to find prime numbers
	for i in list(range(2, number)):
		if number % i == 0:
			return getMessage2(number)
	return getMessage1(number)


theList = numberList()
line = ""
for i in range(0, len(theList)):
    message = isPrime(theList[i], line)
    print(message)