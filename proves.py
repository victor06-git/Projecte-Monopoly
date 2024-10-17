def create_board(rows, cols):#Funció que crear el tauler
    board = [] #Llista taula
    for row in range(rows):
        board.append([" " for _ in range(cols)])#Afegeix espais per columna
    return board#Retorna la llista