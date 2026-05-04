kurssit = [
    {
        "nimi": "Ohjelmistokehityksen perusteet",
        "tunnus": "SOF001AS2A",
        "periodit": [1, 2]
    },
    {
        "nimi": "Web-sovelluskehitys",
        "tunnus": "SOF004AS2A",
        "periodit": [3, 4]
    },
    {
        "nimi": "Tietokannat ja tiedonhallinta",
        "tunnus": "ICT004AS3A",
        "periodit": [1, 3]
    }
]

tunnukset = [k["tunnus"] for k in kurssit]
nimet = [k["nimi"] for k in kurssit]

print(tunnukset)
print(nimet)

kurssi_map = { kurssi["tunnus"]: kurssi["nimi"] for kurssi in kurssit }
print(kurssi_map)
