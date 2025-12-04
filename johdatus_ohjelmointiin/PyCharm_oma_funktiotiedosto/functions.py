# functions.py

import math
import random

def show_personal_info():
    print("Nimi: Maija Mallikas")
    print("Kotipaikka: Kettukylä")
    print("Ammatti: Koodari")

def count_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def magazine_serial_check(serial):
    if len(serial) != 9 or serial[4] != "-":
        print("Väärä ISSN")
        return
    cleaned = serial.replace("-", "")
    if len(cleaned) != 8:
        print("Väärä ISSN")
        return
    if cleaned.isdigit():
        print("Oikea ISSN")
    else:
        print("Väärä ISSN")

def show_numbered_list(title, data):
    print(title)
    for i, name in enumerate(data, start=1):
        print(f"{i}. {name}")

def box_volume(width, height, depth):
    return round(width * height * depth, 2)

def ball_volume(radius):
    return round((4 * math.pi * radius**3) / 3, 2)

def pipe_volume(radius, length):
    return round(math.pi * radius**2 * length, 2)

def lotto_numbers():
    numbers = []
    while len(numbers) < 7:
        n = random.randint(1, 40)
        if n not in numbers:
            numbers.append(n)

    extras = []
    while len(extras) < 3:
        n = random.randint(1, 40)
        if n not in numbers and n not in extras:
            extras.append(n)

    numbers.sort()
    extras.sort()
    return numbers, extras

# ---------------------------------
# Valuuttamuunnin
# ---------------------------------

def convert_money(amount, from_currency, to_currency):
    # Kaikki muutetaan ensin euroiksi
    rates_to_euro = {
        "€": 1,
        "$": 1 / 1.2,      # dollari -> euro
        "£": 1 / 0.9,      # punta -> euro
        "kr": 1 / 10.3     # kruunu -> euro
    }

    # Euroista kohdevaluuttaan
    euro_to_target = {
        "€": 1,
        "$": 1.2,
        "£": 0.9,
        "kr": 10.3
    }

    # Muuta ensin euroiksi
    euros = amount * rates_to_euro[from_currency]

    # Muunna euroista kohdevaluuttaan
    result = euros * euro_to_target[to_currency]

    return round(result, 2)
