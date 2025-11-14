# class parent
class Mhs_Alumni:
    lulus = 2025


class Mhs_Aktif:
    masuk = 2024


# class child (multiple inheritance)
class Mahasiswa(Mhs_Alumni, Mhs_Aktif):
    ktm = "ada"
    ijazah = "belum ada"
    beasiswa = "KIP"


# class multilevel
class Mahasiswa_Lanjut(Mahasiswa):
    program = "S2"


# --- Output ---
m = Mahasiswa()
print("Lulus :", m.lulus)
print("Masuk :", m.masuk)
print("KTM :", m.ktm)
print("Ijazah :", m.ijazah)
print("Beasiswa :", m.beasiswa)

lanjut = Mahasiswa_Lanjut()
print("\nProgram lanjutan :", lanjut.program)