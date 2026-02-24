"""
Printataan vuodet 202x - 2000 laskevassa järjestyksessä
"""
from datetime import date

tanaan = date.today()
vuosi = tanaan.year

while vuosi >= 2000:
    print(vuosi)

    vuosi -= 1
