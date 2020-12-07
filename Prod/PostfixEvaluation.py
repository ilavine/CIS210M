
"""
Program Name:   PostfixEvaluation.py
Writen by:     Iuliia Lavine
Date:          10 November 2020
Synopsis:      This program evaluates given Postfix notation using Queues. 
       
Helpful links: https://www.youtube.com/watch?v=XLXWidXVRJk
               https://www.youtube.com/watch?v=yTpzVWO1Dis
"""
from Queue import Queue
import time

print('This program evaluates given Postfix notation using Queues.')
input('\nPress Enter To Start the Program\n')
operators = ['+', '-', '*', '/']
queue = Queue()

def evaluate_postfix(expression):
    
    for token in expression.split():
        if token not in operators:
            queue.enqueue(token)
        else:
            op2 = int(queue.dequeue())
            op1 = int(queue.dequeue())

            if token == '+':
                op = op1 + op2
            elif token == '-':
                op = op1 - op2
            elif token == '*':
                op = op1 * op2
            elif token == '/':
                op = op1 / op2

            queue.enqueue(op)
    return queue.dequeue()

def user_input_expression(expression):

    tokens = expression.split()
    user_in =\
            [input(f'\n   Now input a number for variable {token}: ')\
                                for token in tokens if token.isalpha()]
    postflix = ' '.join(user_in + tokens[len(user_in):])
    print('\nCalculating...')
    time.sleep(1)
    return evaluate_postfix(postflix)



if __name__ == "__main__":
    print('\nEvaluating given expressions...\n')
    time.sleep(3)
    print('1) 4 5 6 * + 9 - equals', evaluate_postfix("4 5 6 * + 9 -"))
    print('2) 2 3 * + equals', evaluate_postfix("1 2 3 * +"))
    print('3) 3 + 1 6 + * equals', evaluate_postfix("2 3 + 1 6 + *"))
    time.sleep(1)
    print('\nOutput:', user_input_expression("a b d + -"))
