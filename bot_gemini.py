import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Konfigurasi API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: API Key belum ada di file .env!")
    exit()

genai.configure(api_key=api_key)

# 2. Setup Model
# Menggunakan 'gemini-pro' (teks saja)
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. Mulai Chat (History kosong)
chat_session = model.start_chat(history=[])

print("=== Chatbot Ghani (Powered by Gemini) ===")
print("Ketik 'keluar' untuk berhenti.\n")

while True:
    # Input User
    user_input = input("Ghani: ")
    
    if user_input.lower() in ["keluar", "exit"]:
        print("Bot: Sampai jumpa lagi!")
        break

    if user_input.strip() == "":
        continue

    try:
        # Kirim pesan ke Gemini
        # stream=True biar efek ngetiknya muncul pelan-pelan (keren!)
        response = chat_session.send_message(user_input, stream=True)
        
        print("Bot: ", end="")
        for chunk in response:
            print(chunk.text, end="")
        print("\n") # Enter baru setelah selesai

    except Exception as e:
        print(f"\nError: {e}")