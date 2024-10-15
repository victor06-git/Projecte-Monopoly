def line():
    for _ in range(7):
        print("+--------", end="")
    print("+")

def print_row(cells):
    for cell in cells:
        print(f"|{cell:<7} ", end="")
    print("|")

def dibuixar_tauler():
    line()
    cells1_7 = ["Parking","Urqinoa","Fontan","Sort","Rambles","Pl. Cat","Anr pró"]
    print_row(cells1_7)
    print_row([""] * 7)  # empty row
    line()
    cells_finals = ["Presó","Consell","Marina","Sort","Rosell","Lauria","Sortida"]
    print_row(cells_finals)
    print_row([""] * 7)  # empty row
    line()

dibuixar_tauler()