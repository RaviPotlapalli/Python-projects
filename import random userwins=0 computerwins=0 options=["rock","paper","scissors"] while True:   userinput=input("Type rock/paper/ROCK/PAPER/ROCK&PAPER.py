import random
userwins=0
computerwins=0
options=["rock","paper","scissors"]
while True:
  userinput=input("Type rock/paper/scissors or Q to quit").lower()
  if userinput=="q":
    break
  if userinput not in options:
    continue
  randominput=random.randint(0,2)
  computerinput=options[randominput]
  print(computerinput)

  if userinput=="rock" and computerinput=="scissors":
    print("you won!")
    userwins+=1

  elif userinput=="paper" and computerinput=="rock":
    print("you won!")
    userwins+=1
  elif userinput=="scissors" and computerinput=="paper":
    print("you won!")
    userwins+=1
  else:
    print("you lost")
    computerwins+=1
print("you won",userwins,"times.")
print("computer won",computerwins,"times.")
print("goodbye!")
