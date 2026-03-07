"""
VEX SUPER AI - Grafik Arayüzü Uygulaması
==========================================
Güzel ve modern yapay zeka arayüzü + OpenCV
"""

import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
import random
import numpy as np
import datetime
import string
import re
import requests

# --- OpenCV ---
try:
    import cv2
    CV2_AVAILABLE = True
except:
    CV2_AVAILABLE = False

# --- GEMINI AI ---
try:
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyD21iLD8C6NZz5fARyvB2AqxatO92vQfGk")
    model = genai.GenerativeModel('gemini-1.5-flash')
    AI_AVAILABLE = True
except:
    AI_AVAILABLE = False

class VexSuperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VEX SUPER AI - Yapay Zeka Asistanı")
        self.root.geometry("900x750")
        self.root.configure(bg="#1a1a2e")
        
        self.quiz_score = 0
        self.quiz_question = None
        
        self.setup_styles()
        self.create_header()
        self.create_chat_area()
        self.create_input_area()
        self.create_status_bar()
        
        self.is_thinking = False
        
        self.add_message("VEX SUPER AI", f"""
🎉 VEX SUPER AI'ya Hoş Geldiniz!

🤖 Yeni Özellikler:
• 💱 Para Birimi Dönüştürücü
• 📏 Birim Dönüştürücü  
• 🎲 Rastgele Sayı Üretici
• 🔐 Şifre Üretici
• ❓ Quiz Oyunu
• 🌤️ Gerçek Hava Durumu
• 📰 Haber Başlıkları
• 🎨 Görsel Açıklaması
• 💻 Kod Örnekleri
• 🌐 Dil Çevirisi
• ✏️ Cümle Düzeltme
• 🖼️ OpenCV Görüntü İşleme

OpenCV Durumu: {"✅ Aktif" if CV2_AVAILABLE else "❌ Pasif"}
🖼️ OpenCV ile görüntü oluştur, oku, kaydet!

Komut yazın veya sohbet edin!
        """, "ai")
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TFrame", background="#1a1a2e")
        self.style.configure("TLabel", background="#1a1a2e", foreground="#ffffff")
        self.style.configure("TEntry", fieldbackground="#16213e", foreground="#ffffff", borderwidth=0)
        self.style.configure("TButton", background="#0f3460", foreground="#ffffff", borderwidth=0, padding=10)
        self.style.map("TButton", background=[("active", "#e94560")])
    
    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#0f3460", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🤖 VEX SUPER AI + OpenCV", font=("Helvetica", 20, "bold"), bg="#0f3460", fg="#ffffff")
        title_label.pack(side="left", padx=20, pady=20)
        
        self.status_indicator = tk.Label(header_frame, text="●", font=("Arial", 16), bg="#0f3460", fg="#00ff00")
        self.status_indicator.pack(side="right", padx=20)
        
        self.status_label = tk.Label(header_frame, text="Hazır", font=("Arial", 10), bg="#0f3460", fg="#aaaaaa")
        self.status_label.pack(side="right", padx=5)
    
    def create_chat_area(self):
        chat_container = tk.Frame(self.root, bg="#1a1a2e")
        chat_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(chat_container)
        scrollbar.pack(side="right", fill="y")
        
        self.chat_text = scrolledtext.ScrolledText(chat_container, wrap="word", font=("Helvetica", 11), bg="#16213e", fg="#ffffff", insertbackground="#ffffff", borderwidth=0, padx=15, pady=15)
        self.chat_text.pack(fill="both", expand=True)
        self.chat_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.chat_text.yview)
        
        self.chat_text.tag_config("user", foreground="#4ecca3", font=("Helvetica", 11, "bold"))
        self.chat_text.tag_config("ai", foreground="#00d4ff", font=("Helvetica", 11, "bold"))
        self.chat_text.tag_config("system", foreground="#ffd700", font=("Helvetica", 10, "italic"))
        self.chat_text.tag_config("error", foreground="#ff6b6b")
        self.chat_text.tag_config("code", foreground="#ffa500", font=("Courier", 10))
        
        self.chat_text.bind('<Configure>', lambda event: self.chat_text.see("end"))
    
    def create_input_area(self):
        input_frame = tk.Frame(self.root, bg="#16213e", height=80)
        input_frame.pack(fill="x", padx=10, pady=(0, 10))
        input_frame.pack_propagate(False)
        
        self.input_entry = tk.Entry(input_frame, font=("Helvetica", 12), bg="#1a1a2e", fg="#ffffff", insertbackground="#ffffff", borderwidth=0, relief="flat")
        self.input_entry.pack(side="left", fill="both", expand=True, padx=(15, 5), pady=15)
        self.input_entry.bind("<Return>", self.send_message)
        
        send_button = tk.Button(input_frame, text="Gönder ➤", font=("Helvetica", 11, "bold"), bg="#e94560", fg="#ffffff", borderwidth=0, relief="flat", cursor="hand2", command=self.send_message, activebackground="#ff6b6b", activeforeground="#ffffff")
        send_button.pack(side="right", padx=(5, 15), pady=15)
        
        clear_button = tk.Button(input_frame, text="Temizle", font=("Helvetica", 10), bg="#0f3460", fg="#ffffff", borderwidth=0, relief="flat", cursor="hand2", command=self.clear_chat)
        clear_button.pack(side="right", padx=5)
    
    def create_status_bar(self):
        status_frame = tk.Frame(self.root, bg="#0f3460", height=25)
        status_frame.pack(fill="x")
        status_frame.pack_propagate(False)
        
        cv_status = "🖼️ OpenCV: ✅" if CV2_AVAILABLE else "🖼️ OpenCV: ❌"
        self.ai_status = tk.Label(status_frame, text=cv_status, font=("Arial", 9), bg="#0f3460", fg="#00ff00")
        self.ai_status.pack(side="left", padx=10)
        
        version = tk.Label(status_frame, text="VEX SUPER AI v5.0", font=("Arial", 9), bg="#0f3460", fg="#aaaaaa")
        version.pack(side="top", padx=10)
        
        self.time_label = tk.Label(status_frame, text="", font=("Arial", 9), bg="#0f3460", fg="#aaaaaa")
        self.time_label.pack(side="right", padx=10)
        
        self.update_time()
    
    def update_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=now)
        self.root.after(1000, self.update_time)
    
    def add_message(self, sender, message, msg_type="system"):
        self.chat_text.config(state="normal")
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        if msg_type == "user":
            self.chat_text.insert("end", f"\n{sender} ", "user")
        elif msg_type == "ai":
            self.chat_text.insert("end", f"\n🤖 {sender} ", "ai")
        else:
            self.chat_text.insert("end", f"\n[{timestamp}] ", "system")
        
        self.chat_text.insert("end", f"{message}\n")
        self.chat_text.see("end")
        self.chat_text.config(state="disabled")
    
    def send_message(self, event=None):
        message = self.input_entry.get().strip()
        if not message:
            return
        
        self.input_entry.delete(0, "end")
        self.add_message("Siz", message, "user")
        self.set_thinking(True)
        
        thread = threading.Thread(target=self.get_ai_response, args=(message,))
        thread.daemon = True
        thread.start()
    
    def get_ai_response(self, message):
        try:
            response = self.process_message(message)
            self.root.after(0, lambda: self.add_message("VEX", response, "ai"))
        except Exception as e:
            self.root.after(0, lambda: self.add_message("HATA", str(e), "error"))
        finally:
            self.root.after(0, lambda: self.set_thinking(False))
    
    # ========== OpenCV ÖZELLİKLERİ ==========
    
    def opencv_tutorial(self):
        """OpenCV öğretici"""
        return """🖼️ OpenCV Görüntü İşleme:

OpenCV, görüntü işleme için Python kütüphanesidir.

📥 Resim Okuma:
```python
import cv2
resim = cv2.imread("resim.png")
```

💾 Resim Kaydetme:
```python
cv2.imwrite("yeni_resim.png", resim)
```

🖼️ Resim Gösterme:
```python
cv2.imshow("Pencere", resim)
cv2.waitKey()
```

🎨 NumPy ile Görüntü Oluşturma:
```python
import numpy as np
import cv2

# Tek piksel (BGR)
piksel = np.array([150, 150, 150], dtype=np.uint8)

# 3x3 Renkli görüntü
resim = np.array([[[255,0,0],[0,255,0],[0,0,255]]], dtype=np.uint8)

# 2x3x3 Görüntü (2 satır, 3 sütun, 3 kanal)
resim = np.array([[[255,0,0],[0,255,0],[0,0,255]],
                  [[255,255,0],[255,0,255],[0,255,255]]], dtype=np.uint8)

cv2.imshow("Resim", resim)
cv2.imwrite("cikti.png", resim)
cv2.waitKey()
```

📊 Temel Bilgiler:
• uint8: 0-255 arası tam sayı
• [B, G, R]: Mavi, Yeşil, Kırmızı sırası
• 1D dizi: Tek piksel
• 2D dizi: Siyah-beyaz görüntü
• 3D dizi: Renkli görüntü (yükseklik x genişlik x 3)
"""
    
    def opencv_demo(self):
        """OpenCV demo görüntü oluştur"""
        if not CV2_AVAILABLE:
            return "❌ OpenCV kurulu değil!\n\nKurmak için: pip install opencv-python"
        
        try:
            # 100x100 lile görüntü oluştur
            # Kırmızı, Yeşil, Mavi dikdörtgenler
            img = np.zeros((100, 100, 3), dtype=np.uint8)
            
            # Kırmızı (0-33 piksel)
            img[0:33, :] = [0, 0, 255]  # BGR
            
            # Yeşil (33-66 piksel)
            img[33:66, :] = [0, 255, 0]
            
            # Mavi (66-100 piksel)
            img[66:100, :] = [255, 0, 0]
            
            # Kaydet
            cv2.imwrite("opencv_demo.png", img)
            
            return """🖼️ OpenCV Demo Görüntü Oluşturuldu!

Dosya: opencv_demo.png

Bu görüntü:
• 100x100 piksel
• 3 kanal (BGR)
• Kırmızı, Yeşil, Mavi bantlar içerir

Kod:
```python
import numpy as np
import cv2

img = np.zeros((100, 100, 3), dtype=np.uint8)
img[0:33, :] = [0, 0, 255]   # Kırmızı
img[33:66, :] = [0, 255, 0]  # Yeşil
img[66:100, :] = [255, 0, 0] # Mavi

cv2.imwrite("demo.png", img)
```
"""
        except Exception as e:
            return f"❌ Hata: {str(e)}"
    
    def numpy_image_info(self):
        """NumPy görüntü bilgileri"""
        return """📊 NumPy ile Görüntü Bilgileri:

🔢 1D Dizi (Tek Piksel):
```python
dizi = np.array([150, 150, 150], dtype=np.uint8)
print(dizi.dtype)  # uint8
```

🔢 2D Dizi (Siyah-Beyaz):
```python
dizi = np.array([[255, 0, 255],
                 [0, 255, 0]], dtype=np.uint8)
```

🔢 3D Dizi (Renkli):
```python
# 1x3 piksel, 3 kanal
dizi = np.array([[[255,0,0],[0,255,0],[0,0,255]]], dtype=np.uint8)

# 2x3 piksel, 3 kanal
dizi = np.array([[[255,0,0],[0,255,0],[0,0,255]],
                  [[255,255,0],[255,0,255],[0,255,255]]], dtype=np.uint8)
```

📌 Notlar:
• dtype=np.uint8 → 0-255 arası değerler
• [B, G, R] sırasıyla mavi, yeşil, kırmızı
• cv2.imshow() ile gösterilir
• cv2.imwrite() ile kaydedilir
"""
    
    def process_message(self, message):
        """Mesajı işle"""
        m = message.lower()
        
        # ========== OpenCV ÖZELLİKLERİ ==========
        
        # OpenCV öğretici
        if "opencv" in m or "görüntü" in m or "resim" in m or "cv2" in m:
            if "demo" in m or "örnek" in m or "oluştur" in m:
                return self.opencv_demo()
            if "numpy" in m or "dizi" in m or "bilgi" in m:
                return self.numpy_image_info()
            return self.opencv_tutorial()
        
        # Gerçek hava durumu
        if "hava" in m or "weather" in m or "derece" in m:
            return self.get_real_weather()
        
        # Cümle düzeltme
        if "düzelt" in m or "türkçe" in m or "dilbilgi" in m or "yazım" in m:
            if len(message.split()) > 2:
                return self.correct_sentence(message)
            return self.correct_sentence("Örnek cümle")
        
        # Cümle analizi
        if "analiz" in m or "kelime" in m:
            if len(message.split()) > 2:
                return self.analyze_sentence(message)
            return self.analyze_sentence("Örnek cümle")
        
        # Para birimi
        if "para" in m or "currency" in m or "dönüştür" in m:
            return self.currency_converter(m)
        
        # Birim
        if "birim" in m or "unit" in m or "çevir" in m:
            return self.unit_converter()
        
        # Rastgele sayı
        if "rastgele" in m or "random" in m or "zar" in m:
            return self.random_number(m)
        
        # Şifre
        if "şifre" in m or "sifre" in m or "parola" in m or "password" in m:
            return self.password_generator(m)
        
        # Quiz
        if "quiz" in m or "bilgi" in m or "sor" in m:
            return self.quiz_game(m)
        
        # Haber
        if "haber" in m or "news" in m or "gündem" in m:
            return self.news_headlines()
        
        # NumPy
        if "numpy" in m or "dizi" in m:
            arr = np.array([1, 2, 3, 4, 5])
            return f"📊 NumPy Dizi:\n{arr}\n\nToplam: {np.sum(arr)}\nOrtalama: {np.mean(arr)}\n\n" + self.numpy_image_info()
        
        # ========== TEMEL ÖZELLİKLER ==========
        
        # Selamlama
        if any(word in m for word in ["merhaba", "selam", "hi", "hello", "hey"]):
            return "👋 Merhaba! Size nasıl yardımcı olabilirim?"
        
        # Yardım
        if "yardım" in m or "help" in m or "komut" in m:
            return """📚 KOMUT LİSTESİ:

🖼️ opencv - OpenCV öğretici
🖼️ opencv demo - Görüntü oluştur
📊 numpy - NumPy bilgi
🌤️ hava - Gerçek hava durumu
✏️ düzelt - Cümle düzeltme
💱 para - Para birimi
📏 birim - Birim dönüştür
🎲 rastgele - Rastgele sayı
🔐 şifre - Şifre oluştur
❓ quiz - Bilgi yarışması
"""
        
        # Hesaplama
        if any(word in m for word in ["hesapla", "kaç", "topla", "çarp"]):
            try:
                nums = re.findall(r'\d+', message)
                if len(nums) >= 2:
                    result = int(nums[0]) + int(nums[1])
                    return f"✏️ Sonuç: {result}"
            except:
                pass
        
        # ========== GEMINI AI ==========
        if AI_AVAILABLE:
            try:
                response = model.generate_content(message)
                return response.text
            except:
                return "🤔 Bunu düşünüyor... Lütfen biraz bekleyin."
        else:
            return "🤖 AI sistemi dışarı. Normal sohbet edebiliriz!"

    # ========== DİĞER METOTLAR ==========
    
    def get_real_weather(self):
        try:
            url = "https://api.open-meteo.com/v1/forecast?latitude=41.0082&longitude=28.9784&current=temperature_2m,weather_code,relative_humidity_2m,wind_speed_10m"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                current = data.get("current", {})
                temp = current.get("temperature_2m", 0)
                humidity = current.get("relative_humidity_2m", 0)
                wind = current.get("wind_speed_10m", 0)
                code = current.get("weather_code", 0)
                weather_desc = self.get_weather_description(code)
                return f"""🌤️ GERÇEK HAVA DURUMU (İstanbul):
🌡️ Sıcaklık: {temp}°C
☁️ Durum: {weather_desc}
💧 Nem: %{humidity}
🌬️ Rüzgar: {wind} km/s"""
            return self.get_simulated_weather()
        except:
            return self.get_simulated_weather()
    
    def get_weather_description(self, code):
        codes = {0: "Açık", 1: "Parçalı Bulutlu", 2: "Bulutlu", 3: "Kapalı", 45: "Sisli", 51: "Çisenti", 61: "Yağmurlu", 71: "Karlı", 95: "Fırtına"}
        return codes.get(code, "Bilinmiyor")
    
    def get_simulated_weather(self):
        return f"🌤️ Hava Durumu:\nSıcaklık: {random.randint(10, 25)}°C\nDurum: {random.choice(['Güneşli', 'Bulutlu', 'Yağmurlu'])}"
    
    def correct_sentence(self, text):
        corrections = []
        if "ı" in text.lower() and "i" in text:
            corrections.append("Türkçe'de 'ı' ve 'i' doğru kullanılmalı")
        if not text.endswith(".") and len(text) > 10:
            corrections.append("Cümle nokta ile bitmeli")
        result = f"✏️ CÜMLE ANALİZİ:\n\n📝: \"{text}\"\n📊 Kelime: {len(text.split())}"
        if corrections:
            result += "\n🔧: " + ", ".join(corrections)
        return result
    
    def analyze_sentence(self, text):
        words = text.split()
        freq = {}
        for word in words:
            freq[word.lower()] = freq.get(word.lower(), 0) + 1
        result = f"🔍 ANALİZ:\n📝: \"{text}\"\n📊 Kelime: {len(words)}\n📈 En sık: "
        result += ", ".join([f"'{k}'({v})" for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]])
        return result
    
    def currency_converter(self, m):
        rates = {"USD": 1.0, "EUR": 0.92, "TRY": 32.50}
        return "💱 Dönüşüm:\n" + "\n".join([f"1 {k} = {v:.2f} TRY" for k, v in rates.items()])
    
    def unit_converter(self):
        return "📏 Birim:\n1 km = 1000 m\n1 kg = 1000 g\n°C→°F: (°C×9/5)+32"
    
    def random_number(self, m):
        nums = re.findall(r'\d+', m)
        if nums:
            return f"🎲: {random.randint(1, int(nums[0]))}"
        return f"🎲: {random.randint(1, 100)}"
    
    def password_generator(self, m):
        length = int(re.findall(r'\d+', m)[0]) if re.findall(r'\d+', m) else 12
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return f"🔐 Şifre:\n`{''.join(random.choice(chars) for _ in range(length))}`"
    
    def quiz_game(self, m):
        questions = [
            {"s": "Türkiye'nin başkenti?", "a": "ankara"},
            {"s": "Python'un kurucusu?", "a": "guido van rossum"},
            {"s": "Dünya'nın en büyük okyanusu?", "a": "pasifik"},
        ]
        if not self.quiz_question or "yeni" in m:
            self.quiz_question = random.choice(questions)
            return f"❓ {self.quiz_question['s']}"
        if self.quiz_question:
            if m.lower().strip() == self.quiz_question['a']:
                self.quiz_score += 10
                self.quiz_question = None
                return f"✅ Doğru! +10 puan\nToplam: {self.quiz_score}"
            return f"❌ Yanlış! Cevap: {self.quiz_question['a']}"
        return "Quiz için 'quiz' yazın"
    
    def news_headlines(self):
        return "📰 HABERLER:\n" + "\n".join([f"• {h}" for h in random.sample(["Teknoloji gelişiyor", "Spor haberleri", "Ekonomi", "Dünya", "Bilim"], 5)])
    
    def set_thinking(self, thinking):
        self.is_thinking = thinking
        if thinking:
            self.status_indicator.config(text="●", fg="#ffd700")
            self.status_label.config(text="Düşünüyor...")
        else:
            self.status_indicator.config(text="●", fg="#00ff00")
            self.status_label.config(text="Hazır")
    
    def clear_chat(self):
        self.chat_text.config(state="normal")
        self.chat_text.delete(1.0, "end")
        self.chat_text.config(state="disabled")
        self.add_message("VEX", "Sohbet temizlendi!", "ai")
    
    def on_closing(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    try:
        root.iconbitmap("icon.ico")
    except:
        pass
    app = VexSuperGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
