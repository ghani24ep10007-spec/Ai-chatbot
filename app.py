import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- KONFIGURASI HALAMAN WEBSITE ---
st.set_page_config(
    page_title="Ghani AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --- LOAD API KEY ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ API Key belum ditemukan. Cek file .env kamu!")
    st.stop()

# --- KONFIGURASI GEMINI ---
genai.configure(api_key=api_key)
# Menggunakan model terbaru yang tersedia di akunmu
model = genai.GenerativeModel('gemini-2.5-flash')

# --- JUDUL WEBSITE ---
st.title("🤖 Ghani AI Assistant")
st.caption("Chatbot pintar berbasis Google Gemini 2.5 Flash | Dibuat dengan Python")

# --- INITIALIZE CHAT HISTORY ---
# Ini supaya chatnya tidak hilang saat website refresh
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- TAMPILKAN HISTORY CHAT DI LAYAR ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- INPUT USER ---
if prompt := st.chat_input("Ketik pesan untuk Ghani AI..."):
    # 1. Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)
    # 2. Simpan ke history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 3. Proses balasan AI
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Kirim history chat sebelumnya supaya AI ingat konteks
            # (Streamlit perlu kita handle history-nya manual sedikit)
            chat = model.start_chat(history=[
                {"role": "user" if m["role"] == "user" else "model", "parts": m["content"]}
                for m in st.session_state.messages[:-1] # Ambil semua kecuali yg baru dikirim
            ])
            
            response = chat.send_message(prompt, stream=True)
            
            # Efek ngetik
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
            # 4. Simpan balasan AI ke history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error: {e}")