from salasanat import satunnainen_salasana

indeksi = 0

while indeksi < 30:
    print(
        f"username: user{indeksi}@myy.haaga-helia.fi, password: {satunnainen_salasana()}")
    indeksi += 1
