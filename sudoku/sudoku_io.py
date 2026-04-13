"""
Tässä tiedostossa olevat funktiot lukevat ja kirjoittavat
sudoku-ruudukkoja tiedostoihin.
"""
from pathlib import Path
import json

HAKEMISTO = Path(__file__).parent


def lue_sudoku(tiedostonimi: str) -> list:
    """
    Lukee JSON-muotoisen sudokun ja palauttaa sen 
    sisäkkäisinä listoina.

    >>> sudoku = lue_sudoku("sudoku_testi.json")
    >>> sudoku[0][0]
    0
    >>> sudoku[1][1]
    8
    >>> sudoku[2][3]
    3
    """

    polku = HAKEMISTO / tiedostonimi

    if not polku.exists():
        raise IOError(f"Polkua {polku} ei löydy")

    sisalto = polku.read_text(encoding="utf-8")

    return json.loads(sisalto)


def tallenna_sudoku(ruudukko: list, tiedostonimi: str) -> bool:
    """
    Tallentaa annetun sudoku-ruudukon tiedostoon.

    >>> tallenna_sudoku([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "sudoku_testi.out.json")
    True

    >>> lue_sudoku("sudoku_testi.out.json")
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    data = json.dumps(ruudukko)

    polku = HAKEMISTO / tiedostonimi
    polku.write_text(data, encoding="utf-8")
    return True
