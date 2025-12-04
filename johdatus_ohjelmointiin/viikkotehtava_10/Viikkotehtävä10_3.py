import json
from datetime import datetime

FILENAME = "guestbook.json"

# Lataa vieraskirjan sisältö tai palauta tyhjä lista
def load_guestbook():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Tallenna vieraskirja JSON-muotoon
def save_guestbook(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Pääohjelma
choice = input("Haluatko lukea (l) vai kirjoittaa (k)? ").lower()
guestbook = load_guestbook()

if choice == "l":
    if not guestbook:
        print("Vieraskirja on tyhjä.")
    else:
        for entry in guestbook:
            print(f"{entry['timestamp']}: {entry['message']}")

elif choice == "k":
    message = input("Kirjoita viestisi: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    guestbook.append({
        "message": message,
        "timestamp": timestamp
    })

    save_guestbook(guestbook)
    print("Viestisi tallennettiin onnistuneesti.")

else:
    print("Tuntematon valinta.")
