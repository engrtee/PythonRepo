character_name='John'
character_age= "35"
is_male= True
# string, number or boolean
print("There was a man named "  + character_name + ",")
print("The man named "  + character_name + " is " + character_age + " years old" )

character_name='Peter'
character_age= "15"
print("There was a man named "  + character_name + ",")
print("The man named "  + character_name + " is " + character_age + " years old" )

#Working with strings
print("Giraffe \Academy")
phrase=("Giraffe \Academy")
print(phrase + "is cool" )
print(phrase.lower().islower())
print(len(phrase))
print(phrase[3])
print(phrase.index("a"))
print(phrase.replace("Giraffe", "Hyena"))
print(phrase.find("Hyena"))

#Working with Numbers
print(-2.03030)
print(10 % 3)

my_num = 5
print(str(my_num) + " is my favorite number")
print(pow(3,3))
print(max(2,5))
print(min(2,5))
print(round(4.56))
from math import *
print(sqrt(36))
##name = input("Enter your name: ")
#3age = input("Enter your age: ")
##print("Hello " + name + "! You are " + age + " years old" )


#num1=input("Enter a number:")
#num2 = input("Enter another number:")
#result = float(num1)+float(num2)
#print(result)
#MAD LIBS PYTHON GAME

#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")


#school = input("Enter your academic qualifications: ")
#specialty = input("Enter what your core interests are: ")
#church = input("Enter a Denomination: ")

#print("What exactly is your specialty? Well i am into " + specialty + "." )
#
#perfeprint("I attended " + school + "in the year 2014 and i attended " + church +"'s fellowship while i was there")

#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("i love " + celebrity)
#Lists
friends = ["tolu", "tosin","pelumi"]
#print(friends[1])

#List Functions
lucky_numbers=[3,7,9,12,34,5,8]
friends = ["tolu", "tosin","pelumi","pelumi","kate","serere"]
#friends.extend(lucky_numbers)
#friends.append("creek")
#friends.insert(1,"Tobi")
#friends.remove("kate")
#friends.pop()
#print(friends.count("pelumi"))
#friends.sort()
#friends.reverse()
#friends2= friends.copy()
#print(friends2)

#Tuple is a structure where we can store multiple pieces of information ..its similar to list but it has differences. It cant be changed or modified. 
#coordinates = [(4,5),
#print(coordinates)

#Functions
def sayhi(name,age):
    print("Hello " + name ,"you are " + age + " years old")


sayhi("Mike", "35")
sayhi("Leo", "70") 


def cube(num):
   return num * num * num
result = cube(8)
print(result)


#IF Statements
#is_male = False
#is_tall = False

#if is_male and is_tall:
 #   print("you are a male or tall or both")
#elif is_male and not(is_tall):
 #   print("You are a short male")
#elif not(is_male) and is_tall:
 #   print("You are not a male but are tall")
#else:
 #   print("You are neither a male nor tall")


    #Comparison Operators
def max_num(num1,num2 ,num3):
    if num1 >=num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

 print(max_num(30,23,1))   

#num1 = float(input("Enter your first number: "))
#op = (input("Enter your operator: "))
#num2 = float(input("Enter your second number: "))

#if op == "+" :
 #   print(num1 + num2)
#elif op == "-":
 #   print(num1-num2)
#elif op == "/":
 #   print(num1 / num2)
#elif op == "*" :
#    print(num1 * num2)
#else:
 #   print("Invalid Operator")

  #Dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June ",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}  
print(monthConversions.get("August"))




