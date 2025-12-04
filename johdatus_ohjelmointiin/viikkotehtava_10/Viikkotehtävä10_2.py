choice = input("Haluatko lukea vai kirjoittaa vieraskirjaan? (l/k): ").lower()

if choice == "l":
    # Lukeminen
    with open("guestbook.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            print("Vieraskirja on tyhjä.")
        else:
            for line in lines:
                print(line.strip())

elif choice == "k":
    # Kirjoittaminen
    entry = input("Kirjoita viestisi: ")
    with open("guestbook.txt", "a", encoding="utf-8") as file:
        file.write(entry + "\n")
    print("Viestisi on tallennettu vieraskirjaan.")

else:
    print("Tuntematon valinta.")
