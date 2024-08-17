marks={
  "Rohans" : 56,
  "Ashu" : 59,
  "Naina" : 61,
  "list" : [1,3,2,4,5]
}
print(marks,type(marks))
print(marks[0])#throw type error
print(marks["Naina"])
print(marks["list"])
print(marks.values())
marks.update({"Rohans" : 54})  #dictionary is muttable
print(marks)

print(marks.get("Naina")) 
print(marks["Naina"])

print(marks.get("Naina2")) #returns none
print(marks["Naina2"]) #throw error

d = {}#empty dict

#user will know the meaning in english
words = {
  "pyar" : "love",
  "nafrat" : "hate",
  "gussa" : "hate"
}

word = input("Enter word you want to the meaning of ")
print(words[word])

#take key as a name from friend and value as their language
dict = {}
a = input("Enter your name: ")
b = input("Enter your language : ")
dict.update({a:b})
c = input("Enter your name: ")
d = input("Enter your language: ")
dict.update({c:d})
print(dict)#if name of both is same then last value will be printed with that name as a key
