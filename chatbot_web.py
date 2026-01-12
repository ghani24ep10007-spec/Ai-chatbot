import streamlit as st
import time
import random

# --- KONFIGURASI HALAMAN WEB ---
st.set_page_config(
    page_title="AI Asisten Mahasiswa",
    page_icon="🤖",
    layout="centered"
)

# --- OTAK BUATAN (AI LOGIC) ---
# Di sini kita membuat logika sederhana (Rule-Based)
# Nanti bisa diganti dengan Machine Learning beneran kalau sudah jago
def dapatkan_respon_ai(pesan_user):
    pesan_user = pesan_user.lower()
    
    # Database Jawaban (Kamus)
    if "halo" in pesan_user or "hai" in pesan_user:
        return random.choice([
            "Halo! Ada yang bisa saya bantu terkait kuliah?",
            "Hai! Saya asisten virtualmu. Mau tanya apa?",
            "Halo Rizqi! Semangat belajar hari ini."
        ])
    
    elif "siapa namamu" in pesan_user:
        return "Saya adalah Bot Asisten Sistem Informasi v1.0."
    
    elif "matkul" in pesan_user or "mata kuliah" in pesan_user:
        return "Semester 3 biasanya belajar: Struktur Data, Basis Data, dan Statistik."
    
    elif "dosen" in pesan_user:
        return "Untuk info dosen, silakan cek website resmi kampus atau tanya Kak Tingkat ya."
    
    elif "tugas" in pesan_user:
        return "Jangan lupa kerjakan tugas Machine Learning dan Web Development. Deadline makin dekat!"
    
    elif "galau" in pesan_user or "sedih" in pesan_user:
        return "Jangan sedih. Coding memang berat, tapi kamu pasti bisa! Istirahat dulu sana."
    
    else:
        # Jawaban Default kalau AI bingung
        return random.choice([
            "Maaf, saya belum mengerti maksudmu. Coba tanya hal lain tentang kuliah.",
            "Wah, pertanyaan menarik. Tapi database saya belum update soal itu.",
            "Bisa diulangi dengan kalimat yang lebih sederhana?"
        ])

# --- EFEK MENGETIK (TYPING EFFECT) ---
def stream_data(teks):
    for kata in teks.split(" "):
        yield kata + " "
        time.sleep(0.05) # Kecepatan ngetik

# --- ANTARMUKA WEB (UI) ---
st.title("🤖 Chatbot Pintar SI")
st.caption("Asisten Pribadi Rizqi Ghani Adinata | Powered by Python")

# 1. Inisialisasi Riwayat Chat (Session State)
# Ini gunanya biar chat lama gak hilang saat kita ngetik baru
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Tampilkan Riwayat Chat di Layar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Input User (Kotak Chat di Bawah)
if prompt := st.chat_input("Ketik pesanmu di sini..."):
    # Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Simpan pesan user ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # --- PROSES AI MENJAWAB ---
    respon_mentah = dapatkan_respon_ai(prompt)
    
    with st.chat_message("assistant"):
        # Pakai efek ngetik biar keren
        response = st.write_stream(stream_data(respon_mentah))
    
    # Simpan jawaban AI ke riwayat
    st.session_state.messages.append({"role": "assistant", "content": respon_mentah})