import json

# Lue JSON-tiedosto
with open("countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

# Tulostetaan rivit allekkain
for item in countries:
    print(f"{item['country']} - {item['capital']}")

