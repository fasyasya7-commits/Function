
# 1. Variabel Global (Bisa diakses dari mana saja)
NAMA_TOKO = "Toko Makmur"


# 2. Decorator (Fungsi pembungkus sederhana)
def cetak_garis(fungsi_asli):
    def bungkus(barang, harga):
        print("================================")

        hasil = fungsi_asli(barang, harga)

        print("================================")
        return hasil

    return bungkus


# 3. Fungsi utama yang akan didekorasi
@cetak_garis
def tampilkan_barang(barang, harga):

    # Variabel lokal (Hanya bisa diakses di dalam fungsi ini)
    diskon = 6000
    total = harga - diskon

    print(f"Nama Toko: {NAMA_TOKO}")
    print(f"Barang: {barang}")
    print(f"Total bayar setelah diskon: Rp {total}")

    # Nilai Balik (Return Value)
    return total


# 4. Program utama
hasil_akhir = tampilkan_barang("pulpen", 7000)

print(f"Hasil akhir yang dikembalikan: Rp {hasil_akhir}")
