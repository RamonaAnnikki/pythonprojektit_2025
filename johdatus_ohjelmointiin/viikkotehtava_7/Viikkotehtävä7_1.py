cafe = {
    "name": "Imaginary Cafe Oy",
    "website": "https://edu.frostbit.fi/sites/cafe",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address": "Testikuja 22",
        "zip_code": "96200"
    }
}

# Tulostetaan tiedot siististi
print("Kahvilan nimi:", cafe["name"])
print("Kahvilan verkkosivut:", cafe["website"])
print("Kategoriat:")
for category in cafe["categories"]:
    print(" -", category)
print("Sijainti:")
print(" ", cafe["location"]["address"], ",", cafe["location"]["zip_code"], cafe["location"]["city"])


cafe = {
    "name": "Imaginary Cafe Oy",
    "website": "https://edu.frostbit.fi/sites/cafe",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address": "Testikuja 22",
        "zip_code": "96200"
    }
}

# ANSI-väriterminaalikoodeilla saadaan värit PyCharmin konsoliin
GREEN = "\033[92m"   # kirkkaanvihreä
BLUE = "\033[94m"    # sininen
RESET = "\033[0m"    # palauttaa värin normaaliksi

print(f"{GREEN}{cafe['name']}")
print(f"{cafe['location']['address']}")
print(f"{cafe['location']['zip_code']} {cafe['location']['city']}\n")

print(f"{BLUE}{cafe['website']}\n")

print(f"{GREEN}Palvelut: {', '.join(cafe['categories'])}{RESET}")
