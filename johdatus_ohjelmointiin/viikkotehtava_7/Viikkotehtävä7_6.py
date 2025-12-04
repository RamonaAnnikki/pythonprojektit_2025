# Ravintoladata
restaurants = [
    {
        "name": "North Delish",
        "rating": 4.5,
        "reservations": True,
        "services": ["lunch", "dinner"],
        "price_level": 5,
        "location": "Rovaniemi"
    },
    {
        "name": "Food Galore",
        "rating": 3.8,
        "reservations": False,
        "services": ["breakfast", "lunch"],
        "price_level": 3,
        "location": "Tornio"
    },
    {
        "name": "Snacksy Oy",
        "rating": 3.2,
        "reservations": False,
        "services": ["lunch", "dinner", "night"],
        "price_level": 2,
        "location": "Oulu"
    },
    {
        "name": "Midnight Bite",
        "rating": 4.0,
        "reservations": True,
        "services": ["night"],
        "price_level": 4,
        "location": "Rovaniemi"
    },
    {
        "name": "Sunrise Café",
        "rating": 4.2,
        "reservations": False,
        "services": ["breakfast", "lunch"],
        "price_level": 2,
        "location": "Kemi"
    },
    {
        "name": "Fine North",
        "rating": 4.8,
        "reservations": True,
        "services": ["dinner"],
        "price_level": 5,
        "location": "Oulu"
    }
]

# Tervetuloa-teksti
print("Tervetuloa ravintolahakuun!\n")

min_rating = float(input("Monenko tähden ravintolan haluat vähintään? (1–5): "))
max_price = int(input("Minkä hintatason ravintolan haluat maksimissaan? (1–5): "))
res = input("Haluatko tehdä etukäteen varauksen? (k/e): ").lower()
hour = int(input("Mihin kellonaikaan haluat ruokailla? (0–23): "))

# Määritetään palveluajan mukainen ruokailu
def get_service_by_hour(h):
    if 6 <= h <= 10:
        return "breakfast"
    elif 11 <= h <= 16:
        return "lunch"
    elif 17 <= h <= 24:
        return "dinner"
    elif 0 <= h <= 5:
        return "night"
    else:
        return None

wanted_service = get_service_by_hour(hour)

# Suodatetaan ravintolat
matches = []
for r in restaurants:
    # tarkistetaan ehdot
    if r["rating"] >= min_rating and r["price_level"] <= max_price:
        if wanted_service in r["services"]:
            if res == "k" and not r["reservations"]:
                continue  # käyttäjä halusi varattavan, mutta tämä ei ole
            matches.append(r)

# Tulostetaan tulos
print("\nHakutulokset:\n")
if matches:
    for r in matches:
        print(f"- {r['name']} ({r['location']}) – {r['rating']} ★, hinta {r['price_level']}/5")
else:
    print("Valitettavasti sopivaa ravintolaa ei löytynyt!")
