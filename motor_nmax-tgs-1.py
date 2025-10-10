mesin_nyala = False
kecepatan = 0
bahan_bakar = 100
jarak_tempuh = 0

print("=== SIMULASI MOTOR NMAX ===")

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
        if not mesin_nyala:
            mesin_nyala = True
            print("🔑 Mesin dinyalakan.")
        else:
            print("⚙️ Mesin sudah menyala.")

    elif pilihan == "2":
        if mesin_nyala:
            mesin_nyala = False
            kecepatan = 0
            print("🔚 Mesin dimatikan.")
        else:
            print("⚠️ Mesin sudah mati.")

    elif pilihan == "3":
        if mesin_nyala:
            if bahan_bakar <= 0:
                print("⛽ Bahan bakar habis! Tidak bisa jalan.")
                continue

            try:
                tambah = int(input("Tambah kecepatan berapa km/jam: "))
            except ValueError:
                print("⚠️ Masukkan angka saja!")
                continue

            kecepatan += tambah
            if kecepatan > 120:
                kecepatan = 120
                print("🚀 Kecepatan maksimum tercapai (120 km/jam)!")
            else:
                print(f"🏍️ Kecepatan sekarang: {kecepatan} km/jam")

            bahan_bakar -= tambah * 0.5
            jarak_tempuh += tambah * 0.2

            if bahan_bakar < 0:
                bahan_bakar = 0

        else:
            print("❌ Nyalakan mesin dulu sebelum gas.")

    elif pilihan == "4":
        if kecepatan > 0:
            try:
                kurang = int(input("Kurangi kecepatan berapa km/jam: "))
            except ValueError:
                print("⚠️ Masukkan angka saja!")
                continue

            kecepatan -= kurang
            if kecepatan < 0:
                kecepatan = 0
            print(f"🛑 Kecepatan sekarang: {kecepatan} km/jam")
        else:
            print("✅ Motor sudah berhenti.")

    elif pilihan == "5":
        print(f"""
==== STATUS MOTOR ====
Mesin       : {'Nyala' if mesin_nyala else 'Mati'}
Kecepatan   : {kecepatan} km/jam
Bahan bakar : {bahan_bakar:.1f} %
Jarak tempuh: {jarak_tempuh:.1f} km
=======================
""")

    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("⚠️ Pilihan tidak valid, coba lagi.")
