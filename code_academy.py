
######
## Misc
######

# indentation should be 4 spaces = 1 tab

# single line comment use #

"""
Multiline comment use 
"""

######
## Primative Operations
######

# floating point be careful
5   / 10 # = 0
5.0 / 10 # = 0.5

######
## Strings
######

# commas, etc can be escaped with \
text = 'this isn\'t impressive, yet'
print text

# python counting/index starts at 0 not 1
fifth_letter = 'MONTY'[4]
print fifth_letter

# str converts to string
str(24)

# dot notation works only on strings
lion = "roar"
len(lion)
print lion.upper()
print "aBcD".upper()
# however, len() can be used on other objects e.g. vectors

# use + for concatenation
pi = "3.14"
print "life" + " of " + pi

# when concatenating non strings, need to explicitly coerce into string
print "pi " + str(3.14) + " ..."

# can use % for variable concatenations
print "insert into db.%s SELECT * FROM db.%s WHERE a = %s" % ("calls", "calls2", str(1))

######
## Date Time
######

# datetime library
from datetime import datetime
now = datetime.now()
print now
print now.year
print '%s-%s-%s' % (now.year, now.month, now.day)
print str(now.year) + '-' + str(now.month) + '-' + str(now.day)
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

######
## Conditionals & Control Flow
######

alex = 23

def old():
    if alex > 20:
        return "you old bro"
    elif alex < 10:
        return "baby face"
    else:
        return "hokkkkay"

print old()

######
## Functions
######

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
print tax(meal_cost)*1.10


def cube(number):
    """ input a number to be cubed """
    return number**3

def by_three(number):
    """ if divisible by 3, cube, else return False """
    if number % 3 == 0:
        return cube(number)
    else:
        return False

def add_function(a,b):
    """ add two ints """
    return(a+b)

def get_element(list,element):
    """ get element of list """
    return(list[element])
n = [3, 5, 7]
get_element(n,2)

# function + for loop
n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
print double_list(n)

# python: range(1,100) == r: 1:100
for i in range(len(n)):
    print n[i]

def summ(list):
    running_total = 0
    for i in range(len(list)):
        running_total = list[i] + running_total
    return running_total


######
## Modules
######

# Generic import
import math
print math.sqrt(25)

# Function import
from math import sqrt
sqrt(25)

# Universal import
""" avoid where possible - clutters your program and potential for clashes """
""" universal import will overwrite any previously defined functions/vars """
from math import *
sqrt(25)

######
## Functions for vectors, etc
######

# to allow input of multiple arguments
""" note: inputting  vec = (1,2,3) does not work """
def biggest_number(*args):
    return max(args)

# same as 'class' in R
type(42)
type('alex')
def is_numeric(num):
    return type(num) == int or type(num) == float

######
## Lists
######

list1 = [1,2,4]
listone = ["one","two","four"]

list1.append(5)
listone.append("five")

len(list1)
len(listone)

# up to but not including
list1[0:2] # == list[0], list[1]
listone[0:2]

# don't have to use 1:len(list1); can just use 1:
list1[1:]

# can find index of item
listone.index("five") # == 3
listone[listone.index("five")]  # == "five"

# remove item based on index
list1.pop(2)

# remove item based on item name
listone.remove("four")

#for loops

my_list = [1,9,3,8,5,7]
for number in my_list:
    print 2 * number
 

start_list = [5, 3, 1, 2, 4]
square_list = []

for item in start_list:
    square_list.append(item ** 2)

square_list.sort()
print square_list

######
## Dictionaries
######

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
menu['Pizza'] = 4.02 # Adding new key-value pair
print menu['Chicken Alfredo']

del menu[4.02] # deletes key-value pair
menu['Chicken Alfredo'] = menu['Chicken Alfredo'] + 10.10
print menu

######
## Loops
######

count = 0
while count <= 10:
    print count
    count = count + 1

for count in range(10+1):
    print count

## code broken, but you get the idea:
choice = raw_input('Enjoying the course? (y/n)')
while (choice != "y" and choice != "n"):
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
else:
    print "thank you for your feedback brother"

# using break
count = 0
while True:
    print count
    count += 1
    if count >= 10:
        break

# using while/else
from random import randint

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"



## number guessing game
from random import randint

