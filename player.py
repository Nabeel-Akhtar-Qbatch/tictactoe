class Player:
    "Player Class"
    def __init__(self, player_name='NoPlayer', total_win=0, total_loss=0):
        self.player_name = player_name
        self.total_win = total_win
        self.total_loss = total_loss

    def player_detail_decorator(func):
        def inner(self):
            print("\n","*" * 10,"Player Detail","*" * 10)
            func(self)
        return inner

    #Display Player Info
    @player_detail_decorator
    def player_info(self):
        print("\nPlayer Name: ", self.player_name)
        print("\nTotal Wins: ", self.total_win)
        print("\nTotal Loss: ", self.total_loss)


