import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

# Värit
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

# a) Selvitetään missä tuulee eniten ja vähiten
max_wind = max(weather, key=lambda x: x["wind"])
min_wind = min(weather, key=lambda x: x["wind"])

print(f"{CYAN}Eniten tuulee: {max_wind['location']} ({max_wind['wind']} m/s)")
print(f"Vähiten tuulee: {min_wind['location']} ({min_wind['wind']} m/s){RESET}")

print()

# b) Lasketaan keskimääräinen tuulennopeus alueittain
areas = {}
for data in weather:
    area = data["area"]
    wind = data["wind"]
    if area not in areas:
        areas[area] = []
    areas[area].append(wind)

# Käännös englanninkielisistä aluekoodista suomeksi
area_names = {
    "lapland": "Lapin alue",
    "middle": "Maan keskiosa",
    "south": "Etelä-Suomi"
}

print(f"{GREEN}Keskimääräinen tuulennopeus alueittain:{RESET}")
for area, winds in areas.items():
    avg_wind = sum(winds) / len(winds)
    print(f"- {area_names.get(area, area)}: {avg_wind:.1f} m/s")

