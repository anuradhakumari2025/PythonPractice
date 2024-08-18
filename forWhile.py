# n=4
# for i in range(1,11):
#   # n = n * i
#   # print(n) #this will not print table and give output as 4 8 24 480 2880 ...
#   print(f"{n} x {i} = {n*i}")
  
#greet hello whose name start with L
# list = ["Lakhan","Rani","Lalbabu","Lohit"]
# for name in list:
#   if(name.startswith("L")):
#     print(f"Hello {name}")

# i=1
# n=int(input("Enter a number to print its table: "))
# while(i<11):
#   print(f"{n} x {i} = {n*i}")
#   i +=1

#check for prime
# n = int(input("Enter a number to check for prime: "))
# for i in range(2,n):
#   if(n%i) == 0:
#     print("The num is not prime")
#     break
# else:
#   print("The num is prime")

# n = int(input("Enter num of which you want to print star pattern: "))
# for i in range(1,n+1):
#   print("" * (n-i),end="")
#   print("*" *  (2*i -1),end="")
#   print("")

# n = int(input("Enter num of which you want to print star pattern: "))
# for i in range(1,n+1):
#   print("*" *  (i),end="")
#   print("")

# n = int(input("Enter num of which you want to print star pattern: "))
# for i in range(1,n+1):
#   if(i==1 or i==n):
#       print("*" *n,end="")
#       print("")
#   else:
#     print("*",end="")
#     print(" "*(n-2),end="")
#     print("*",end="")
#     print("")
    
 

i=10
n=int(input("Enter num which you want multiplication table:"))
while(i>0):
  print(f"{n} x {i} = {n*i}")
  i-=1
  