a = (1,2,3,4,5)#tuple
print(type(a)) 
c=(1)#this will not be a tuple ,it will be integer
print(type(c))
b=(1,)#tuple having one element
print(type(b))

d=("the",56,"good",56.7)
print(d)

# d[2] = "god"#tuple is immutable
print(d)
print(a+d)