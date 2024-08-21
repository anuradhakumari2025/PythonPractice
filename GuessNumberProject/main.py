import random
n = random.randint(1,50)
guesses = 0
a=-1
while(a != n):
  a = int(input("Enter the number to guess right number: "))
  if(a>n):
    guesses +=1
    print("Please guess lower number")
  else:
    guesses +=1
    print("Please guess higher number")

print(f"You have guess the num {n} in {guesses} guess")