shopcart = [
    {"name": "Lokki-valaisin", "price": 349.9},
    {"name": "Stockholm-matto", "price": 129.9},
    {"name": "Malm-lipasto", "price": 49.9},
    {"name": "Vienna-divaanisohva", "price": 799.9},
    {"name": "Ritz-nojatuoli", "price": 369.9}
]

# ANSI-värit terminaaliin
GREEN = "\033[92m"
RESET = "\033[0m"

# Tulostus
print(f"{GREEN}Kuitti ostoksista:")

total = 0
for item in shopcart:
    print(f"- {item['name']}")
    total += item['price']

print()
print(f"Yhteensä {total} €.")
print("Tervetuloa uudelleen!" + RESET)
