import json

saldo = 0
FILE_DATA = "saldo.json"

def simpan_saldo():
    try:
        with open(FILE_DATA, "w") as file:
            json.dump({"saldo": saldo}, file)
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")

def baca_saldo():
    global saldo
    try:
        with open(FILE_DATA, "r") as file:
            data = json.load(file)
            saldo = data.get("saldo", 0)
            print(f"Saldo dimuat dari file: Rp{saldo:,}")
    except FileNotFoundError:
        print("File saldo.json tidak ditemukan. Membuat file baru...")
        saldo = 0
        simpan_saldo()
    except Exception as e:
        print(f"Gagal membaca data: {e}")

def tambah_pemasukan():
    global saldo
    try:
        jumlah = int(input("Masukkan jumlah pemasukan: "))
        if jumlah > 0:
            saldo += jumlah
            simpan_saldo()
            print(f"Pemasukan Rp{jumlah:,} berhasil ditambahkan!")
        else:
            print("Jumlah harus lebih dari 0!")
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = int(input("Masukkan jumlah pengeluaran: "))
        if jumlah > 0:
            if saldo >= jumlah:
                saldo -= jumlah
                simpan_saldo()
                print(f"Pengeluaran Rp{jumlah:,} berhasil dikurangi!")
            else:
                print(f"⚠️ Saldo tidak cukup! Saldo Anda hanya Rp{saldo:,}")
        else:
            print("Jumlah harus lebih dari 0!")
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

def lihat_saldo():
    print("=" * 30)
    print(f"Saldo Anda: Rp{saldo:,}")
    print("=" * 30)

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

baca_saldo()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")



                                                                                                            