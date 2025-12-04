import json
from datetime import date
import os

FILENAME = "maintenance.json"

# Tarkistetaan onko maintenance.json olemassa
if os.path.exists(FILENAME):
    print("Aiempi huoltokirjaus löytyy:")
    with open(FILENAME, "r", encoding="utf-8") as file:
        old_data = json.load(file)
        print(old_data)
    print()  # tyhjä rivi

# Kysytään uudet tiedot käyttäjältä
name = input("Kirjaajan nimi: ")
code = input("Tilannekoodi: ")
desc = input("Selite: ")
today = date.today().isoformat()   # esim. '2025-11-20'

# Rakennetaan dictionary
entry = {
    "name": name,
    "code": code,
    "description": desc,
    "date": today
}

# Tallennetaan JSON-tiedostoon
with open(FILENAME, "w", encoding="utf-8") as file:
    json.dump(entry, file, indent=4, ensure_ascii=False)

print("Uusi huoltokirjaus tallennettu.")
