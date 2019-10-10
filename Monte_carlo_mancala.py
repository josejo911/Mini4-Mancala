from Mancala import Mancala
import random
import copy


class Monte_carlo_mancala:
    def __init__(self, n=100):
        self.num_juegos_que_jugar = n # numero de juegos que hace el monte carlo
        self.juego_mancala = Mancala()

    def gameOver(self):
        ganador = self.juego_mancala.get_ganador(end=True)
        if ganador == 1:
            print('AI Winner')
        elif ganador == 0:
            print('Empate')
        else:
            print('Player One Wins')
        exit(0)
    
    def empezar_juego(self):
        juego_termino = False
        resultados_de_juegos = [0,0,0,0,0,0]
        while not juego_termino:
            for num_de_partida in range(self.num_juegos_que_jugar):
                copyActualGame = copy.deepcopy(self.juego_mancala)
                posibleMove  = copyActualGame.posibleMove()
                if posibleMove == []:
                    self.gameOver()
                frstMove = random.choice(posibleMove)
                copyActualGame.jugada(frstMove)
                while True:
                    posibleMove = copyActualGame.posibleMove()
                    if (posibleMove == []):
                        break
                    copyActualGame.jugada(random.choice(posibleMove))

                if copyActualGame.get_ganador() == 1:
                    resultados_de_juegos[frstMove] += 1

            while self.juego_mancala.plyrTurn == 1:
                movida = resultados_de_juegos.index(max(resultados_de_juegos))
                self.juego_mancala.jugada(movida)
                print('AI Moves {}'.format(movida))

            while self.juego_mancala.plyrTurn == 2:
                print(self.juego_mancala)
                posibleMove = self.juego_mancala.posibleMove()
                if posibleMove == []:
                    self.gameOver()
                    print('Game Over')
                
                for number in range(len(posibleMove)):
                    posibleMove[number] -= 6

                print('Posible moves are: {}'.format(posibleMove))
                movida_player = input()

                if int(movida_player) not in posibleMove:
                    while True:
                        print('Bro... thats not a move ')
                        movida_player = input()
                        if int(movida_player) in posibleMove:
                            break
                
                self.juego_mancala.jugada(int(movida_player)+6)

            print(self.juego_mancala)
            
          
            

juego = Monte_carlo_mancala()
juego.empezar_juego()