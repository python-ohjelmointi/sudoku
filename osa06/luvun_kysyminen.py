"""
Tässä esimerkissä kokeillaan luvun kysymistä käyttäjältä
niin, että virhetilanteessa luku kysytään uudestaan.
"""

while True:
    try:
        luku = int(input("Syötä numero: "))
        break
    except ValueError:
        print("Syötit virheellisen luvun, yritä uudelleen.")

    except KeyboardInterrupt:
        print("Ok, kiitos kuitenkin ja kokeile tätä uudelleen myöhemmin.")
        break


if luku < 50:
    print("Luku on pieni")
else:
    print("Luku on suuri")

