def create_board(rows, cols):#Funció que crear el tauler
    board = [] #Llista taula
    for row in range(rows):
        board.append([" " for _ in range(cols)])#Afegeix espais per columna
    return board#Retorna la llista


def print_board(board): #Imprimeix el tauler
    for row in board:#Per cada fila en el tauler
        print("|", end="")#Imprimeix "|" i les va afegint en linea 
        for cell in row:#Per cada cel·la en la fila
            print(cell, end="|")#Afegeix la cel·la i acaba amb "|"
        print()#Imprimeix un espai de línea


def add_piece(board, row, col, piece):#Funció afegir nom
    board[row][col] = piece #Defineix la variable piece com un caracter en la taula

def add_text(text):
    pass    





def main():#Funció principal (main)
    rows = 7#Filas
    cols = 7#Columnas
    board = create_board(rows, cols)#Crida la funció crear tauler

    
    
    caselles = ["Parking","Urqinoa", "Fontan", "Sort", "Rambles", "Pl. Cat", "Anr pró", "Aragó", "S.Joan","Caixa","Aribau","Muntan","Angel","Augusta","Caixa","Balmes","Gracia","Presó","Consell","Marina","Sort","Rosell","Lauria","Sortida"]
    
    #Afegeix els noms de les caselles
    add_piece(board, 0, 0, caselles[0])
    add_piece(board, 0, 1, caselles[1])
    add_piece(board, 0, 2, caselles[2])
    add_piece(board, 0, 3, caselles[3])
    add_piece(board, 0, 4, caselles[4])
    add_piece(board, 0, 5, caselles[5])
    add_piece(board, 0, 6, caselles[6])
    add_piece(board, 1, 0, caselles[7])
    add_piece(board, 2, 0, caselles[8])
    add_piece(board, 3, 0, caselles[9])
    add_piece(board, 4, 0, caselles[10])
    add_piece(board, 5, 0, caselles[11])
    add_piece(board, 1, 6, caselles[12])
    add_piece(board, 2, 6, caselles[13])
    add_piece(board, 3, 6, caselles[14])
    add_piece(board, 4, 6, caselles[15])
    add_piece(board, 5, 6, caselles[16])
    add_piece(board, 6, 0, caselles[17])
    add_piece(board, 6, 1, caselles[18])
    add_piece(board, 6, 2, caselles[19])
    add_piece(board, 6, 3, caselles[20])
    add_piece(board, 6, 4, caselles[21])
    add_piece(board, 6, 5, caselles[22])
    add_piece(board, 6, 6, caselles[23])
    print_board(board)

main()
