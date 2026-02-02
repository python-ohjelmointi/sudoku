# pylint: disable=C0103

# UI eli käyttöliittymä:
moottori = input("Onko moottoria (k/e): ") == "k"
polkimet = input("Onko polkimet (k/e): ") == "k" if moottori else False
teho = int(input("Syötä teho (W): ")) if moottori else False
avustusnopeus = int(input("Syötä avustusnopeus: ")) if moottori else False

# "Bisneslogiikka"
if moottori:
    if polkimet:
        if teho <= 250 and avustusnopeus <= 25:
            print("Sähköavusteinen polkupyörä")
            print("Rinnastettavissa polkupyörään")
        elif avustusnopeus <= 45:
            print("Mahdollisesti nopea sähköpyörä tai sähkömopo")
            print("Vaatii tyyppihyväksynnän")
        else:
            print("Muu kevyt sähköajoneuvo")
    else:
        print("Mahdollisesti sähköpotkulauta")
else:
    print("Tuntematon kulkuväline")
