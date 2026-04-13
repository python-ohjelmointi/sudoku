"""
Tässä esimerkissä tehdään sudoku-ruudukko sanakirjan avulla.
"""

sudoku = {}
sudoku[(1, 1)] = 8
sudoku[(3, 4)] = 5

print(sudoku.get((1, 1), 0))
print(sudoku.get((8, 8), 0))

for rivi in range(9):
    for sarake in range(9):
        solu = (rivi, sarake)
        print(sudoku.get(solu, 0), end=" ")
    print()

print()

print(sudoku)
print()
