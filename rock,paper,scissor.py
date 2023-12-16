import random
user_choice=int(input("enter the number between 0 to 2 .0 for rock,1 for scissors,2 for paper : "))
print("your choice is ",user_choice)
if user_choice>2 or user_choice<0:
    print("invalid input")
if user_choice<=2 and user_choice>=0:
    computer_choice=random.randint(0,2)
    print("computer choice is : ",computer_choice)
if user_choice ==computer_choice:
    print("its draw")
elif user_choice==0 and computer_choice==1:
    print("user wins")
elif user_choice==1 and computer_choice==0:
    print("computer  wins")
elif user_choice==0 and computer_choice==2:
    print("user wins")
elif user_choice==2 and computer_choice==0:
    print("computer  wins")
elif user_choice==0 and computer_choice==2:
    print("user wins")
elif user_choice==1 and computer_choice==2:
    print("user wins")
elif user_choice==2 and computer_choice==1:
    print("computer wins")