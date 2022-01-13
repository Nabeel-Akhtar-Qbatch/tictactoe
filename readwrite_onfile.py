from player import Player
from write_onfile import add_player_one, add_player_two

#reading player 1 and player 2 data from files
try:
    file_player_one = open("Player1.txt","r")
    file_player_one_data = file_player_one.read().splitlines()

    file_player_two = open("Player2.txt","r")
    file_player_two_data = file_player_two.read().splitlines()

    # print(file_player_one_data,"\n")       
    # print(file_player_two_data,"\n")
except:
    print("Files can't be open")
finally:
    file_player_one.close()
    file_player_two.close()

#Filtering Required data from List
player_one_data = list(map(lambda sub_list: sub_list.split(': ').pop(),file_player_one_data))
player_two_data = list(map(lambda sub_list: sub_list.split(': ').pop(),file_player_two_data))

#Creating Player1 and Player2
player_one = Player(player_one_data[0],int(player_one_data[1]),int(player_one_data[2]))
player_two = Player(player_two_data[0],int(player_two_data[1]),int(player_two_data[2]))

#Player Details
def player_detail(a):
    a = int (a)
    if a == 1: player_one.player_info()
    elif a == 2: player_two.player_info()
    else: print("Invalid Player/ No Record Found!")

#Add New Player 
def add_new_player(p):
    p = int(p)
    name = input("\nName: ")
    t_win = input("\nTotal Wins: ")
    t_loss = input("\nTotal Loss: ")
    if p == 1:
        add_player_one(name, t_win, t_loss)
    elif p == 2:
        add_player_two(name, t_win, t_loss)
    else:
        print("\n!!!Wrong Selection!!!\n")
        return

