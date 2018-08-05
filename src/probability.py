import random as rd
import math as mt


# Function to check if a list have duplicated elements
def has_duplicates(l):
    dic = {}
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in dic.values():
        if j > 1:
            return True
    return False


# Function to check if a list elemnt repeated three times
def has_three(l):
    dic = {}
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in dic.values():
        if j > 2:
            return True
    return False


# Birthday paradox
def birthday_paradox():
    counter = 0
    for i in range(0, 10000):
        students = []
        for j in range(27):
            students.append(rd.randint(1, 365))
        if has_duplicates(students):
            counter += 1
    return counter / 10000


# Paradox for three birthdays
def birthday_paradox_3():
    counter = 0
    for i in range(0, 10000):
        students = []
        for j in range(27):
            students.append(rd.randint(1, 365))
        if has_three(students):
            counter += 1
    return counter / 10000


# Approximate probability
def approx():
    power = (27 ** 2) / (2 * 365)
    return 1 - mt.pow(mt.e, -power)


# Exact probability
def exact():
    p = 1
    for i in range(27):
        p *= (365 - i) / 365
    return 1 - p


print("Exact:", exact())
print("Approximate:", approx())
print("Birthday Paradox Function:", birthday_paradox())
print("Function for 3 students:", birthday_paradox_3())
