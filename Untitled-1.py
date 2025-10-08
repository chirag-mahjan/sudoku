class snake_ladders():
    def __init__(self):
        self.snakes={14:6,25:13,37:24,49:4,53:38,61:33,70:27,77:63,88:44,97:29}
        self.ladders={4: 14, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.position=0
    def roll_dice(self):
        import random
        return random.randint(1,6)
    def move_player(self,steps):
        self.position=self.position+steps
        if self.position in self.snakes:
            self.position=self.snakes[self.position]
            print("oops! landed on snake.Go down to",self.position)
        elif self.position in self.ladders:
            self.position=self.ladders[self.position]
            print("Yay you got a ladder.move to",self.position)
    def play(self):
        while self.position<100:
            print(input("press enter to roll dice..."))
            steps=self.roll_dice()
            print("you rolled a",steps)
            self.move_player(steps)
            print("You are at",self.position)
        print("you won the game")

play=snake_ladders()
play.play()
