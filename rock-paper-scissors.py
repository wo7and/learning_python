from random import choice

class Game():
    
    def start(self):
        print(3*'-', 'Rock Paper Scissors Game', 3*'-')
        self.__rounds = int(input("How many rounds would you like to play? "))

    def rounds(self):
        self.h_points = 0
        self.c_points = 0
        for i in range(self.__rounds):
            human = input('Rock, paper or scissors [r/p/s]? ')
            computer = choice(['r', 'p', 's'])
            print('You:', human, '|', 'Computer', computer)
            if human == computer:
                print('This round is a tie.')
                continue
            elif human == 'r':
                if computer == 'p':
                    print('You lost this round!')
                    self.c_points += 1
                    continue
                else:
                    print('You won this round!')
                    self.h_points += 1
                    continue
            elif human == 'p':
                if computer == 's':
                    print('You lost this round!')
                    self.c_points += 1
                    continue
                else:
                    print('You won this round!')
                    self.h_points += 1
                    continue
            else:
                if computer == 'r':
                    print('You lost this round!')
                    self.c_points += 1
                    continue
                else:
                    print('You won this round!')
                    self.h_points += 1
                    continue
        return self.c_points, self.h_points
            
    def score(self):
        print('[Game Summary]', 'Your points:',self.h_points, 'Computer points:', self.c_points)
        if self.c_points > self.h_points:
            print('Computer won.')
        elif self.c_points < self.h_points:
            print('You won.')
        else:
            print('It was a tie.')
                

    

my_game = Game()
my_game.start()
my_game.rounds()
print()
my_game.score()
