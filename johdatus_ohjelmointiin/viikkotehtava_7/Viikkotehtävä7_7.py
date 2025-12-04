import json
import urllib.request
from datetime import datetime

# Haetaan data API:sta
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
warnings = json.loads(raw_data)

# Jos API palauttaa listan, varmistetaan että siinä on dataa
if not warnings:
    print("Liukastumisvaroituksia ei löytynyt.")
    exit()

# 1) Selvitetään missä kaupungissa on ollut eniten varoituksia
city_counts = {}

for warning in warnings:
    city = warning.get("city")
    if city:
        city_counts[city] = city_counts.get(city, 0) + 1

# Etsitään kaupunki, jolla on eniten varoituksia
most_warnings_city = max(city_counts, key=city_counts.get)
print(f"Eniten liukastumisvaroituksia on ollut kaupungissa: {most_warnings_city} ({city_counts[most_warnings_city]} kpl)\n")

# 2) Näytetään 5 viimeisintä varoitusta aikajärjestyksessä
# Järjestetään aikaleiman mukaan uusimmasta vanhimpaan
warnings_sorted = sorted(
    warnings,
    key=lambda x: x.get("created_at", ""),
    reverse=True
)

print("Viisi viimeisintä liukastumisvaroitusta:\n")
for w in warnings_sorted[:5]:
    city = w.get("city", "Tuntematon")
    timestamp = w.get("created_at", "")
    try:
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        formatted_time = dt.strftime("%d.%m.%Y %H:%M")
    except Exception:
        formatted_time = timestamp
    print(f"- {city}: {formatted_time}")
