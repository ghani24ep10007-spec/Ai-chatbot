import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

print("=== SEDANG MENGAMBIL DAFTAR MODEL DARI GOOGLE... ===")

try:
    # Minta daftar model ke Google
    models = genai.list_models()
    
    found = False
    for m in models:
        # Kita cuma cari model yang bisa generate text (generateContent)
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Model Tersedia: {m.name}")
            found = True
            
    if not found:
        print("❌ Tidak ada model yang ditemukan. Cek API Key.")

except Exception as e:
    print(f"Error Parah: {e}")