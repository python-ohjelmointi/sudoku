"""
Tässä esimerkissä on tarkoitus vähän miettiä, mitä viittaukset oikein
tarkoittavat.
"""

# luodaan tietokoneen muistiin "olio"
rivi = [0, 0, 0, 0, 0, 0, 0, 0, 0]
rivi[1] = 8

print(rivi)
print()

# laitetaan *sama* olio yhdeksän kertaa:
ruudukko = [rivi, rivi, rivi, rivi, rivi, rivi, rivi, rivi, rivi]

print(*ruudukko, sep="\n")
print()

print(ruudukko[0])
print(ruudukko[0][0])
print()

# tämä muutos vaikuttaa kaikkiin riveihin
ruudukko[4][4] = 3

print(*ruudukko, sep="\n")
print()
