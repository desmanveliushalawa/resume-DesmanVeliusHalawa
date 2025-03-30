class Orang: 
    # Mendefinisikan class Orang sebagai contoh OOP
    def __init__(self, nama, umur): 
        # Method __init__ digunakan untuk inisialisasi atribut
        self.nama = nama 
        # Atribut nama untuk menyimpan nama orang
        self.umur = umur 
        # Atribut umur untuk menyimpan umur orang

    def tampilkan_profil(self): 
        # Method untuk menampilkan profil orang
        print(f"Nama: {self.nama}") 
        # Menampilkan nama orang
        print(f"Umur: {self.umur} tahun") 
        # Menampilkan umur orang

    def berbicara(self, pesan): 
        # Method untuk membuat orang berbicara
        print(f"{self.nama} berkata: {pesan}") 
        # Menampilkan pesan yang diucapkan orang

# Membuat objek orang1 dari class Orang
orang1 = Orang("John Doe", 30) 
# Inisialisasi atribut nama dan umur orang1

# Menampilkan profil orang1
orang1.tampilkan_profil() 
# Memanggil method tampilkan_profil

# Membuat orang1 berbicara
orang1.berbicara("Halo, apa kabar?") 
# Memanggil method berbicara