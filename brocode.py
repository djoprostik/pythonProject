x = input("enter your name: ")
print(f'Hello {x}')
-----------------------------------------------------
a = 5
b = 4
print("If multiply", a, "by", b, "equals", a*b)
print(f'If multiply {a} by {b} equals', a*b) # it is better to write the print function through the format function
-----------------------------------------------------
name = str(input('enter your name:'))

chat_num = len(name)
print(chat_num)
-----------------------------------------------------
first = str(input('Enter your first name:')).upper() # .upper() - to convert input to only capilas letters
last = str(input('Enter your last name:')).upper()
middle = str(input('Enter your middle name:')).upper()

initials = first[0] + middle[1] + last[0] # to take any single character

nik = first[0:2] + " " + last[-2:-1]  # to take couple consecutive characters
# also if it is difficult to count last characters we can write "-1"

print(f'Your initials are: {initials}')
print(f'Your nik name is: {nik}')

-----------------------------------------------------

print('It\'s time to sleep') # if you want to put (') symbol inside quotes ('') you have to add (\) back slash

-----------------------------------------------------

length = float(input('Enter the length of your room:\n')) # \n - to transfer the input to the new line
print(f'Your room has {length} metres in length')
width = float(input('Enter the width of your room:\n'))
print(f'Your room has {length} metres in width')
print(f'The square of you room is {length * width} m2')
in_acres = round((length * width / 0.3048 / 43560),5) # round function is used to make only 4 digits after coma
print(f'The square of your room in acres is {in_acres} ')

-----------------------------------------------------

print('The price for the bottles < 1 litre, the price is 0.10$, and 0.25$ for > 1 litre')
print('---------------')
amount1 = int(input('How many bottles with volume less than 1 litre you have: '))
amount2 = int(input('How many bottles with volume less than 1 litre you have: '))
price1 = 0.10 # in $
price2 = 0.25 # in $
sum1 = round((amount1 * price1),2)
sum2 = round((amount2 * price2),2)
print(f'You have ${sum1} for the small bottles.')
print(f'You have ${sum2} for the small bottles.')

-----------------------------------------------------

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

we can write the same code like below

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

-----------------------------------------------------

say = print
say("Whoo! i can t ")

-----------------------------------------------------

lambda function

def double(x):
    return x * 2

print(double(5))

double = lambda x:x * 2
print(double(5))

double = lambda x: x * 2
print(double(2))

multiply = lambda x,y: x * y
print(multiply(5, 6))

add = lambda x, y, z: x + y + z
print(add(5, 6, 7))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Evgeniy", "Balyka"))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))

-----------------------------------------------------

squares = []

for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

-----------------------------------------------------

students = [100,90,80,70,60,50,40,30,20,10,0]

passed_students = list(filter(lambda x: x>= 60, students)) # this

passed_students = [i for i in students if i >= 60] # or this

passed_students = [i if i >= 60 else 'failed' for i in students]

print(passed_students)

-----------------------------------------------------

import time

#print(time.ctime(time.time()))

time_object = time.localtime()
time_object = time.gmtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

-----------------------------------------------------

x = "Hello world"
print(x)
print(type(x))
x = 1+2+3*2
print(x)
aaa = print
a = 2 + 4
aaa(a)


-----------------------------------------------------

a = int("1" + "1") - 2 # equals  = 11 -2 =9
print(a)


a = 6 / 2           #float
b = round(6 / 2)    #int
print(type(a))
print(type(b))

a = 8%3    # ostatok ot delenia = 2
print(a)

a = 2 * 1.5          # float
print(type(a))

b = 2 * "1.5"        # str
print(type(b))


a = 2
a += 1  # =    a = a + 1, the same operation we can make with *, -, /
print(a)


print("a" * 3)

-----------------------------------------------------

from fractions import Fraction
import sys

a = Fraction(1,3)
c = 1/3
b = c*3

print(b)
print(sys.getsizeof(a))
print(sys.getsizeof(b))

-----------------------------------------------------

date5: int = 1278

text = "hello new year"

text_1 = "Hello" + str(date5) + "year"

text_2 = "Hello {y} year{x}".format(x=date5, y="!")

text_3 = f"hello {date5 = } \n new year"

print("hello" , date5 , "year")


remove it


print(text_3)

print(text_2)

a = int("1")
b = int("2")

print(a > b)

print("new line")

-----------------------------------------------------

a = 0.1
b = 0.1
c = 0.1

d = round(a+b+c,1) # or d = round(a,2) + round(b,2) + round(c,2)

print(d == 0.3)


a = 1,9
a = int(a)
print(type(a))

a = 2
b = 5
tmp = a
a = b
b = tmp
print(a)
print(b)

-----------------------------------------------------

a = 3 + 5
b = a / 2
print(b)

var1 = 500
var2 = 500
print(var1 == var2)
print(var1 is var2)

-----------------------------------------------------

x = 1
while x <= 10:
    print("running")
    x += 1
    print(x)

-----------------------------------------------------

var3 = "volume1"
var4 = "v"+"o"+"l"+"u"+"m"+"e"+"1"
var5 = ["v","o","l","u","m","e","1"]
print(var5[3])
var5[1] = "u"
print(var3)
print(var4)
print(var5)
print(var3 == var4)
print(var3 == var5)

-----------------------------------------------------

var_1 = "volume1"
var_2 = ["v","o","l","u","m","e","1"]

var_3 = var_1[:3] + "2" + var_1[4:]

print(var_3)

-----------------------------------------------------

date: int = 1278

text = "Hello new year"

text_1 = "Hello " + str(date) + " year"

text_2 = "Hello {y} year {x}".format(x=date, y="any")

text_3 = f"Hello {date=}  \\new year"

print("Hello " , date_5 + , year")

-----------------------------------------------------

print(s := 45)
print(a := 234, f"string {a}")

-----------------------------------------------------

from car import Car

car_1 = Car("Chevy","Corvette","2021","blue")
car_2 = Car("Ford","Mustang","2022","red")