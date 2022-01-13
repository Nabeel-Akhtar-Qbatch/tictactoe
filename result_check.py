from game_board import the_board, print_board
from write_onfile import write_board

def check(func):
    def inner(turn):
        print(turn)
        if the_board['7'] == the_board['8'] == the_board['9'] != ' ': # across the top
            return func(turn)
        elif the_board['4'] == the_board['5'] == the_board['6'] != ' ': # across the middle
            return func(turn)
        elif the_board['1'] == the_board['2'] == the_board['3'] != ' ': # across the bottom
            return func(turn)
        elif the_board['1'] == the_board['4'] == the_board['7'] != ' ': # down the left side
            return func(turn)
        elif the_board['2'] == the_board['5'] == the_board['8'] != ' ': # down the middle
            return func(turn)
        elif the_board['3'] == the_board['6'] == the_board['9'] != ' ': # down the right side
            return func(turn)
        elif the_board['7'] == the_board['5'] == the_board['3'] != ' ': # diagonal
            return func(turn)
        elif the_board['1'] == the_board['5'] == the_board['9'] != ' ': # diagonal
            return func(turn)
    return inner


@check
def detail_check(turn):
    try: 
        file = open("record.txt", "a")
    except:
        print("File not available\nThis game will not be recorded")
    print_board(the_board)
    print("\nGame Over.\n")                
    print(" **** " + turn + " won. ****")
    write_board(the_board) 
    playerwon = f" **** ({turn}) won. ****"
    file.write(playerwon)
    file.close()
    return True
