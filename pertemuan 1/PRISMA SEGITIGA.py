# Mengambil input untuk panjang alas, tinggi segitiga, dan tinggi prisma
alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

# Menghitung luas permukaan
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
luas_permukaan_prisma = 2 * alas_segitiga * tinggi_segitiga + 3 * alas_segitiga * tinggi_prisma

# Menghitung volume
volume_prisma = luas_segitiga * tinggi_prisma

# Mencetak luas permukaan dan volume
print(f"Luas permukaan prisma segitiga : {luas_permukaan_prisma}")
print(f"Volume prisma segitiga : {volume_prisma}")


