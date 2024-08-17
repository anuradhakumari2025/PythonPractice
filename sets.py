s = {1,2,4} #set
e = set() #empty set as s = {} will be an empty dict
print(s)

a = {1,5,"love", "prem",4}
print(a,type(a),type(s))

a.remove("anu")#throw error as it is not in set(a)
a.discard("anu")#do nothing

s1={3,45,6,7,1}
s2={3,7,5,23,7}
print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1.union(s,s2))

# print unique no taken from user
s = set()
a = int(input("Enter no. 1: "))
s.add(a)
b = int(input("Enter no 2: "))
s.add(b)
c = int(input("Enter no 3: "))
s.add(c)
d=int(input("Enter no 4: "))
s.add(d)
e = int(input("Enter no 5: "))
s.add(e)
print(s)#if any number user give more than one time then set will only print it one time

s = {18,"18"}
print(s)
print(len(s))

s = {"2",2,2.0}
print(s)
print(len(s))# output is 2 because 2 == 2.0 returns true. i.e. python treats value of 2 and 2.0 as equal and not as integer and float two different value


#change value inside list given in a set
s = {1,5,"love","pyar",[5,6,7,8]}
print(s)#type error as set dont accept list as a