random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = raw_input('pick number between 1 and 10:')
    if guess == str(random_number):
        print "you win!"
        yay = "!"
        for i in range(1000):
            yay = yay + "!"
        print yay
        print "correct! number was " + str(random_number)
        break
    else:
        guesses_left = guesses_left - 1
        print "wrong. " + str(guesses_left) + " guesses remain."
else:
    print "You lose."
    print "number was " + str(random_number)

## take a string
## reverse list
input_string = raw_input('Enter a string to reverse:')
input_string[::-1]


######
## Lambda
######

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)


######
## Bitwise / Binary opperations
######

#1
print 0b01
#2
print 0b10 

#1 + 3
print 0b1 + 0b11 
#3 * 3
print 0b11 * 0b11 

# convert 2 -> binary
print bin(2) 
# convert binary -> 2
print int("0b10",2) 
print int("10",2) 
# convert oct -> 17
print int("021",8) 

# Left Bit Shift {<<}  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift {>>}
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0) 

## AND {&}
#     a:   00101010   42
#     b:   00001111   15       
#    ===================
# a & b:   00001010   10

#0b111 (7) & 0b1010 (10) = 0b10 (2)
0b111 & 0b1010

## OR {|}
#     a:  00101010  42
#     b:  00001111  15       
#     ================
# a | b:  00101111  47

#0b110 (6) | 0b1010 (10) = 0b1110 (14)
0b110 | 0b1010
bin(0b110 | 0b1010)

## XOR {^}
## Exlusive OR: OR only, not AND OR
#     a:  00101010   42
#     b:  00001111   15       
#      ================
# a ^ b:  00100101   37

# 111 (7) ^ 1010 (10) = 1101 (13)
bin(0b111 ^ 0b1010)

## Using a mask to check if a bit is on
num =   0b01001001
mask4 = 0b00000100
mask8 = 0b00001000

mask4_test = num & mask4
mask8_test = num & mask8

if mask4_test > 0:
    print "Bit 4 was on"

if mask8_test > 0:
    print "Bit 8 was on"

## function not going to work because can't work on the output of bin(integer)
#def mask4(integer):
#    if 0b00000100 & bin(integer) > 0:
#        return("Bit 8 was on")


## Using a mask to ensure a bit is turned on
num =   0b01001001
mask4 = 0b00000100
mask8 = 0b00001000

mask4_on = num | mask4
mask8_on = num | mask8


## Using a mask to flip a bit
num =   0b01001001
mask4 = 0b00000100
mask8 = 0b00001000

mask4_flip = num ^ mask4
mask8_flip = num ^ mask8

print bin(num)
print bin(mask4_flip)
print bin(mask8_flip)


######
## Object Orientated Programming
######


class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)
    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()


class Animal(object):
    def __init__(self,name):
        self.name = name

zebra = Animal("Jeffrey")
print zebra.name


class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Rachael",23)
hippo.description()


class Car(object):
    """Object Car"""
    condition = "new"
    def __init__(self,model,color,mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    def display_car(self):
#        print "This is a %s %s with %s MPG" (self.color, self.model, str(self.mpg))
        print "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."
    def drive_car(self):
        self.condition = "used"

## Create duplicate instance of car
my_car = Car("DeLorean","silver",88)

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

#my_car.display_car()

"""
print(my_car.model)
print(my_car.color)
print(my_car.mpg)
"""

class ElectricCar(Car):
    """Object Electric Car; based on class Car"""
    def __init__(self,model,color,mpg,battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("DeLorean","silver",88,"molten salt")


print(my_car.condition)
my_car.drive_car()
print(my_car.condition)


## Representation

class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)

print(my_point)


######
## File Input Output
######

# "w" = write
# "r" = read
# "r+" = read and write
# "a" = append

my_file = open("output.txt", "r+")

## Write
## (ERROR)
my_list = [i**2 for i in range(1,11)]
my_file = open("output.txt", "r+")

for i in range(0,9):
    my_file.write(str(my_list[i])) 
    my_file.write("\n")

my_file.close()

## Read
my_file = open("output.txt","r")
print my_file.read()
my_file.close()

## Read line at a time
## ERROR
my_file = open("text.txt","r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

## Read/Write as an object
with open("text.txt", "w") as textfile:
    textfile.write("Success!")

with open("text.txt", "w") as my_file:
    my_file.write("Success!! x2")

if my_file.closed == False:
    my_file.close()
        
print my_file.closed
