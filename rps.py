import random
print("Rules of the game Rock Paper Scissors are:\n"
      +"Rock vs. Paper>>Paper wins\n"
      +"Paper vs. Scissor>>Scissor wins\n"
      +"Scissor vs. Rock>>Rock wins")

print("Enter your choice:\n1.Rock\n2.Paper\n3.Scissor")

choice=int(input("Enter your choice"))

if choice==1:
    choice_name='Rock'
elif choice==2:
    choice_name='Paper'
elif choice==3:
    choice_name='Scissor'
else:
    print("Kindly choose a valid handsign")

print("You chose",choice_name)
print("now let me play :)......")
comp_choice=random.randint(1,3)

if comp_choice==1:
    comp_choice_name='Rock'
elif comp_choice==2:
    comp_choice_name="Paper"
else:
    comp_choice_name='Scissor'
    
print("I chose",comp_choice_name)
print("{0} vs {1}".format(choice_name,comp_choice_name))
if choice==comp_choice:
    print("It's a draw")
elif choice==1 and comp_choice==2:
    print("I win")
elif choice==2 and comp_choice==1:
    print("You won")
elif choice==2 and comp_choice==3:
    print("I win")
elif choice==3 and comp_choice==2:
    print("You won")
elif choice==1 and comp_choice==3:
    print("you won")
else:
    print("I won ")
        

    