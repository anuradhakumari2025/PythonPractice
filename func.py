# def greet():
#   # print("Good Day!!")
#   return "Good Day!!"

# user = input("Enter your name: ")
# print(user,greet())

# def wish(name):
#   print("Happy Birthday " + name)

# wish("Anuradha")

#Recursion
# def factorial(n):
#   if(n==1 or n==0):
#     return 1
#   return n * factorial(n-1)

# num = int(input("Enter num to know its factorial: "))
# print(f"The factorial of {num} is {factorial(num)}")

# num = int(input("Enter num to know its factorial: "))
# for i in range(1,num):
#   num = num * i
# print(f"The factorial is {num}")

#Find greatest of 3 num
# def findGreatNum(num1,num2,num3):
#   if(num1>num2 and num1>num3):
#     return num1
#   elif(num2>num1 and num2>num3):
#     return num2
#   else:
#     return num3
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))
# print(f"The greatest number is {findGreatNum(num1,num2,num3)}")

# convert value from celsius to farenheit
# def convertCelsiusToFarenheit(value):
#   return ((9/5)*value) + 32
# value = int(input("Enter a value to convert it from celsius to farenheit : "))
# print(f"The converted value is {convertCelsiusToFarenheit(value)}°F")

#Use of recursion to calculate sum of n natural numbers
# def sum(n):
#   if n <= 0:  # Base case to stop recursion
#     return 0
#   else:
#     return n + sum(n-1)
# num = int(input("Enter num to know sum of its first natural num: "))
# print(f"The sum of first {num} natural number is {sum(num)}")

#Print patterns of * using funtion
# def printPattern(n):
#   for i in range(n, 0, -1):  # Start from n, go down to 1
#         print("*" * i)
# printPattern(3)

# def printPattern2(n):
#     if(n==0):
#         return
#     else:
#         print("*" * n)
#         printPattern2(n-1)
# printPattern2(4)

#convert value from celsius to farenheit
# def convertInchesToCm(value):
#   return 2.54*value
# value = int(input("Enter a value to convert it from celsius to farenheit : "))
# print(f"The converted value is {convertInchesToCm(value)}cm")

#function to multiplication of given number
def multiplicationTable(n):
  for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
multiplicationTable(5)
  
