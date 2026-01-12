import os
import time

# Nama file untuk menyimpan data
NAMA_FILE = "database_tugas.txt"
daftar_tugas = []

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- FUNGSI BARU: DATABASE (FILE HANDLING) ---

def muat_data_dari_file():
    """Membaca data dari file .txt saat program baru dibuka"""
    tugas_loaded = []
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as file:
            # Membaca setiap baris di file
            for baris in file:
                # .strip() membuang karakter 'enter' (\n) di ujung kalimat
                tugas_loaded.append(baris.strip())
    return tugas_loaded

def simpan_ke_file():
    """Menulis ulang seluruh isi list ke dalam file .txt"""
    with open(NAMA_FILE, "w") as file:
        for tugas in daftar_tugas:
            file.write(tugas + "\n") # Tambah \n biar turun baris

# --- FUNGSI FITUR (Sama tapi di-update) ---

def tampilkan_menu():
    print("=== TO-DO LIST PRO (AUTO-SAVE) ===")
    print("[1] Lihat Daftar Tugas")
    print("[2] Tambah Tugas Baru")
    print("[3] Hapus Tugas")
    print("[4] Keluar")
    print("==================================")

def lihat_tugas():
    bersihkan_layar()
    print("--- DAFTAR TUGAS KAMU ---")
    
    if len(daftar_tugas) == 0:
        print("Tugas kosong. File database bersih.")
    else:
        for index, tugas in enumerate(daftar_tugas, 1):
            print(f"{index}. {tugas}")
    
    input("\nTekan Enter untuk kembali ke menu...")

def tambah_tugas():
    bersihkan_layar()
    print("--- TAMBAH TUGAS ---")
    tugas_baru = input("Masukkan nama tugas: ")
    
    if tugas_baru: # Cek biar user gak input kosong
        daftar_tugas.append(tugas_baru)
        simpan_ke_file() # <--- PENTING: Langsung simpan ke harddisk
        print(f"\n✅ Berhasil disimpan ke {NAMA_FILE}!")
    else:
        print("Gak boleh kosong dong.")
        
    time.sleep(1)

def hapus_tugas():
    bersihkan_layar()
    print("--- HAPUS TUGAS ---")
    
    if len(daftar_tugas) == 0:
        print("Tidak ada tugas.")
        time.sleep(1)
        return

    for index, tugas in enumerate(daftar_tugas, 1):
        print(f"{index}. {tugas}")

    print("-------------------")
    try:
        nomor = int(input("Hapus tugas nomor berapa? "))
        if 1 <= nomor <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas.pop(nomor - 1)
            simpan_ke_file() # <--- PENTING: Update file setelah menghapus
            print(f"\n🗑️ Tugas '{tugas_dihapus}' dihapus permanen.")
        else:
            print("\n❌ Nomor salah.")
    except ValueError:
        print("\n❌ Masukkan angka saja.")
    
    time.sleep(1.5)

def main():
    # Load data dulu sebelum program jalan
    global daftar_tugas
    daftar_tugas = muat_data_dari_file()

    while True:
        bersihkan_layar()
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            lihat_tugas()
        elif pilihan == '2':
            tambah_tugas()
        elif pilihan == '3':
            hapus_tugas()
        elif pilihan == '4':
            print("Data aman. Sampai jumpa!")
            break
        else:
            print("Menu tidak ada.")
            time.sleep(1)

if __name__ == "__main__":
    main()