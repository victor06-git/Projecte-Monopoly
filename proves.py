def create_board(rows, cols):
    board = []
    for row in range(rows):
        board.append([" " for _ in range(cols)])
    return board


def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print()


def add_piece(board, row, col, piece):
    board[row][col] = piece





def main():
    rows = 6
    cols = 8
    board = create_board(rows, cols)

    # Add your pieces here, make sure to only add them on valid locations.
    add_piece(board, 0, 0, "Parking")
    add_piece(board, 0, 1, "Urqinoa")
    add_piece(board, 0, 2, "Fontan")
    add_piece(board, 0, 3, "Sort")
    add_piece(board, 0, 4, "Rambles")
    add_piece(board, 0, 5, "Pl. Cat")
    add_piece(board, 0, 6, "Anr pró")
    add_piece(board, 1, 0, "Aragó")
    add_piece(board, 2, 0, "S. Joan")
    add_piece(board, 3, 0, "Caixa")
    add_piece(board, 4, 0, "Aribau")
    add_piece(board, 5, 0, "Muntan")
    add_piece(board, 1, 7, "Angel")
    add_piece(board, 2, 7, "Augusta")
    add_piece(board, 3, 7, "Caixa")
    add_piece(board, 4, 7, "Balmes")
    add_piece(board, 5, 7, "Gracia")
    #add_piece(board, 7, 7, "sortida")
    print_board(board)

main()
