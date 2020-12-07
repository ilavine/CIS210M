"""
Program Name:   Stopwatch.py


Writen by:      Iuliia Lavine


Date:           07 September 2020


Synopsis:      This is a stopwatch program that is a timed loop.
               The loop initiates when a user presses 1. To exit the loop, 
               a user needs to press CTRL+C. The program will print the elapsed time. 
"""




import time

start = input('Press 1 to start timing. Exit the loop with CTRL+C:')

if start == '1':
    timer = True
    
    
sec = 0
min = 0

timer = start

try:
    while True:
        sec += 1
        print(str(min) + " minute(s) " + str(sec) + " second(s)")
        time.sleep(1)
        if sec == 60:
            sec = 0
            min += 1
            print(str(min) + " minute(s)" + str(sec) + " second(s)")
            
except KeyboardInterrupt:
    print('Timing has stopped at ' + str(min) + ' minutes ' + str(sec) + ' seconds')