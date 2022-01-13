from game_board import the_board

#Appending Complete game record between Player1 and Player2 on File (record.txt)
def write_board(board):
    line1 = str(board['7'] + '|' + board['8'] + '|' + board['9'])
    line2 = '-+-+-'
    line3 = str(board['4'] + '|' + board['5'] + '|' + board['6'])
    line4 = str(board['1'] + '|' + board['2'] + '|' + board['3'])
    mainline = f"\n{line1}\n{line2}\n{line3}\n{line2}\n{line4}\n"
    try:
        file = open("record.txt","a")
        file.write(mainline)

    except:
        print("File not available\nThis game will not be recorded")

#Adding New Player in Player Files 
#Player1.txt
def add_player_one(name,win,loss):
    try:
        file_player_one = open("Player1.txt","w")
        update_player = f"Name: {name}\nTotalWins: {win}\nTotalLoss: {loss}"
        file_player_one.write(update_player)
    except:
        print("Player1 Can't Open\n New Player record is not saved")

#Player2.txt
def add_player_two(name,win,loss):
    try:
        file_player_two = open("Player2.txt","w")
        update_player = f"Name: {name}\nTotalWins: {win}\nTotalLoss: {loss}"
        file_player_two.write(update_player)
    except:
        print("Player1 Can't Open\n New Player record is not saved")