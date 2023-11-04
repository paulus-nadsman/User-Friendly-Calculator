#This begins the User Friendly calculator 2.0
#project  started on november 1st 2023, by Paul Schulz

#Imports the math module and allows for just about every possible math function to be used 
import math 

#Variables storing the user inputs 
user1 = float(input("Enter Number Here" + " "))
print(" ")
user2 = float(input("Enter Number Here" + " "))
print(" ")
user3 = str(input("Enter Operation Here" + " "))
print(" ")
user4 = str(input("Type degrees to convert trig functions to degrees" + " "))

#Variable that stores user input operation
calc = user3



#Conditional statement checking user inputs and matching them with the correct operation
if calc == "add" : 
    print(user1 + user2)
    print(" ")
elif calc == "subtract" : 
    print(" ")
    print(user1 - user2)
    print(" ")
elif calc == "multiply" : 
    print(" ")
    print(user1 * user2)
    print(" ")
elif calc == "divide" : 
    print(" ")
    print(user1 / user2)
    print(" ")
elif calc == "square root" :
    print(" ")
    print("Only Takes Square Root of First Number")
    print(math.sqrt(user1))
    print(" ")
elif calc == "sin(x)" : 
    print(" ")
    print("Takes Sine of first number in radians")
    print(math.sin(user1))
    print(" ")
elif calc == "cos(x)" : 
    print(" ")
    print("Takes Cosine of first number in radians")
    print(math.cos(user1))
    print(" ")
elif calc == "tan(x)" :
    print(" ")
    print("Takes Tangent of first number in radians")
    print(math.tan(user1))
    print(" ")
elif calc == "log10(x)" :
    print(" ")
    print("Takes base log 10 of first number")
    print(math.log10(user1))
    print(" ")
elif calc == "ln(x)" :
    print(" ")
    print("Takes the natrual log of the first number")
    print(math.log1p(user1))
    print(" ")
elif calc == "exponet" :
    print(" ")
    print("Takes first number raised to second number")
    print(math.pow(user1, user2))
    print(" ")



#Conditional statement that checks for trig functions then converts the calculated value to degrees
if calc == "sin(x)" and user4 == "degrees" :
    print("Takes Sine of first number in radians then converts to degrees")
    print(math.degrees(math.sin(user1)))
    print(" ")  
elif calc == "cos(x)" and user4 == "degrees" : 
    print("Takes Cosine of first number in radians then converts to degrees")
    print(math.degrees(math.cos(user1)))
    print(" ")
elif calc == "tan(x)" and user4 == "degrees" : 
    print("Takes Tangent of first number in radians then converts to degrees")
    print(math.degrees(math.tan(user1)))
    print(" ")


