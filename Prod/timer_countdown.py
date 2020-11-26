"""
Program Name:   Random number generator


Writen by:      Iuliia Lavine


Date:           13 September 2020


Synopsis:      This program generates random numbers from 0 to 1000000 
"""


#import
import random 

#This fundtion will generate 100000 random numbers

def random_list():
    list = [random.randint(0,1000000) for _ in range(1000000)]
    return list

list = random_list()
print(list)


#imports data to a text file 
#file directory needs to be changed upon execution 

with open(r'C:\Users\iulii\Desktop\Python\output.txt', 'a')as f:
    f.write(str(list))
