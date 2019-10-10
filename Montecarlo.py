from Rules import Rules
import random
import copy


class Montecarlo:
    def __init__(self, n=1000):
        self.iterations = n
        self.game = Rules()

    def gameOver(self):
        winner = self.game.get_winner(end=True)
        if winner == 1:
            print('AI Winner')
        elif winner == 0:
            print('The game ends in Tie')
        else:
            print('Player One Wins')
        exit(0)
    
    def start(self):
        finish = False
        results = [0,0,0,0,0,0]
        while not finish:
            for i in range(self.iterations):
                copyActualGame = copy.deepcopy(self.game)
                posibleMove  = copyActualGame.posibleMove()
                if posibleMove == []:
                    self.gameOver()
                frstMove = random.choice(posibleMove)
                copyActualGame.play(frstMove)
                while True:
                    posibleMove = copyActualGame.posibleMove()
                    if (posibleMove == []):
                        break
                    copyActualGame.play(random.choice(posibleMove))

                if copyActualGame.get_winner() == 1:
                    results[frstMove] += 1

            while self.game.plyrTurn == 1:
                moves = results.index(max(results))
                self.game.play(moves)
                print('AI Moves {}'.format(moves))

            while self.game.plyrTurn == 2:
                print(self.game)
                posibleMove = self.game.posibleMove()
                if posibleMove == []:
                    self.gameOver()
                    print('Game Over')
                
                for number in range(len(posibleMove)):
                    posibleMove[number] -= 6

                print('Posible moves are: {}'.format(posibleMove))
                player2moves = input()

                if int(player2moves) not in posibleMove:
                    while True:
                        print('Bro... thats not a move ')
                        player2moves = input()
                        if int(player2moves) in posibleMove:
                            break
                
                self.game.play(int(player2moves)+6)

            print(self.game)
            
juego = Montecarlo()
juego.start()