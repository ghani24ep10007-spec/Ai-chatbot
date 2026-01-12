import random
import os

# --- ASET GAMBAR (ASCII ART) ---
# Ini gambar orang digantung dari tiang, bertahap dari kosong sampai mati.
# Serem tapi keren buat belajar coding!
GAMBAR_HANGMAN = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

# Database kata-kata (bisa kamu tambah sendiri)
KUMPULAN_KATA = [
    "PYTHON", "ALGORITMA", "KOMPUTER", "PROGRAMMER", 
    "INTERNET", "DATABASE", "VARIABLE", "WINDOWS", 
    "LINUX", "KEYBOARD", "MONITOR", "SYSTEM"
]

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # 1. Pilih kata acak
    kata_rahasia = random.choice(KUMPULAN_KATA)
    panjang_kata = len(kata_rahasia)
    
    # 2. Siapkan variabel
    nyawa = 6  # Kesempatan salah (sesuai jumlah gambar - 1)
    huruf_ditebak = [] # List untuk menyimpan huruf yang sudah diketik user
    game_over = False

    while not game_over:
        bersihkan_layar()
        print("=== GAME HANGMAN: TEBAK KATA IT ===")
        
        # Tampilkan gambar sesuai sisa nyawa
        # (6 - nyawa) artinya: kalau nyawa 6, index 0. Kalau nyawa 0, index 6.
        index_gambar = 6 - nyawa
        print(GAMBAR_HANGMAN[index_gambar])
        
        print(f"Nyawa tersisa: {nyawa}")
        print("Huruf yang sudah dipakai:", ", ".join(huruf_ditebak))
        print("\n")

        # 3. Tampilkan status kata (Contoh: P _ T H _ N)
        tampilan_kata = ""
        huruf_benar_semua = True # Anggap benar dulu, nanti dicek
        
        for huruf in kata_rahasia:
            if huruf in huruf_ditebak:
                tampilan_kata += huruf + " "
            else:
                tampilan_kata += "_ "
                huruf_benar_semua = False # Masih ada yg belum ditebak
        
        print(f"TEBAK KATA:  {tampilan_kata}")
        print("\n")

        # --- CEK KONDISI MENANG/KALAH ---
        
        if huruf_benar_semua:
            print(f"🎉 SELAMAT! Kamu berhasil menebak: {kata_rahasia}")
            break

        if nyawa == 0:
            print(f"💀 GAME OVER! Orang itu telah dihukum...")
            print(f"Kata yang benar adalah: {kata_rahasia}")
            break

        # --- INPUT USER ---
        tebakan = input("Masukkan satu huruf: ").upper()

        # Validasi input
        if len(tebakan) != 1 or not tebakan.isalpha():
            print("⚠️ Masukkan satu huruf saja (A-Z)!")
            input("Tekan Enter...")
            continue
        
        if tebakan in huruf_ditebak:
            print(f"⚠️ Kamu sudah menebak huruf '{tebakan}' sebelumnya!")
            input("Tekan Enter...")
            continue

        # Masukkan ke list huruf yg sudah ditebak
        huruf_ditebak.append(tebakan)

        # Cek apakah tebakan benar atau salah
        if tebakan in kata_rahasia:
            print(f"✅ Mantap! Huruf '{tebakan}' ada.")
        else:
            print(f"❌ Yah... Huruf '{tebakan}' tidak ada.")
            nyawa -= 1 # Kurangi nyawa
            
        # Jeda sebentar biar user sempat baca "Benar/Salah"
        # (Opsional, bisa pakai time.sleep, tapi input() juga cukup)
        # input("Lanjut...") 

if __name__ == "__main__":
    main()