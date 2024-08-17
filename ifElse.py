# a = int(input("Enter your age: "))

# if(a%2 == 0):
#   print("The number  is even")
# if(a>=18):
#   print("You can vote")
#   print("Its your duty to vote")
# elif(a<0):
#   print("Age can't be negative!!")
# else:
#   print("You can play")

# if(a%2 != 0):
#   print("The number  is odd")

# print("Perform your duty")

#find greatest of four no.
# a= int (input("Enter number 1: "))
# b= int (input("Enter number 2: "))
# c= int (input("Enter number 3: "))
# d= int (input("Enter number 4: "))
# if(a>b and a>c and a>d):
#   print(str(a)+ " is the largest number") 
# elif(b>a and b>c and b>d):
#   print(str(b)+ "  is the largest no")
# elif(c>a and c>b and c>d):
#   print(str(c)+ " is the largest number")
# else:
#   print(d," is the largest number")

#33% is required to pass in individual subject and 40% is required to pass as a total
# a = int(input("Enter marks of subject 1: "))
# b = int(input("Enter marks of subject 2: "))
# c = int(input("Enter marks of subject 3: "))
# # percentOf_a = int((a/100)*100)
# # percentOf_b = int((b/100)*100)
# # percentOf_c = int((c/100)*100)
# totalPercent =int(((a+b+c)/300)*100)
# if(a >= 33 and b >= 33 and c >= 33 and totalPercent >= 40):
#   print("You have passed",totalPercent)
# else:
#   print("You have failed in exam",totalPercent)

# p1="hate"
# p2="anger"
# p3="sad"
# p4="illegal"
# msg = input("Enter some beautiful message for me: ")
# # the 'in' keyword is used to check if a value exists within a sequence or a collection, such as a string, list, tuple, dictionary, or set. It returns True if the value is found and False if it's not.
# if((p1 in msg ) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
#   print("You are a believable human on earth")
# else:
#   print("You can cheat me")

#check whether char len is less than 10 or not
# char = input("Enter a word: ")
# if(len(char) <10):
#   print("Length of word is less than 10")
# else:
#   print("Length of word is greater than 10")

post = input("Enter post : ")
if("Anuradha".lower() in post.lower()):
  print("You are talking about anuradha")
else:
  print("Yoou are not talking about anuradha")
