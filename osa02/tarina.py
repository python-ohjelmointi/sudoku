"""
lopetetaan sanaan "loppu" tai jos käyttäjä syöttää saman sanan kahdesti
"""

# kokoojamuuttuja, johon laitetaan kaikki talteen:
tarina = ""
edellinen = ""

while True:

    sana = input("Anna sana: ")

    if sana == "loppu" or sana == edellinen:
        break

    if tarina == "":
        tarina = sana
    else:
        tarina = tarina + " " + sana

    edellinen = sana

print(tarina)
