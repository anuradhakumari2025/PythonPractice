class Employee:
  language = "Python"
  salary = 100000
  @staticmethod
  def greet():
    print("Well done!!")
  
  def getInfo(self):
    print(f"The salary is {self.salary} and language is {self.language}")

harry=Employee()
harry.name =  "Anuradha"
harry.getInfo()
harry.greet()
print(harry.language)