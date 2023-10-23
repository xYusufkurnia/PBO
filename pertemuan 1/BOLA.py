import math

# Input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari bola: "))

# Menghitung luas permukaan bola
luas = 4 * math.pi * jari_jari ** 2

# Menghitung volume bola
volume = (4/3) * math.pi * jari_jari ** 3

# Tampilkan hasil
print(f"Luas permukaan bola adalah: {luas:.2f}")
print(f"Volume bola adalah: {volume:.2f}")
