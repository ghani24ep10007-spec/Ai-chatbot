import random
import os

def main():
    # Bersihkan layar terminal biar rapi
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("==============================")
    print("   GAME TEBAK ANGKA (CLI)     ")
    print("==============================")
    print("Saya memikirkan angka 1 - 100")
    print("Coba tebak angka berapa itu!")
    print("------------------------------")

    angka_rahasia = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0

    while tebakan != angka_rahasia:
        try:
            input_user = input("Masukkan tebakanmu: ")
            tebakan = int(input_user)
            jumlah_tebakan += 1

            if tebakan < angka_rahasia:
                print("❌ Terlalu RENDAH! Coba lagi.\n")
            elif tebakan > angka_rahasia:
                print("❌ Terlalu TINGGI! Coba lagi.\n")
            else:
                print(f"\n🎉 SELAMAT! Angkanya adalah {angka_rahasia}.")
                print(f"Kamu berhasil menebak dalam {jumlah_tebakan} kali percobaan.")
        
        except ValueError:
            print("⚠️ Harap masukkan angka saja!\n")

if __name__ == "__main__":
    main()