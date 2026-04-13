'''
Tehtävä on lainattu Helsingin yliopiston Ohjelmoinnin perusteet -kurssilta
ohjelmointi-22.mooc.fi, ja se on lisensoitu Creative Commons BY-NC-SA 4.0 -lisenssillä.

Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
'''

# pylint: disable=unused-argument,fixme


def rivi_oikein(sudoku: list, rivi_nro: int) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    # https://ohjelmointi-22.mooc.fi/osa-5/1-lisaa-listoja#programming-exercise-sudoku-rivit-oikein
    return True


def sarake_oikein(sudoku: list, sarake_nro: int) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    # https://ohjelmointi-22.mooc.fi/osa-5/1-lisaa-listoja#programming-exercise-sudoku-sarakkeet-oikein
    return True


def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    # https://ohjelmointi-22.mooc.fi/osa-5/1-lisaa-listoja#programming-exercise-sudoku-neliot-oikein
    return True


def sudoku_oikein(sudoku: list) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    # https://ohjelmointi-22.mooc.fi/osa-5/1-lisaa-listoja#programming-exercise-sudoku-ruudukko-oikein
    return True


def sudoku_valmis(sudoku: list) -> bool:
    '''
    Tarkastaa, että annettu sudoku on kokonaan täytetty ja että se täyttää
    kaikki numeroita koskevat säännöt.
    '''

    for rivi in sudoku:
        if 0 in rivi:
            return False

    return sudoku_oikein(sudoku)
