import os

FILENAME = "products.txt"

# Lataa tuotteet listaksi
def load_products():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


# Tallenna tuotteet takaisin tiedostoon
def save_products(products):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for product in products:
            file.write(product + "\n")


# Tulosta lista numeroituna
def print_products(products):
    print("\nTuotelista:")
    if not products:
        print("(ei tuotteita)")
    else:
        for i, product in enumerate(products):
            print(f"{i+1}. {product}")
    print()


# --- Pääohjelma ---
products = load_products()

while True:
    print_products(products)

    print("Valitse toiminto:")
    print("1 = Lisää tuote")
    print("2 = Muokkaa tuotetta")
    print("3 = Poista tuote")
    print("4 = Lopeta")
    choice = input("Valinta: ")

    if choice == "1":
        new_product = input("Anna uuden tuotteen nimi: ")
        products.append(new_product)
        print("Tuote lisätty.\n")

    elif choice == "2":
        index = int(input("Anna muokattavan tuotteen numero: ")) - 1
        if 0 <= index < len(products):
            new_name = input("Anna uusi nimi: ")
            products[index] = new_name
            print("Tuote päivitetty.\n")
        else:
            print("Virheellinen numero.\n")

    elif choice == "3":
        index = int(input("Anna poistettavan tuotteen numero: ")) - 1
        if 0 <= index < len(products):
            removed = products.pop(index)
            print(f"Tuote '{removed}' poistettu.\n")
        else:
            print("Virheellinen numero.\n")

    elif choice == "4":
        save_products(products)
        print("Tuotteet tallennettu. Ohjelma sulkeutuu.")
        break

    else:
        print("Tuntematon valinta.\n")
