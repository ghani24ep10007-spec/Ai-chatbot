import time
import os

# Kumpulan Data Soal (List of Dictionaries)
# Kamu bisa tambah soal sesukamu di sini
bank_soal = [
    {
        "pertanyaan": "Apa nama ibu kota negara Indonesia?",
        "pilihan": ["A. Bandung", "B. Surabaya", "C. Jakarta", "D. Medan"],
        "jawaban": "C"
    },
    {
        "pertanyaan": "Hewan apa yang memakan bambu?",
        "pilihan": ["A. Panda", "B. Koala", "C. Gajah", "D. Jerapah"],
        "jawaban": "A"
    },
    {
        "pertanyaan": "Berapa hasil dari 5 + 5 x 2?",
        "pilihan": ["A. 20", "B. 15", "C. 10", "D. 25"],
        "jawaban": "B"
    },
    {
        "pertanyaan": "Bahasa pemrograman apa yang sedang kita pakai ini?",
        "pilihan": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "jawaban": "C"
    },
    {
        "pertanyaan": "Siapa pendiri Microsoft?",
        "pilihan": ["A. Steve Jobs", "B. Bill Gates", "C. Elon Musk", "D. Mark Zuckerberg"],
        "jawaban": "B"
    }
]

def bersihkan_layar():
    # Perintah untuk membersihkan terminal (cls di Windows, clear di Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    bersihkan_layar()
    print("=================================")
    print("   SELAMAT DATANG DI KUIS PINTAR  ")
    print("=================================")
    print("Jawablah dengan mengetik A, B, C, atau D.\n")
    
    skor = 0
    jumlah_soal = len(bank_soal)

    # Loop untuk setiap soal di dalam bank_soal
    for nomor, butir_soal in enumerate(bank_soal, 1):
        print(f"Soal No. {nomor}:")
        print(butir_soal["pertanyaan"])
        
        # Tampilkan pilihan jawaban
        for opsi in butir_soal["pilihan"]:
            print(opsi)
        
        # Minta input user
        tebakan = input("Jawab: ").upper() # .upper() biar huruf kecil jadi besar (a -> A)

        # Cek jawaban
        if tebakan == butir_soal["jawaban"]:
            print("✅ Benar!\n")
            skor += 1
        else:
            print(f"❌ Salah! Jawaban yang benar adalah {butir_soal['jawaban']}\n")
        
        time.sleep(1) # Jeda 1 detik biar enak dilihat

    # Tampilkan hasil akhir
    print("=================================")
    print(f"Kuis Selesai! Skor kamu: {skor} dari {jumlah_soal}")
    nilai = (skor / jumlah_soal) * 100
    print(f"Nilai Akhir: {int(nilai)}")
    
    if nilai == 100:
        print("🎉 Sempurna! Kamu jenius!")
    elif nilai >= 60:
        print("👍 Bagus! Tingkatkan lagi.")
    else:
        print("📚 Jangan menyerah, belajar lagi ya!")

if __name__ == "__main__":
    main()