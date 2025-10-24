class Motor:
    # 🔹 CLASS VARIABLE (sama untuk semua motor)
    batas_kecepatan = 120
    konsumsi_bbm = 0.5  # pengurangan bahan bakar per km/jam
    efisiensi_jarak = 0.2  # tambahan jarak tempuh per km/jam
    total_motor = 0

    def __init__(self, nama):
        # 🔸 INSTANCE VARIABLE (unik untuk setiap objek motor)
        self.nama = nama
        self.mesin_nyala = False
        self.kecepatan = 0
        self.bahan_bakar = 100
        self.jarak_tempuh = 0
        Motor.total_motor += 1  # setiap buat motor baru, tambah jumlah motor

    def nyalakan_mesin(self):
        if not self.mesin_nyala:
            self.mesin_nyala = True
            print("🔑 Mesin dinyalakan.")
        else:
            print("⚙ Mesin sudah menyala.")

    def matikan_mesin(self):
        if self.mesin_nyala:
            self.mesin_nyala = False
            self.kecepatan = 0
            print("🔚 Mesin dimatikan.")
        else:
            print("⚠ Mesin sudah mati.")

    def gas(self):
        if not self.mesin_nyala:
            print("❌ Nyalakan mesin dulu sebelum gas.")
            return

        if self.bahan_bakar <= 0:
            print("⛽ Bahan bakar habis! Tidak bisa jalan.")
            return

        try:
            tambah = int(input("Tambah kecepatan berapa km/jam: "))
        except ValueError:
            print("⚠ Masukkan angka saja!")
            return

        self.kecepatan += tambah
        if self.kecepatan > Motor.batas_kecepatan:
            self.kecepatan = Motor.batas_kecepatan
            print(f"🚀 Kecepatan maksimum tercapai ({Motor.batas_kecepatan} km/jam)!")
        else:
            print(f"🏍 Kecepatan sekarang: {self.kecepatan} km/jam")

        # pakai class variable untuk rumus konsumsi
        self.bahan_bakar -= tambah * Motor.konsumsi_bbm
        self.jarak_tempuh += tambah * Motor.efisiensi_jarak

        if self.bahan_bakar < 0:
            self.bahan_bakar = 0

    def rem(self):
        if self.kecepatan > 0:
            try:
                kurang = int(input("Kurangi kecepatan berapa km/jam: "))
            except ValueError:
                print("⚠ Masukkan angka saja!")
                return

            self.kecepatan -= kurang
            if self.kecepatan < 0:
                self.kecepatan = 0
            print(f"🛑 Kecepatan sekarang: {self.kecepatan} km/jam")
        else:
            print("✅ Motor sudah berhenti.")

    def status(self):
        print(f"""
==== STATUS MOTOR {self.nama} ====
Mesin       : {'Nyala' if self.mesin_nyala else 'Mati'}
Kecepatan   : {self.kecepatan} km/jam
Bahan bakar : {self.bahan_bakar:.1f} %
Jarak tempuh: {self.jarak_tempuh:.1f} km
==============================
Batas Kecepatan Global : {Motor.batas_kecepatan} km/jam
Total Motor Tersimpan  : {Motor.total_motor}
==============================
""")


# ==============================
# MAIN PROGRAM
# ==============================

print("=== SIMULASI MOTOR NMAX ===")
motor1 = Motor("Yamaha NMAX 155")

while True:
    print("""
==============================
1. Nyalakan mesin
2. Matikan mesin
3. Gas
4. Rem
5. Lihat status
6. Keluar
==============================
""")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        motor1.nyalakan_mesin()
    elif pilihan == "2":
        motor1.matikan_mesin()
    elif pilihan == "3":
        motor1.gas()
    elif pilihan == "4":
        motor1.rem()
    elif pilihan == "5":
        motor1.status()
    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("⚠ Pilihan tidak valid, coba lagi.")
