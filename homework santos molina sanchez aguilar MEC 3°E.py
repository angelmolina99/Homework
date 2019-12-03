#!/usr/bin/env python
# coding: utf-8

# # EXCERCISE N°13
# ## PARAMETERS, UNPACKING, VARIABLES
# 
# In this exercise we will change the input variables to a script. Then this program will show

# In[5]:


from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# # EXCERCISE N°14
# ## PROMPTING AND PASSING
# 
# In this excercise we are gonna use teh argv and input together to ask the user something specific.

# In[ ]:


from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = imput(prompt)

print(f"Whre do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. nice.
""")


# In[ ]:


# EXERCISE N°15
## READING FILES

This excercise involves writing two files. This second file isn't a script but a plain text file we'll be reading in our script


# In[ ]:


from sys import argv

script, filename = argv

txt = open(filename)

print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


# In[ ]:


# EXERCISE N°16
## READING AND WRITING FILES

In this exercise we will learn to use the commands, some also take parameters but in this exercise we will make a small text editor


# In[ ]:


from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()


# In[ ]:


# EXERCISE N°17
## MORE FILES

In this exercise we will learn to use the files, and it will give us the idea of how to do several things with them


# In[ ]:


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out-file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# In[ ]:


# EXERCISE N°18
# NAMES, VARIABLES, CODE, FUNCTIONS

The functions do three things:

*They name pieces of code the xay variables name strings and numbers

*They take argumnts the way your scripts take argv

*Using 1 and 2, they let you make your own "mini.scripts" or "tiny commands"

We can create a function by using the word def in Python


# In[ ]:


def print_two(*args):
    arg1 ,  arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
def print_two_again(arg1 ,  arg2):
    print(f"arg1: {arg1}, arg2 {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing'.")
    
    

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()


# Del Angel Mendoza Ana Gabriela

# In[ ]:


# EXERCISE N°19
## Functions and Variables 


# This shows all the different ways we’re able to give our function of the values it
# needs to print them. We can give it straight numbers. We can give it variables. We can give it math. We
# can even combine math and variables.
# 

# In[5]:


def heros_and_fusions(hero_count, fusions_of_heros):
    print(f"you have {hero_count} heros" )
    print(f"you have { fusions_of_heros} fusions of heros")
    print("bro that's enough for a duel!")
    
print("We can just give the function numbers directly:") 
heros_and_fusions(30, 15)
    
print("OR, we can use variables from our script:") 
amount_of_heros = 20 
amount_of_fusions_of_heros = 10
heros_and_fusions(amount_of_heros, amount_of_fusions_of_heros)

print("We can even do math inside too:") 
heros_and_fusions(30 + 20, 15 + 10)

print("And we can combine the two, variables and math:") 
heros_and_fusions(amount_of_heros + 200, amount_of_fusions_of_heros + 70)


# In[ ]:


# EXERCISE N°20
## Functions and Files 


# here we see how a function and a row work together

# In[ ]:


from sys import argv

script, input_file = argv
 
def print_all(f): 
    print(f.read())
def rewind(f): 
    print( f.seek(0))

def print_a_line(line_count, f): 
    print(line_count, f.readline())

    current_file = open(input_file)

    print("First let's print the whole file:\n")

    print_all(current_file)

    print("Now let's rewind, kind of like a tape.") 

    rewind(current_file) 

    print("Let's print three lines:")

current_line = 1 
print_a_line(current_line, current_file)
 
current_line = current_line + 1 
print_a_line(current_line, current_file)
 
current_line = current_line + 1 
print_a_line(current_line, current_file)


# In[ ]:


# EXERCISE N°21
## Functions Can Return Something


# here we will use words to establish
# variables to be a value of a function.

# In[20]:


def add(a, b): 
    print(f"ADDING {a} + {b}") 
    return a + b

def subtract(a, b): 
    print(f"SUBTRACTING {a} - {b}") 
    return a - b

def multiply(a, b): 
    print(f"MULTIPLYING {a} * {b}") 
    return a * b
 
def divide(a, b): 
    print(f"DIVIDING {a} / {b}") 
    return a / b 

print("Let's do some math with just functions!")
 
age = add(19, 7) 
height = subtract(172, 10) 
weight = multiply(96, 9) 
iq = divide(192, 2)
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")
 
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
 
print("That becomes: ", what, "Can you do it by hand?")


# In[ ]:


# EXERCISE N°40
## Modules, Classes, and Objects


# Objects are an encapsulation of variables and functions in a single entity. Objects obtain their variables and functions from classes.

# In[29]:


class Song(object): 

    def __init__(self, lyrics): 
        self.lyrics = lyrics

    def sing_me_a_song(self):      
        for line in self.lyrics: 
            print(line)

the_reason = Song(["I'm sorry that I hurt you", 
                    "It's something I must live with everyday", 
                    "And all the pain I put you through"
                    "I wish I could take it all away"
                    "And be the one who catches all your tears"
                    "That's why I need you to hear"])
 
waste = Song(["And every day that you want to change, that you want to change, yeah", 
            "I'll help you see it through 'cause I just really want to be with you"])
the_reason.sing_me_a_song()
waste.sing_me_a_song()


# In[ ]:


# EXERCISE N°41
## Learning to Speak Object-Oriented


# In this code we will see how to use words to form sentences

# In[ ]:


import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
    "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
 }

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
    
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
    
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
               random.sample(WORDS, snippet.count("%%%"))]

    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []


    for i in range(0, snippet.count("@@@")):

        param_count = random.randint(1,3)
        param_names.append(', '.join(
        random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]
        
        for word in class_names:
            result = result.replace("%%%", word, 1)
            
        for word in other_names:
            result = result.replace("***", word, 1)
        
        for word in param_names:
            result = result.replace("@@@", word, 1)
            
        results.append(result)
    return results

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
                
            print(question)
            
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
                print("\nBye")


# In[ ]:


# EXERCISE N°42
## Is-A, Has-A, Objects, and Classes


# here we will see the difference between an object and classes

# In[ ]:


class Animal(object):
    pass

class Dog(Animal):
    
    def __init__(self, name):
        
        self.name = name
        
class Cat(Animal):

    def __init__(self, name):
        
        self.name = name
        
class Person(object):
    
    def __init__(self, name):
        
        self.name = name
        
        self.pet = None
        
class Employee(Person):

    def __init__(self, name, salary):
        
        super(Employee, self).__init__(name)
        
        self.salary = salary
        
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

