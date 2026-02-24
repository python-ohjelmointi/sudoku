teksti = "merkkijono"
pituus = len(teksti)

alku = pituus - 1
loppu = pituus

while alku >= 0:
    print(teksti[alku:loppu])
    alku -= 1
