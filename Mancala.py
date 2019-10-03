'''
Mini 4
Javier Jo 14343
Pablo Lopez

'''

class Mancala:


    def __init__(self):
        self.tablero = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        self.turno_jugador = 1
        self.jugada_inicial = None


    def jugada(self,posicion_de_jugada):
        stack_de_piezas = self.tablero[posicion_de_jugada]
        self.tablero[posicion_de_jugada] = 0
        ultimo_turno = self.distribucion(stack_de_piezas,posicion_de_jugada)
        self.reglas_especiales(ultimo_turno)
        self.cambio_de_turno()


    def distribucion(self, stack, posicion_obtenido):
        posicion_ahora = 0
        while stack > 0:
            posicion_obtenido += 1

            if (posicion_ahora+posicion_obtenido) >= len(self.tablero):
                posicion_ahora -= 14
            if self.turno_jugador == 1 and (posicion_ahora+posicion_obtenido) != 13:
                self.tablero[posicion_ahora+posicion_obtenido] += 1
                stack -= 1

            if self.turno_jugador == 2 and (posicion_ahora+posicion_obtenido) != 6:
                self.tablero[posicion_ahora+posicion_obtenido] += 1
                stack -= 1

        ultima_piedra = (posicion_ahora+posicion_obtenido)
        return ultima_piedra

    def posibles_jugadas(self):

        jugadas_posibles = []
        if self.turno_jugador == 1:
            jugadas_posibles = [0,1,2,3,4,5]
        else:
            jugadas_posibles = [7,8,9,10,11,12]
        elements_to_delete = []
        for x in jugadas_posibles:
            if self.tablero[x] == 0:
                elements_to_delete.append(x)
        
        for x in elements_to_delete:
            jugadas_posibles.remove(x)

        return jugadas_posibles


    def reglas_especiales(self, posicion_final):

        # Jugador 1
        if self.turno_jugador == 1: 
            if posicion_final == 6:
                self.cambio_de_turno()
            elif self.tablero[posicion_final] == 1:
                self.tablero[posicion_final] = 0
                self.tablero[6] += 1
                self.tablero[6] += self.tablero[12-posicion_final]
                self.tablero[12-posicion_final] = 0
        # Jugador 2
        else:
            if posicion_final == 13:
                self.cambio_de_turno()
            elif self.tablero[posicion_final] == 1:
                self.tablero[posicion_final] = 0
                self.tablero[13] += 1
                self.tablero[13] += self.tablero[12-posicion_final]
                self.tablero[12-posicion_final] = 0



    def cambio_de_turno(self):
        next_player = self.turno_jugador % 2
        self.turno_jugador = next_player + 1



    def get_ganador(self, end=False):
        jugador_1 = sum(self.tablero[0:7])
        jugador_2 = sum(self.tablero[7:14])
        if end:
            print('Puntaje del jugado: {}'.format(jugador_2))
            print('Puntaje del AI: {}'.format(jugador_1))

        if (jugador_1 > jugador_2):
            return 1
        elif(jugador_1 < jugador_2):
            return 2
        else:
            return 0


    def get_primera_jugada(self):
        return self.jugada_inicial


    def set_primera_jugada(self, jugada_1):
        self.jugada_inicial = jugada_1

    def print_tablero(self):
        return self.tablero

    def __str__(self):
        tabl_reverse = self.tablero[::-1]
        tablero_en_string = " " + str(tabl_reverse[8:]) + "\n"
        tablero_en_string += str(self.tablero[6])+ "                  "+ str(self.tablero[13]) + "\n"
        tablero_en_string += " " + str(self.tablero[7:13])
        return tablero_en_string