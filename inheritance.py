# class Employee:
#   a = 1
#   def __init__(self):
#     print("Employee class constructor")
# class Programmer(Employee):
#   b=2
#   def __init__(self):
#     print("Programmer class constructor")
# class Manager(Programmer):
#   c=3
#   def __init__(self):
#     super().__init__()
#     print("Manager class constructor")

# o = Employee()
# print(o.a)
# o = Programmer()
# print(o.b)
# o=Manager()
# print(o.a,o.b)
# print(o.c)

# class Student:
#   a=1

#   @classmethod
#   def show(cls):
#     print(f"The class attribute of a is {cls.a}")

#   @property
#   def name (self):
#     return f"{self.fname} {self.lname}"
  
#   @name.setter
#   def name (self,value):
#     self.fname = value.split(" ")[0]
#     self.lname = value.split(" ")[1]

# o = Student()
# o.name = "Anuradha Kumari"
# print(o.name)
# print(o.fname,o.lname)
# o.show()
# print(f"The class attribute of a before assigning a new value to a {o.a}")
# a = 45
# print(f"The class attribute of a after assigning a new value to a {o.a}")
# print("The value not change because of use of classmethod")

class Vector:
  def __init__(self,i,j,k):
    self.i = i
    self.j=j
    self.k=k
  def __add__(self,other):
    result = Vector(self.i + other.i,self.j+other.j,self.k+other.k)
    return result
  def __mul__(self,other):
    result = self.i * other.i + self.j*other.j + self.k*other.k
    return result
  def __str__(self):
    return  f"Vector is ({self.i}i,{self.j}j,{self.k}k)"
  
#__add__: Adds two vectors component-wise and returns a new Vector.
#__str__: Provides a string representation of the Vector.
  
#Test the implementation
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3=Vector(7,8,9)
print(v1 + v2)
print(v1*v2)



