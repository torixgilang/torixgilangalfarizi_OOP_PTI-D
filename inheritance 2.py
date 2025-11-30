# multi level inheritance
class jenisKelamin:
    def jenis (self):
        print("jenis kelamin : Laki - Laki") 

class statusHidup:
    def status (self):
        print ("Status mahasiswa : masih hidup")

class mhs_Alumni (statusHidup):
    def lulus (self):
        print ("mahasiswa lulus tahun 2025")

class mhs_Aktif (jenisKelamin):
    def Masuk (self):
        print ("mahasiswa dengan NIM : 24241137")

#class child
class KTM (mhs_Aktif):
    pass
class Ijazah (mhs_Alumni):
    pass
class Beasiswa (mhs_Alumni, mhs_Aktif):
    pass

ktm = KTM()
ijazah = Ijazah()
beasiswa = Beasiswa()

ktm.Masuk()
ktm.jenis()
ijazah.status()
