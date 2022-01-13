from ReadingPlayerData import Player1,Player2,Player_Detail,AddNewPlayer
from menu import menu_selection
from gameBoard import theBoard, board_keys, printBoard
from writeOnFile import writeBoard
from datetime import datetime

def game():

    try: 
        file = open("record.txt","a")
    except:
         print("File not available\nThis game will not be recorded")
    dt =datetime.now()
    print(Player1.PName, "(X) vs ", Player2.PName,"(O)")
    players = f"\n{Player1.PName}(X) vs {Player2.PName}(O)  {dt}"
    file.write(players)
    file.close()
    turn = 'X'
    count = 0


    for i in range(10):
        try: 
            file = open("record.txt","a")
        except:
             print("File not available\nThis game will not be recorded")
        printBoard(theBoard)
        writeBoard(theBoard)
        if turn == 'X': 
            print("It's your turn," +Player1.PName+ "("+turn + ").Move to which place?")
            move = input()
            move = str(move)

        else:
            print("It's your turn," +Player2.PName+ "("+turn + ").Move to which place?")
            move = input()
            move = str(move)

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard) 
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard)
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard)
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard)
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard)
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard)
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard)
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                writeBoard(theBoard)
                playerwon = f" **** ({turn}) won. ****"
                file.write(playerwon)
                file.close()
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            writeBoard(theBoard)
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
            theBoard[key] = " "
        game()
    

def gamePlay():
    
    selection = menu_selection()

    if selection == 1:
        game()
    elif selection == 2:
        print("\nSelect Player to Add\n1. Player1\n2. Player2")
        p = input("Please Enter: ")
        AddNewPlayer(p)
        gamePlay()
    elif selection == 3:
        print("\nPlease Select\n1. Player1\n2. Player2\n")
        a = input("Please Enter: ")
        Player_Detail(a)
        gamePlay()

