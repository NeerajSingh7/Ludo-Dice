import random

# dice layout
dice =[" "," "," ",
       " "," "," ",
       " "," "," "]


# while loop for continuing program

playerwant= True
while playerwant:

    number= random.randint(1,6)
    if number == 1:
       dice[4]="o"
    elif number == 2:
       dice[3]="o"
       dice[5]="o"
    elif number == 3:
       dice[0]="o"
       dice[4]="o"
       dice[8]="o"
    elif number == 4:
       dice[0]="o"
       dice[2]="o"
       dice[6]="o"
       dice[8]="o"
    elif number == 5:
       dice[0]="o"
       dice[2]="o"           
       dice[4]="o"           
       dice[6]="o"           
       dice[8]="o"
    elif number == 6:
       dice[0]="o"
       dice[2]="o"
       dice[3]="o"
       dice[5]="o"
       dice[6]="o"
       dice[8]="o"

#printing the dice 
    print("-------")
    print("|"+dice[0]+" "+dice[1]+" "+dice[2]+"|")
    print("|"+dice[3]+" "+dice[4]+" "+dice[5]+"|")
    print("|"+dice[6]+" "+dice[7]+" "+dice[8]+"|")
    print("-------")

# Assigning empty values to indexes again
    dice[0]=" "
    dice[1]=" "
    dice[2]=" "
    dice[3]=" "
    dice[4]=" "
    dice[5]=" "
    dice[6]=" "
    dice[7]=" "
    dice[8]=" "


    print("do u want to roll again?   press 'y' to continue , 'n' to stop.")
    sign=input()
    if sign=='n':
           playerwant=False
