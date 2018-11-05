class Kota:
    '''Dasar kota'''
    jumlah_kota = 0

    def __init__(self, nama, walikota, geografi):
        self.nama = nama
        self.gaji = walikota
        self.geografi = geografi
        kota.jumlah_kota += 1

    def tampilkan_jumlah(self):
        print("Total kota:", kota.jumlah_kota)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Walikota :", self.walikota)
        print("Geografi :", self.geografi)

# Membuat objek pertama dari kelas Kota
kota1 = Kota("Surabaya", tri risma, dataran rendah)
# Membuat objek kedua dari kelas Kota
kota2 = Kota("Gresik", sambari, bukit kapur)

kota1.tampilkan_profil()
kota2.tampilkan_profil()
print("Total kota :", Kota.jumlah_kota)

	if bukit_kapur:
		print("Gresik:")
	else:
		print("Surabaya:")