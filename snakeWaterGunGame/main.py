import random
'''
Game Rules:
Snake vs. Water: Snake drinks water, so Snake wins.
Water vs. Gun: Gun sinks in water, so Water wins.
Gun vs. Snake: Gun shoots the snake, so Gun wins.
'''
user=int(input("Enter 1 for snake ,-1 for water, 0 for gun: "))
comp = random.choice([-1,0,1])
print(f"You choose {user}\ncomp choose {comp}")
if(comp == user):
  print("Match Draw!!")
else:
  if(user == 1 and comp == -1):
    print("user win")
  elif(user == 0 and comp == -1):
      print("comp win")
  elif(user == 0 and comp == 1):
    print("user win")
  elif(user == -1 and comp == 1):
    print("comp win")
  elif(user == -1 and comp == 0):
    print("user win")
  elif(user == 1 and comp == 0):
    print("comp win")
  else:
    print("Something went wrong")
