"""
* 20 km/h
* 40 km/h
* 60 km/h
* 80 km/h
* 100 km/h
* 150 km/h
* 200 km/h
* 250 km/h
"""
nopeus = 40

# toistoehto
while nopeus <= 250:
    print(f"* {nopeus} km/h")

    # kasvatetaan 20:llä, tai jos luku > 100, niin 50:llä:
    if nopeus < 100:
        nopeus += 20
    else:
        nopeus += 50
