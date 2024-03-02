def hitung_dan_tampilkan_bilangan_ganjil(lower, upper):
    
    # memastikan batas bawah dan batas atas tidak negatif
    if lower < 0 or upper < 0:
        print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
        return

    # Jika batas atas ganjil, kurangi satu agar tidak termasuk dalam perhitungan
    if upper % 2 != 0:
        upper -= 1

    # Menghitung jumlah bilangan ganjil dalam rentang
    total_ganjil = sum(i for i in range(lower, upper + 1, 2))

    # Mencetak output 
    print("batas bawah:", lower)
    print("batas atas:", upper + 1)  # Tampilkan batas atas sebenarnya (tanpa perubahan)
    print("Bilangan ganjil dalam rentang tersebut:")
    for i in range(lower, upper + 1, 2):
        print(i)
    print("total:", total_ganjil)


# Input batas bawah dan batas atas dari user
lower = int(input("Masukkan batas bawah: "))
upper = int(input("Masukkan batas atas: "))

# Memanggil fungsi untuk menghitung dan menampilkan bilangan ganjil
hitung_dan_tampilkan_bilangan_ganjil(lower, upper)
