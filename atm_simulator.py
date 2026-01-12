import os
import time

# --- DATA USER (Ceritanya database nasabah) ---
PIN_RAHASIA = "123456"
saldo_rekening = 500000  # Saldo awal Rp 500.000

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cek_pin():
    """Fungsi untuk meminta login PIN di awal"""
    percobaan = 0
    while percobaan < 3:
        bersihkan_layar()
        print("==============================")
        print("   SELAMAT DATANG DI ATM PYTHON")
        print("==============================")
        input_pin = input("Masukkan 6 digit PIN Anda: ")

        if input_pin == PIN_RAHASIA:
            return True # Login berhasil
        else:
            print("❌ PIN SALAH!")
            percobaan += 1
            sisa = 3 - percobaan
            print(f"Sisa percobaan: {sisa}")
            time.sleep(1.5)

    return False # Gagal login 3x

def tampilkan_menu():
    print("=== MENU TRANSAKSI ===")
    print("[1] Cek Saldo")
    print("[2] Tarik Tunai")
    print("[3] Setor Tunai")
    print("[4] Keluar")
    print("======================")

def main():
    # Panggil global variable saldo biar bisa diubah-ubah
    global saldo_rekening 

    # 1. Login Dulu
    if not cek_pin():
        print("\n🚫 KARTU ANDA DIBLOKIR KARENA SALAH PIN 3X.")
        return # Stop program

    # 2. Masuk Menu Utama
    while True:
        bersihkan_layar()
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            bersihkan_layar()
            print(f"💰 Saldo Anda saat ini: Rp {saldo_rekening:,}")
            # {:,} itu format biar angkanya ada komanya (500,000)
            input("\nTekan Enter untuk lanjut...")

        elif pilihan == '2':
            bersihkan_layar()
            print(f"Saldo: Rp {saldo_rekening:,}")
            try:
                jumlah = int(input("Masukkan nominal penarikan: Rp "))
                
                if jumlah < 50000:
                    print("⚠️ Minimal penarikan Rp 50.000")
                elif jumlah > saldo_rekening:
                    print("❌ Saldo tidak cukup!")
                else:
                    saldo_rekening -= jumlah # Kurangi saldo
                    print("✅ Penarikan berhasil!")
                    print("Silakan ambil uang Anda.")
                    print(f"Sisa saldo: Rp {saldo_rekening:,}")
            except ValueError:
                print("❌ Masukkan angka saja!")
            
            input("\nTekan Enter untuk lanjut...")

        elif pilihan == '3':
            bersihkan_layar()
            try:
                jumlah = int(input("Masukkan nominal setoran: Rp "))
                if jumlah < 0:
                    print("⚠️ Tidak bisa setor minus!")
                else:
                    saldo_rekening += jumlah # Tambah saldo
                    print("✅ Setor tunai berhasil!")
                    print(f"Saldo baru: Rp {saldo_rekening:,}")
            except ValueError:
                print("❌ Masukkan angka saja!")
            
            input("\nTekan Enter untuk lanjut...")

        elif pilihan == '4':
            print("Terima kasih telah menggunakan ATM Python.")
            print("Jangan lupa ambil kartu Anda.")
            break
        
        else:
            print("Menu tidak tersedia.")
            time.sleep(1)

if __name__ == "__main__":
    main()