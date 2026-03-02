"""
Pythonin listojen käsittely muistuttaa surresti merkkijonojen käsittelyä,
sekä muita sekvenssityyppejä.

https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""

jono = ["ma", "ti", "ke", "to", "pe", "la", "su"]  # "maanantai"

# osataan katsoa pituus
print("pituus:", len(jono))

# osataan ottaa yksittäisiä arvoja
print("eka:", jono[0])
print("vika:", jono[-1])

# osataan katsoa osajonoja
print("pari ekaa:", jono[0:2])
print("pari seuraavaa:", jono[2:4])


# toisin kuin merkkijonoja, listoja voidaan muuttaa
jono[0] = "MA"

print(jono)

jono.insert(1, "TI")

print(jono)

# del-operaattori poistaa tietystä _indeksistä_
poistettu = jono.pop(2)

# remove poistaa tietyn arvon
jono.remove("su")

print(jono)

jono.append("SU")

print(jono)

print("poistettu:", poistettu)
