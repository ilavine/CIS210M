"""
Program Name:  sieve.py
Writen by:     Iuliia Lavine
Date:          10 November 2020
Synopsis:      This is the implementation of Sieve_of_Eratosthenes

Helpful links: https://www.youtube.com/watch?v=pKvGYOnO9Ao

       
"""

from simple_stack import Stack
import random 

def sieve(n):
	for i in n:
		for j in n:
			if j != i and j%i == 0:
				n.remove(j)
	return n


def isPrime(numero):
	for i in range(2, numero):
		if numero % i == 0:
			return False
	return True

#testing the isPrime function

print ("Is Prime?\n")
print ('Is 2 a prime?', isPrime(2))
print ('Is 3 a prime?', isPrime(3))
print ('Is 4 a prime?', isPrime(4))
print ('Is 5 a prime?', isPrime(5))
print ('Is 10 a prime?', isPrime(10))

#implementing a Stack
stack = Stack()
data = [random.randint(1,1000) for _ in range(1000)]
stack.push(data)
print("\nPushing to Stack\n\n",data)

print ("\nSieve of Eratosthenes\n")
numbers = data
print(*data, sep=' ')
print ("\nOutput (primes):\n")
primes = sieve(data)
print(*primes, sep=' ')
stack.push(primes)
print("\nPushing to Stack\n\n", primes)

#finding the size of the Stack
howBig = stack.size()
print('\n\n', howBig)


