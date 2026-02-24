"""
Luodaan ja tulostetaan 32 merkkiä pitkä satunnainen salasana 
"""

from random import choice
from string import ascii_letters, digits, punctuation

PITUUS = 32
MERKIT = ascii_letters + digits + punctuation


def satunnainen_salasana():
    """
    Palauttaa satunnaisen salasanan.
    """
    salasana = ""

    while len(salasana) < 32:
        merkki = choice(MERKIT)
        salasana += merkki

    return salasana
