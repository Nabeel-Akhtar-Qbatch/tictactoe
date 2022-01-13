#Implementing Decorators to print Tic Tac Toe Game Headline/Title
def star (func):    
    def inner():
        print("*" * 35)
        func()
        print("*" * 35)
    return inner

def percent (func):
    def inner():
        print("%" * 35)
        func()
        print("%" * 35)
    return inner

@star
@percent
def splash_printer():
    print ("\tTic Tac Toe Game")

#Main Menu
def main_menu(func):
    def inner():
        print("\nSelect\n1. Play\n2. Add New Player\n3. Players Detail")
        return func()
    return inner

@main_menu
def menu_selection():
    sel = input("\nPlease Enter:")
    return int (sel)








