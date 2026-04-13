"""
Path-luokka helpottaa tiedostojen käsittelyä huomattavasti,
koska sen avulla saadaan luotua dynaamisesti polkuja, jotka
ovat järjestelmäriippumattomia. Sillä saadaan tarkastettua
onko tiedosto olemassa ja luettua sen sisältö kerralla.
"""

from pathlib import Path

tyohakemisto = Path()
print("Työhakemisto:", tyohakemisto.resolve())

skripti = Path(__file__)
print("Skriptin sijainti:", skripti)

skriptihakemisto = skripti.parent
print("Skriptin hakemisto:", skriptihakemisto)

luettava_tiedosto = skriptihakemisto / "zen_fi.txt"
print("zen-tiedosto:", luettava_tiedosto)

if luettava_tiedosto.exists():
    print("Tiedosto löytyy")

    sisalto = luettava_tiedosto.read_text(encoding="utf-8")

    print(sisalto)
    print(len(sisalto), "merkkiä")
    print(len(sisalto.splitlines()), "riviä")

else:
    print("Tiedostoa ei valitettavasti löydy")
