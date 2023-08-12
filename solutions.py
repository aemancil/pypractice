#farenheight to celcius calculator

f = 84

c = (f - 32) / 1.8

print(c)

#bmi calculator
m = 95
h = 1.53

bmi = m/(h ** 2)

print(bmi)

#hypotenuse.py program
import math
a = 2
b = 3

c = math.sqrt( a ** 2 + b ** 2)

print(c)

#or

a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = (a**2 + b**2) ** 0.5

print(c)

#currency
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

total = pesos * 0.00025 + soles * 0.28 + reais * 0.21

print(total)

#coin_flip.py
import random

num = random.randint(0, 1)   # RNGesus will give us a random number that is either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')

#type casting = convert the data type of a value to another data type
x = 1 #int
y = 2.0 #float
z = "3" #str

x = float(x)
y = int(y)
z = int(z)

print(x)
print(int(y))
print(z)

#inputs
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age+1

print("hello "+ name)
print("Your age next year is: " + str(age))
print("You are " +str(height)+ " short!")

#mathing in python
import math
pi = 3.14
x = 1
y = 2
z = 3

print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi)) #absolute value tells you how far a number is from 0
print(pow(pi,2)) #pi to the power of 2
print(math.sqrt(pi))
print(max(x,y,z)) #find largest value
print(min(x,y,z)) #find minimum value

#slicing and spicing~ index operators
name = "elaine hzii"

first_name = name[:3] # or [0:3]
funky_name = name[::4] # [start:stop:step]
reversed_name = name[::-1]

print(first_name)
print(funky_name)
print(reversed_name)

website = "http://xxxxxxxxxx.com"

slice = slice(7,-4)

print(website[slice])

#while loop - will execute block of code as long as condition == true
name = ""

while len(name) == 0:
    name = input("Enter your name: ")
print("Hello " + name)

# while 1 == 1: 
#  print("help meeee") #infinite loop

# while loop = unlimited
# for loop = limited
for i in range(10):
   print(i +1)

for i in "elaine":
    print(i)


#countdown timer
import time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy Days!!")

# nested loops = one loop inside of another loop
rows = int(input("How many rows?: "))
cols = int(input("How many cols?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()

#break - terminate loop entirely
while True: 
    name = input("Enter your name: ")
    if name != "":
        break

#continue - skip to next iteration of a loop
phone_number = "420-69-666"
for i in phone_number:
    if i == "-":
        continue
    print(i, end ="")

#pass - does nothing, acts as a placeholder
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

#lists and 2d lists
candy = ["chocolate", "gummy bears", "lollipops","sweet tarts"]

#candy.append("bubblegum") #add a value
#candy.remove("chocolate") #remove a value
#candy.pop() #will remove last element
#candy.insert(0,"sprinkles") #index 0 add sprinkles
#candy.clear() #remove all elements of a list
#candy.sort() #sort a list alphabetically

for i in candy:
    print(i)

dessert = ["candy", "ice cream"]
drinks = ["tea", "soda", "coffee"]
veggie = ["cucumber","potato"]

food = [dessert,drinks,veggie]

print(food)
print(food[0][0])

#tuple - collection which is ordered and unchangeable
student = ("Elaine",24,"f")

print(student.count("Elaine"))
print(student.index("f"))

for i in student:
    print(i)

if "Elaine" in student:
    print("Elaine here!")

#set - collection which is unordered, unindexed, no duplicates
utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("spork")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)
dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils)) #what do dishes have that utensils doesn't
# print(utensils.intersection(dishes)) #what do they have in common?

for i in dinner_table:
    print(i)

#dictionary - changeable, unordered collection of unique key: value pairs, fast because they use hashing

capitals = {'USA':'Washhington DC',
            'India':'New Dehli',
            'China':'Bejing',
            'Russia':'Moscow'}

capitals.update({'Poland':'Warsaw'})
capitals.update({'USA':'W. DC'})
capitals.pop('China') #remove a key value pair
#capitals.clear() #clear entire dict

#print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())

for key,value in capitals.items():
    print(key, value)

#index operater[] = gives acccess to a sequence's element
name = "elaine"
#if(name[0].islower):
#    name = name.capitalize()
first_name = name[:3].upper()
last_name = name[3:].lower()
last_ch = name[-1]#last element will be -1
print(first_name)
print(last_name)
print(last_ch)


