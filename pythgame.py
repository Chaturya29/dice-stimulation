print("Welcome to our gaming world!!")
name=input("What is your sweet name? ")
age=int(input("What is your age? "))
print("Hello",name,"you are",age,"years old")
lives = 10
print("You are starting with",lives,"lives")
if age>=18:
  print("You are old enough",name,"!!")
  wants_to_play=input("Do you want to play game ?").lower()
  if wants_to_play=="yes":
    print("Let's play",name)
    left_or_right=input("Enter your first choice...Left or Right(Left/Right)?").lower()
    if left_or_right=="left":
      ans=input("Nice,You will follow the path and reach a lake...Do you swim accross or go around(accross/around) ?")
      if ans=="around":
        print("You went around and reached the other side of lake!!")
      elif ans=="accross":
        print("You managed to get accross,but you were bite by a fish and lost lives")
        lives-=5
      hmm=input("You noticed a house and river,Which one would you like to visit(house/river)??").lower()
      if hmm=="house":
        print("You visited the house and owner doesn't liked you....You have lost your one life")
        lives-=1
        if (lives<=0):
          print("You now have no lives to continue the game...")
        else:
          print("Hurray!!You have survived and you won the game!!!")
      else:
        print("You fell into the river and lost life :(")
    else:
        print("You lost :(")
    
else:
  print("You are not eligible to play :)")
  
