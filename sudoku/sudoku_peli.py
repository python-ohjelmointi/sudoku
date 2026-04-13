'''
Tämä tiedosto sisältää Sudoku-pelin käyttöliittymän, mutta se ei sisällä lainkaan
pelin logiikkaa. Logiikka on toteutettu aikaisemmissa viikkoharjoituksissa.
Pelin tueksi on toteutettu lisäksi sudoku_valmis-niminen funktio.
Logiikka löytyy tiedostosta sudoku_tarkistin.py.
'''

from sudoku_tarkistin import sudoku_oikein, sudoku_valmis
from sudoku_io import lue_sudoku, tallenna_sudoku

PELITILANNE_JSON = "pelitilanne.json"

# Sudoku-logo on luotu https://patorjk.com/software/taag/ -palvelussa.
logo = r'''
   _____             __        __
  / ___/ __  __ ____/ /____   / /__ __  __
  \__ \ / / / // __  // __ \ / //_// / / /
 ___/ // /_/ // /_/ // /_/ // ,<  / /_/ /
/____/ \__,_/ \__,_/ \____//_/|_| \__,_/

'''


def pelaa(ruudukko: list) -> bool:
    '''
    Pelaa Sudokua annetulla 2-ulotteisella kokonaislukuruudukolla, kunnes
    peli on läpäisty tai pelaaja keskeyttää pelin.

    Palauttaa True tai False riippuen siitä, pelattiinko peli loppuun.
    '''

    print(logo)

    # Toistetaan siirtoja, kunnes peli on valmis:
    while True:
        tulosta_ruudukko(ruudukko)
        print()  # Tyhjä rivi ruudukon ja kysymysten väliin

        try:
            pelaa_siirto(ruudukko)

            if sudoku_valmis(ruudukko):
                print('Sait sudokun valmiiksi 🥳:\n')
                tulosta_ruudukko(ruudukko)
                return True

        except KeyboardInterrupt:
            # Ctrl+C -komento johtaa pelistä poistumiseen
            print('Kiitos pelaamisesta 👋!')
            return False

        print()  # Tyhjä rivi jokaisen siirron jälkeen


def pelaa_siirto(ruudukko: list) -> None:
    '''
    Kysyy pelaajalta siirron ja tekee sen annetussa ruudukossa.
    Jos siirto ei ole sallittu, se perutaan.
    '''

    rivi = kysy_numero('Syötä rivi (0-8): ')
    sarake = kysy_numero('Syötä sarake (0-8): ')
    numero = kysy_numero('Syötä numero (1-9): ')

    try:
        # Alkuperäinen numero talteen, jotta se voidaan tarvittaessa palauttaa
        alkuperainen = ruudukko[rivi][sarake]

        # Asetetaan käyttäjän antama numero annettuun kohtaan
        ruudukko[rivi][sarake] = numero

        if sudoku_oikein(ruudukko):
            print('OK!')
            tallenna_sudoku(ruudukko, PELITILANNE_JSON)

        else:
            # Perutaan siirto
            print('Ei sallittu numero!')
            ruudukko[rivi][sarake] = alkuperainen

    except IndexError:
        print('Virheellinen rivi tai sarake!')


def kysy_numero(teksti: str) -> int:
    '''
    Pyytää käyttäjää syöttämään kokonaisluvun käyttäen annettua tekstiä.
    Toistaa kysymyksen, kunnes saa kelvollisen kokonaisluvun, joka palautetaan.
    '''

    # Toistetaan kysymystä, kunnes saadaan kelvollinen numero:
    while True:
        try:
            numero = int(input(teksti))
            return numero

        except ValueError as virhe:
            print('Virheellinen numero!')
            print('Voit lopettaa pelin painamalla Ctrl+C')
            print(virhe)


def tulosta_ruudukko(ruudukko: list):
    '''
    Tulostaa annetun ruudukon siten, että rivit ja sarakkeet on numeroitu.
    Eri "neliöt" sudokussa erotellaan putkilla (|) ja viivoilla (-), esim:

        0 1 2   3 4 5   6 7 8

    0   2 6 7 | 8 3 9 | 5   4
    1   9 8 3 | 5 1   | 6   2
    2   4 5 1 | 6     | 8 3 9
        ------ ------- ------
    3   5 1 9 |   4 6 | 3 2 8
    4   8   2 | 1   5 | 7   6
    5   6 7 4 | 3 2   |     5
        ------ ------- ------
    6         | 4 5 7 | 2 6 3
    7   3 2   |   8   |   5 7
    8   7 4 5 |     3 | 9   1
    '''

    ylin = '    0 1 2   3 4 5   6 7 8'
    vali = '    ------ ------- ------'

    print(ylin)
    print()

    for rivi_nro, rivi in enumerate(ruudukko):
        if rivi_nro in (3, 6):
            print(vali)

        print(f'{rivi_nro}   ', end='')

        for sarake_nro, numero in enumerate(rivi):
            if sarake_nro in (3, 6):
                print('| ', end='')

            # Nollien tilalla näytetään vain välilyönti:
            print(numero if numero != 0 else ' ', end=' ')

        print()  # Rivinvaihto viimeisen sarakkeen jälkeen


def main():
    # Pelin alkutila on lainattu mooc.fi:n esimerkistä
    ruudukko = lue_sudoku(PELITILANNE_JSON)

    pelaa(ruudukko)


if __name__ == '__main__':
    main()
