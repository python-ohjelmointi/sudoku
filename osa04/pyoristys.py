"""
Oletuksena, Python pyöristää "puolivälit" aina lähimpään parilliseen,
eikä ylöspäin kuten olemme tottuneet.
"""


def pyorista(numero):
    """
    Pyöristää annetun numeron "peruskoulun" pyöristyssääntöjen mukaan,
    eli puolikkaat ylöspäin. Liulukujen epätarkkuuden vuoksi virheet ovat
    silti mahdollisia.

    Doctest-testit auttavat koodin laadunvarmistuksessa ilman, että joudut
    itse vertailemaan ja tulostelemaan asioita.

    >>> pyorista(100.9)
    101
    >>> pyorista(1.5)  
    2
    >>> pyorista(-1.9)
    -2
    >>> pyorista(-1.1)
    -1
    >>> pyorista(0)
    0
    """

    if numero < 0:
        # negatiiviset luvut käännetään positiivisiksi,
        # pyöristetään ja muutetaan takaisin negatiivisiksi
        return -pyorista(-numero)

    kokonaiset = int(numero)
    desimaalit = numero % 1

    if desimaalit >= 0.5:
        # pyöristä ylöspäin
        return kokonaiset + 1

    return kokonaiset
