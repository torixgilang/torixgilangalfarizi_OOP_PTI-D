# Class Induk
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")

# Class Anak 1 - Dosen
class Dosen(Person):
    def __init__(self, nama, umur, nidn, mata_kuliah):
        super().__init__(nama, umur)  # mewarisi atribut dari Person
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"NIDN: {self.nidn}")
        print(f"Mata Kuliah: {self.mata_kuliah}")

# Class Anak 2 - Mahasiswa
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")

# === Program Utama ===
print("=== Data Dosen ===")
dosen1 = Dosen("Pak Budi", 40, "12345678", "Pemrograman Python")
dosen1.tampilkan_info()

print("\n=== Data Mahasiswa ===")
mhs1 = Mahasiswa("Khalid Tarmizi", 20, "2311001", "Teknik Komputer dan Jaringan")
mhs1.tampilkan_info()
