#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

    #greet (Elijah):
    #print(f"Hello, {Elijah}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    #Hello, programmer!

def add(num1, num2):
    return num1 + num2
#result=add(3,5)
#print(result)


def halve(number):
    return number/2
#result=halve(8)
#print(result)