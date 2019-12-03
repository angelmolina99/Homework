#!/usr/bin/env python
# coding: utf-8

# # Exercise 17-21

# In[ ]:


##EXERCISE 17


from sys import argv
from os.path import exists

script, from_file, to_file=argv
print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the input file existe?{exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file=open(to_file,'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()


# ### EXERCISE 18

# In[4]:


def print_two(*args):
    arg1,arg2 = args
    print(f"arg1:{arg1}, arg2: {arg2}")
    
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
def print_one(arg1):
    print(f"arg1: {arg1}")
    
def print_none():
    print("I got nothin'.")
    
print_two("FERNANDO","MARTINEZ")
print_two_again("FERNANDO","MARTINEZ")
print_one("FIRST!")
print_none()


# ### EXERCISE 19

# In[6]:


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses! ")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("get a blanket. \n")
    
print("we can just give the function numbers directly: ")
cheese_and_crackers(30, 40)

print("OR, we can use variables rom our script: ")
amount_of_cheese =20
amount_of_crackers= 60

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
cheese_and_crackers (20+30, 10+12)

print("and we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 200, amount_of_crackers + 2000)


# ### EXERCISE 20

# In[24]:


from sys import argv

script, input_file, fernando= argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(fernando)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape. ")

rewind(current_file)

print("let's print three lines: ")
 
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line,current_file)

current_line= current_line + 1
print_a_line(current_line, current_file)


# ## EXERCISE 21

# In[31]:


def add(a, b):
    print(f"ADDING {a}-{b}")
    return a + b
def substract(a, b):
    print(f"SUBSTRACTING {a}-{b}")
    return a - b
def multiply(a, b):
    print(f"MULTIPLYING {a}*{b}")
    return a * b
def divide(a, b):
    print(f"DIVIDING {a}/{b}")
    return a / b
print("Lets do some math with just functions!! ")

data=add(30, 5)
height=substract(78,4)
weight=multiply(90,2)
chair=divide(100, 2)

print(f"data: {data}, height: {height}, weight: {weight}. chair: {chair}")

print("here is a puzzle")

what=add(data,substract(height,multiply(weight,divide(chair,2))))

print("That becomes: ", what, "can you do it by hand?")


# In[ ]:

