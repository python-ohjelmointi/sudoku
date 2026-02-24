"""
<select id="kulutus">
    <option value="1">1  l/100 km</option>
    <option value="2">2  l/100 km</option>
</select>
"""

print('<select id="kulutus">')

kulutus = 1

while True:
    print(f'    <option value="{kulutus}">{kulutus}</option>')

    kulutus += 1

    if kulutus > 30:
        break

print('</select>')
