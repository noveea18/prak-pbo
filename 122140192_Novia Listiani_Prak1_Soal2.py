
phi = 3.14159

# Input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Memastikan jari-jari tidak negatif
if jari_jari < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    # Menghitung luas dan keliling lingkaran
    luas = phi * jari_jari ** 2
    keliling = 2 * phi * jari_jari

    # Mencetak hasil
    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)
