import math

print("Toisen asteen yhtälön ratkaisu")
print("Yhtälö muotoa: a*x^2 + b*x + c = 0")

# Kysy käyttäjältä a, b ja c
a = float(input("Anna a: "))
b = float(input("Anna b: "))
c = float(input("Anna c: "))

# Tarkista, että a ei ole 0
if a == 0:
    print("a ei voi olla 0, tämä ei ole toisen asteen yhtälö.")
else:
    # Laske diskriminantti
    d = b**2 - 4*a*c

    if d > 0:
        # Kaksi eri ratkaisua
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Yhtälöllä on kaksi ratkaisua: x1 = {x1}, x2 = {x2}")
    elif d == 0:
        # Yksi ratkaisu
        x = -b / (2*a)
        print(f"Yhtälöllä on yksi ratkaisu: x = {x}")
    else:
        # Ei ratkaisua
        print("Yhtälöllä ei ole reaalisia ratkaisuja")