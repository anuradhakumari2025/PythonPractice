# f = open("file.txt","r") #r means I want to read file
# data = f.read()
# print(data)
# f.close() #close file after using it as it is a best practice

#the above code can be written without use of close()
# with open("file.txt") as f:
#   print(f.read()) #here we don't have to explicitly close the file

#Write file
# str = "I am doing great!"
# f=open("file2.txt","w") #w means you can write in file
# f.write(str)
# f.close()

#function of files
# f = open("file.txt")
# lines = f.readlines()
# print(lines,type(lines))

# line1 = f.readline()
# print(line1,type(line1))
# line2 = f.readline()
# print(line2,type(line2))
# f.close()

#append lines
# str = "\nYou have to do it"
# f=open("file.txt","a")
# f.write(str)
# f.close()

#find whether a word is given in file
# with open("file.txt") as f:
#   if("genious"  in f.read()):
#     print("The word genious is present in file")
#   else:
#     print("The word genious is not present in file")

#practice set 9 question 1
# import random
# def game():
#   print("You are playing a game")
#   score = random.randint(1,70)
#   #fetch score from highscore
#   with open("hiscore.txt") as f:
#     hiscore = f.read()
#     if(hiscore != ""):
#       hiscore = int(hiscore)
#     else:
#       hiscore = 0
#   print(f"Your score is {score}")
#   if(score>hiscore):
#     #write this hiscore in the file
#     with open("hiscore.txt","w") as f:
#       f.write(str(score))
# game()

#program to write table of 9 to 19 in different files and store it in a folder
# def generateTable(n):
#   table = ""
#   for i in range(1,11):
#     table += f"{n} x {i} = {n*i}\n"
#   with open(f"tables/tableOf{n}.txt","w") as f:
#     f.write(table)
# for i in range(9,20):
#   generateTable(i)

#replace word with another word or symbol
# word = "amajon"
# with open("file2.txt") as f:
#   content = f.read()
#   newWord = content.replace(word,"$$$$$")
# with open("file2.txt","w") as f:
#   f.write(newWord)

#above code for list of words
# words = ["amajon","flipkart","walmart","tcsPrime"]
# with open("file2.txt") as f:
#   content = f.read()
# for word in words:
#   #newWord = content.replace(word,"$" * len(word)) 
#   '''
#   each time the loop runs, it assigns a new value to newWord, which is a modified version of the original content. However, you're only writing the result of the last replacement operation back to the file. As a result, only the last word in the list ("tcsPrime") gets replaced.
#   '''
#   content = content.replace(word,"$" * len(word)) 
# with open("file2.txt","w") as f:
#   f.write(content)

#wipe out content of file
with open("file3.txt","w") as f:
  f.write("")

#rename a file
with open("file2.txt") as f:
  content = f.read()
with open("file2_rename.txt","w") as f:
  f.write(content)


