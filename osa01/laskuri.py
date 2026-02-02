# pylint: disable=C0103,C0114
from math import ceil

vieraat = int(input("Montako vierasta on tulossa? "))
lasillisia_simapullossa = 7

pulloja = ceil(vieraat / lasillisia_simapullossa)

print(f"{vieraat} vierasta tarvitsee {pulloja} pulloa simaa")
