import os
import time

# List kosong untuk menampung tugas
daftar_tugas = []

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    print("=== APLIKASI TO-DO LIST ===")
    print("[1] Lihat Daftar Tugas")
    print("[2] Tambah Tugas Baru")
    print("[3] Hapus Tugas")
    print("[4] Keluar")
    print("===========================")

def lihat_tugas():
    bersihkan_layar()
    print("--- DAFTAR TUGAS KAMU ---")
    
    # Cek apakah list kosong atau ada isinya
    if len(daftar_tugas) == 0:
        print("Tugas kosong! Wah, kamu rajin atau malas nih?")
    else:
        # Enumerate mulai dari 1 biar user bacanya enak (bukan index 0)
        for index, tugas in enumerate(daftar_tugas, 1):
            print(f"{index}. {tugas}")
    
    input("\nTekan Enter untuk kembali ke menu...")

def tambah_tugas():
    bersihkan_layar()
    print("--- TAMBAH TUGAS ---")
    tugas_baru = input("Masukkan nama tugas: ")
    
    # Masukkan ke dalam list
    daftar_tugas.append(tugas_baru)
    
    print(f"\n✅ Berhasil menambahkan: '{tugas_baru}'")
    time.sleep(1)

def hapus_tugas():
    bersihkan_layar()
    print("--- HAPUS TUGAS ---")
    
    # Tampilkan dulu daftarnya biar user tau mau hapus nomor berapa
    if len(daftar_tugas) == 0:
        print("Tidak ada tugas untuk dihapus.")
        time.sleep(1.5)
        return

    for index, tugas in enumerate(daftar_tugas, 1):
        print(f"{index}. {tugas}")

    print("-------------------")
    try:
        nomor = int(input("Hapus tugas nomor berapa? "))
        
        # Logika menghapus: Index list itu mulai dari 0, sedangkan user input mulai dari 1.
        # Jadi input user harus dikurang 1.
        if 1 <= nomor <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas.pop(nomor - 1)
            print(f"\n🗑️ Tugas '{tugas_dihapus}' telah dihapus.")
        else:
            print("\n❌ Nomor tidak ditemukan!")
            
    except ValueError:
        print("\n❌ Masukkan angka yang benar!")
    
    time.sleep(1.5)

def main():
    while True:
        bersihkan_layar()
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            lihat_tugas()
        elif pilihan == '2':
            tambah_tugas()
        elif pilihan == '3':
            hapus_tugas()
        elif pilihan == '4':
            print("Sampai jumpa! Semangat nugasnya.")
            break
        else:
            print("Pilihan tidak valid.")
            time.sleep(1)

if __name__ == "__main__":
    main()