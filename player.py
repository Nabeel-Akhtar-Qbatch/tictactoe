class player:
    "Player Class"
    def __init__(self,PName = 'NoPlayer',TotalWins = 0,TotalLoss = 0):
        self.PName = PName
        self.TotalWins = TotalWins
        self.TotalLoss = TotalLoss


    def decoratorofPlayer(func):
        def inner(self):
            print("\n","*" * 10,"Player Detail","*" * 10)
            func(self)
        return inner

    #Display Player Info
    @decoratorofPlayer
    def Player_info (self):
        print("\nPlayer Name: ",self.PName)
        print("\nTotal Wins: ",self.TotalWins)
        print("\nTotal Loss: ",self.TotalLoss)


        