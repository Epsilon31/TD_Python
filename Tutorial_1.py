import numpy as np
import math
import matplotlib.pyplot as plt
import random

#Exercise 1

def profiling(name,age,height):

    #name

    if len(name) >20:
        print("Your name is long\n")
    elif len(name) > 15:
        print("Your name is semi-long\n")
    elif (len(name) > 8) and (len(name) <= 10):
        print("Your name is semi-short \n")
    else:
        print("Your name is short \n")

    #age

    if age >= 18:
        print("You are an adult\n")
    else:
        print("You are not an adult\n")
    #Height

    if height> 172:
        print("You are tall\n")
    else:
        print("You are not tall\n")

    return None
#profiling("Arthur", 20, 180)

#Exercise 2

def check(n):
    test = True
    if n<0:
        print("This number is negative\n")
    else:
        print("This number is positive \n")
    if n%2 == 0:
        print("This number is even\n")
    else:
        print("This number is odd\n")
    if n==1:
        test = False
    elif n==2:
        print("This number is a prime number")
    else:
        for i in range(2, n):
            if n%i == 0:
                test = False
    if test == True:
        print("This number is a prime number\n")
    else:
        print("This is not a prime number ")

#check(10)

def count_even_odd(L):
    compteur_even = 0
    compteur_odd = 0
    
    for i in range(len(L)):
        if L[i]%2 == 0:
            compteur_even += 1
        else:
            compteur_odd += 1
    return compteur_odd,compteur_even

def count_prime_number(L):
    compteur_prime = 0
    test = True
    for i in range(len(L)):
        if L[i] == 2:
            compteur_prime+=1
        elif L[i] > 2:
            test = True
            for j in range(2,L[i]):
                if L[i] % j == 0:
                    test = False
            if test == True:
                compteur_prime += 1
    return compteur_prime
            
#print(count_even_odd([1,2,3,4,5,6,7,8,9,10]))
#print(count_prime_number([1,2,3,4,5,6,7,8,9,10]))

#Exercice 3

def Pass_checker(password):
    """ Test your password """
    test = True
    compteur_lower = 0
    compteur_upper = 0
    compteur_number = 0
    compteur_char = 0
    compteur_total = 0

    for i in range(len(password)):
        if (password[i]>= 'a') and (password[i] <= 'z'):
            compteur_lower+=1
        elif (password[i] >='A') and (password[i] <='Z'):
            compteur_upper+=1
        elif (password[i]>= '0') and (password[i] <= '9'):
            compteur_number+= 1
        elif (password[i] == '$','#','@'):
            compteur_char += 1
        
        compteur_total = compteur_lower + compteur_char + compteur_upper + compteur_number
        print("compteur_lower = ", compteur_lower)
        print("compteur_upper =",compteur_upper)
        print("compteur_number = ", compteur_number)
        print("compteur_char = ",compteur_char)
        print("compteur_total = ", compteur_total)

        if (compteur_lower<2):
            print("You need at least two lower character\n")
            test = False
        elif(compteur_upper<2):
            print("You need at least two upper character\n")
            test = False
        elif(compteur_number < 2):
            print("You need at least two number\n")
            test = False
        elif(compteur_char == 0):
            print("You need at least a special character\n")
            test = False

        if (compteur_total<6):
            print("Your password is too short\n")
            test = False
        elif (compteur_total>16):
            print("Your password is too long \n")
            test = False


        if (test):
            print("Your password is efficient !\n")
    return None
        
#Pass_checker("DIngo25#")    

#Exercise 4

def guess_game():
    """ A small game to guess a random number btw  0 and 100"""
    guess = random.randint(0,100)
    res = False
    while(res == False):
        test = int(input("Give a number btw 0 and 100\n"))
        if (test > guess):
            print("Your number is bigger than the correct number\n")
        elif (test < guess):
            print("Your number is smaller than the correct number\n")
        else:
            print("It's the correct number !\n ",guess)
            test = True
    return None

#guess_game()

#Exercise 5
def Fibo(n):
    """This program calculate the Fibonnaci sequence for a number n given by the user"""
    L=[0,1]
    if n == 0:
        return 0
    elif n == 1:
        return L
    else:
        for i in range(2,n+1):
            L.append(L[i-1]+L[i-2])
        
        return L

#print(Fibo(7))

def Fibo_rec(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo_rec(n-1) + Fibo_rec(n-2)
#print(Fibo_rec(3))

#Exercise 6

def Facto_rec(n):
    if n==0:
        return 1
    else:
        return n*Facto_rec(n-1)
    
def binomial_coefficient(n,k):
    if (n-k < 0) or (k<0):
        return 0
    elif (n==k):
        return 1
    else:
        return Facto_rec(n)/Facto_rec(k)*(Facto_rec(n-k))

#Exercise 7

def text_analysis(text):
    compteur = 0
    compteur_words= 0
    compteur_vowels = 0
    compteur_words_vowels = 0 #count words containing only two or more vowels
    L_vow=['a','e','i','o','u','y']

    L = text.split()
    compteur_words = len(L)

    for i in range(len(text)):
        for j in range(len(L_vow)):
            if text[i] == L_vow[j]:
                compteur_vowels += 1

    for i in L:
        compteur = 0
        for j in range(len(i)):
            for k in range(len(L_vow)):
                if i[j] == L_vow[k]:
                    compteur += 1
        if compteur >=2:
            compteur_words_vowels +=1

       
    return compteur_words_vowels, compteur_vowels, compteur_words