from readwrite_onfile import player_one, player_two, player_detail, add_new_player
from menu import menu_selection
from game_board import the_board, board_keys, print_board
from write_onfile import write_board
from result_check import detail_check
from datetime import datetime

def game():

    try: 
        file = open("record.txt", "a")
    except:
         print("File not available\nThis game will not be recorded")
    dt =datetime.now()
    players = f"\n{player_one.player_name}(X) vs {player_two.player_name}(O)  {dt}"
    print(players)
    file.write(players)
    file.close()
    turn = 'X'
    count = 0


    for i in range(10):
        try: 
            file = open("record.txt", "a")
        except:
             print("File not available\nThis game will not be recorded")
        print_board(the_board)
        write_board(the_board)
        if turn == 'X': 
            print("It's your turn," +player_one.player_name+ "("+ turn + ").Move to which place?")
            move = input()
            move = str(move)

        else:
            print("It's your turn," +player_two.player_name+ "("+ turn + ").Move to which place?")
            move = str(input())

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            retruned_result = detail_check(turn)
            if retruned_result == True:
                break
        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            write_board(the_board)
            gametie = f"\n Game Over\nIt's a Tie"
            file.write(gametie)
            file.close()

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
        
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    restart = str(restart)
    if restart == "y" or restart == "Y": 
        for key in board_keys:
            the_board[key] = " "
        game()
    

def game_play():
    
    selection = menu_selection()

    if selection == 1:
        game()
    elif selection == 2:
        print("\nSelect Player to Add\n1. Player1\n2. Player2")
        p = input("Please Enter: ")
        add_new_player(p)
        game_play()
    elif selection == 3:
        print("\nPlease Select\n1. Player1\n2. Player2\n")
        a = input("Please Enter: ")
        player_detail(a)
        print ("\nPlayer Info is updated")
        game_play()
