import random  # Satunnaislukujen luontiin

# a) Satunnaisluku 1–10
luku = random.randint(1, 10)
print("Arvottu luku 1–10:")
print(luku)

print("\n---\n")

# b) Suorakulmion pinta-ala satunnaisilla sivuilla 2–10
a = random.randint(2, 10)
b = random.randint(2, 10)
pinta_ala = a * b

print("Arvottu sivu a:")
print(a)
print("Arvottu sivu b:")
print(b)
print("Suorakulmion pinta-ala:")
print(pinta_ala)