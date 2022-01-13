from gameBoard import theBoard

#Appending Complete game record between Player1 and Player2 on File (record.txt)
def writeBoard(board):
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
def AddPlayer1(name,win,loss):
    try:
        FP1 = open("Player1.txt","w")
        updatePlayer = f"Name: {name}\nTotalWins: {win}\nTotalLoss: {loss}"
        FP1.write(updatePlayer)
    except:
        print("Player1 Can't Open\n New Player record is not saved")

#Player2.txt
def AddPlayer2(name,win,loss):
    try:
        FP2 = open("Player2.txt","w")
        updatePlayer = f"Name: {name}\nTotalWins: {win}\nTotalLoss: {loss}"
        FP2.write(updatePlayer)
    except:
        print("Player1 Can't Open\n New Player record is not saved")