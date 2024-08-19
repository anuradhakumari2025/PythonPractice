# class Employee:
#   language = "Python"
#   salary = 100000
#   def __init__(self): #dunder method is called automatically
#     print("What's up")

#   @staticmethod
#   def greet():
#     print("Well done!!")
  
#   def getInfo(self):
#     print(f"The salary is {self.salary} and language is {self.language}")

# harry=Employee()
# harry.name =  "Anuradha"
# harry.getInfo()
# harry.greet()
# print(harry.language,harry.name)

#class store info of programmers
# class programmer:
#   company = "Microsoft"
#   def __init__(self,name,salary,language):  #constructor
#     self.name = name
#     self.salary = salary
#     self.language  = language

# harry = programmer("Anuradha",10000000,"python")
# print(f"Programmer name is {harry.name}, language is {harry.language},salary is {harry.salary} and working in company{harry.company}")

#class to claculate square,cube and square of a number
# class Calculator:
#   def __init__(self,n):
#     self.n = n
#   def square(self):
#     print(f"The square of num is {self.n*self.n}")
#   def squareRoot(self):
#     print(f"The square root of num is {self.n**1/2}")
#   def cube(self):
#     print(f"The cube of num is {self.n*self.n*self.n}")
#   def greet(self):
#     print("Hello")
# num = int(input("Enter a num: "))
# a = Calculator(num)
# a.greet()
# a.square()
# a.squareRoot()
# a.cube()

# class Change():
#   a=3
# harry=Change()
# print(harry.a)
# harry.a = 0
# print(harry.a)
#print(Change.a) #it show that class attribute is not changed

#know train status
from random import randint
class Train():
  def __init__(self,name,start,destination,noOfSeat,tier):
    self.name = name
    self.start = start
    self.destination = destination
    self.noOfSeat = noOfSeat
    self.tier = tier
  def getStatus(self,noOfSeats):
    self.noOfSeat  = noOfSeats
  def getFare(self,start,destination,price):
    self.price = price
    self.start = start
    self.destination = destination
  
user = Train("Anuradha","Patna","Mumbai",1,"3AC")
print(f"Ticet booked for {user.name}, jouney start from {user.start} to {user.destination} and has book {user.noOfSeat} seats in {user.tier} tier")
user.getStatus(f"Number of seats available is {randint(1,100)}")
print(user.noOfSeat)
user.getFare("Bihar","Manali",2340)
print(f"Ticket fare from {user.start} to {user.destination} is Rs.{user.price}")

  
    