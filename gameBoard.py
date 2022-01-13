
#Dictionary
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# def writeBoard(board):
#     line1 = str(board['7'] + '|' + board['8'] + '|' + board['9'])
#     line2 = '-+-+-'
#     line3 = str(board['4'] + '|' + board['5'] + '|' + board['6'])
#     line4 = str(board['1'] + '|' + board['2'] + '|' + board['3'])
#     mainline = f"\n{line1}\n{line2}\n{line3}\n{line2}\n{line4}"
#     return mainline



