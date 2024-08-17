
friends = ["apple",6,56.0,"allah"] #list
print(friends[3])
a = "Anuradha"#string
print(a)

# a[4] ="p"#throw error because string is immutable
friends[3] ="god" #list is mutable
# print(a)
print(friends) 

print(a.endswith("Rani"))#tell whether it is right or not
print(a)

friends.append("banana")
friends.insert(2,555234)
print(friends)

li=[3,5,8,8,99,123,63,0]
# li.sort()
# li.reverse()
li.remove(99)
li.remove(li[5])
print(li)



#take input from user and store as a list
f1 = input("Enter fruit name ")
f2=input("Enter other fruit name")
f3=input("Enter animal name ")
f4=input("Enter your name")
fruits = []
fruits.append(f1)
fruits.append(f2)
fruits.append(f3)
fruits.append(f4)
print(fruits)



#add numbers in list
li=[1,2,3,4]
sum = li[0]+li[1]+li[2]+li[3]
print(sum)
print(sum(li))

