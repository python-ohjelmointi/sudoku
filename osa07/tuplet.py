from collections import namedtuple
from random import sample

Pisterivi = namedtuple("Pisterivi", ["tunnus", "tehtava", "pisteet", "palautusaika"])

# tunnus;tehtävä;pisteet;hh:mm
csv_rivi = Pisterivi("timo", 2, 10, "21:22")

print(csv_rivi)

print(csv_rivi.tunnus)
print(csv_rivi.tehtava)
print(csv_rivi.pisteet)
print(csv_rivi.palautusaika)
