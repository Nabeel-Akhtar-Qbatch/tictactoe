from player import player
from writeOnFile import AddPlayer1,AddPlayer2

#reading player 1 and player 2 data from files
try:
    f1 = open("Player1.txt","r")
    f1_data = f1.read().splitlines()

    f2 = open("Player2.txt","r")
    f2_data = f2.read().splitlines()

    # print(f1_data,"\n")       
    # print(f2_data,"\n")
except:
    print("Files can't be open")
finally:
    f1.close()
    f2.close()

#Filtering Required data from List
Obj_P1 = list(map (lambda sub_list: sub_list.split(': ').pop(),f1_data))
Obj_P2 = list(map (lambda sub_list: sub_list.split(': ').pop(),f2_data))

#Creating Player1 and Player2
Player1 = player(Obj_P1[0],int(Obj_P1[1]),int(Obj_P1[2]))
Player2 = player(Obj_P2[0],int(Obj_P2[1]),int(Obj_P2[2]))

#Player Details
def Player_Detail(a):
    a = int (a)
    if a == 1: Player1.Player_info()
    elif a == 2: Player2.Player_info()
    else: print("Invalid Player/ No Record Found!")

#Add New Player 
def AddNewPlayer(p):
    p = int(p)
    name = input("\nName: ")
    Twin = input("\nTotal Wins: ")
    Tloss = input("\nTotal Loss: ")
    if p == 1:
        AddPlayer1(name,Twin,Tloss)
    elif p == 2:
        AddPlayer2(name,Twin,Tloss)
    else:
        print("\n!!!Wrong Selection!!!\n")
        return

    








