"""
Tämä skripti lukee Pythonin zenin ulkoisesta tekstitiedostosta

Bugi 0: tiedostoa ei ole olemassa
    Ratkaisu: kerrotaan käyttäjälle kohteliaasti

Bugi 1: käyttäjän tulee olla samassa hakemistossa
    Ratkaisu: tehdään poluista suhteellisia suoritettavaan tiedostoon!

Bugi 2: polut toimivat eri tavoin Windowsissa ja Linuxissa
    Ratkaisu: ei kovakoodata polkuja, vaan muodostetaan ne ohjelmallisesti

Bugi 3: erikoismerkit ja ääkköset sekaisin
    Ratkaisu: lisätään encoding-parametri
"""

with open("osa06/zen_fi.txt", encoding="utf-8") as tiedosto:
    teksti = tiedosto.read()
    print(teksti)
