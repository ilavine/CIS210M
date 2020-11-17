
"""
Program Name:   PostfixEvaluation.py
Writen by:     Iuliia Lavine
Date:          10 November 2020
Synopsis:      This program evaluates given Postfix notation using Queues. 
       
Helpful links: https://www.youtube.com/watch?v=XLXWidXVRJk
               https://www.youtube.com/watch?v=yTpzVWO1Dis
"""
from Queue import Queue


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
            [input(f'Input a number for variable {token}: ')\
                                for token in tokens if token.isalpha()]
    postflix = ' '.join(user_in + tokens[len(user_in):])
    return evaluate_postfix(postflix)



if __name__ == "__main__":
    print(evaluate_postfix("2 3 1 * + 9 -"))
    print(evaluate_postfix("1 2 4 * +"))
    print(evaluate_postfix("2 3 + 1 4 + *"))
    print(evaluate_postfix("4 5 + 3 *"))
    print(evaluate_postfix("4 2 3 * +"))
    print(evaluate_postfix("10 2 3 * -"))
    print(evaluate_postfix("10 2 - 3 *"))

    print(user_input_expression("a b d + -"))
