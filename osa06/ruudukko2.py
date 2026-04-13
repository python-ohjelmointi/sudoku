"""
Tässä esimerkissä rivit ovat uniikkeja.

Ongelmana on vain se, että vain 1 % tämän pelilaudan ruuduista
sisältää oikeasti tärkeää dataa.
"""

# listan muodostaja on yksinkertaisempi tapa luoda lista, jossa on toistoa
ruudukko = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]

ruudukko[1][1] = 8

print(*ruudukko, sep="\n")
