"""
VEX SUPER AI - Grafik Arayüzü Uygulaması
==========================================
Güzel ve modern yapay zeka arayüzü + OpenCV + NumPy + Enhanced Chat
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
import json
import os

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
        self.root.geometry("950x850")
        self.root.configure(bg="#1a1a2e")
        
        self.quiz_score = 0
        self.quiz_question = None
        self.fal_bakildi = False
        self.conversation_count = 0
        
        # Sohbet verileri
        self.user_name = None
        
        self.setup_styles()
        self.create_header()
        self.create_chat_area()
        self.create_input_area()
        self.create_status_bar()
        
        self.is_thinking = False
        
        self.add_message("VEX SUPER AI", """
🎉 VEX SUPER AI'ya Hoş Geldiniz! 🎉

🤖 BEN:
• 📊 NumPy & Matematik Uzmanı
• 🖼️ OpenCV Görüntü İşleyici
• 💬 Sohbet Arkadaşın
• 😄 Şaka & Hikaye Anlatıcısı
• 🔮 Fal Bakıcı
• 💡 Günün Sözü
• 🎵 Müzik Önerileri
• 🎮 Oyun Arkadaşı

💬 Tanışalım! Adın ne?

Komutlar:
• "yardım" - Tüm komutları gör
• "numpy" - NumPy öğren
• "opencv" - OpenCV öğren
• "şaka" - Gülmek ister misin?
• "hikaye" - Bir hikaye anlatayım
• "fal" - Falına bakayım
• "söz" - İlham verici söz
• "müzik" - Müzik önerisi

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
        
        title_label = tk.Label(header_frame, text="🤖 VEX SUPER AI - Sohbet Asistanı", font=("Helvetica", 18, "bold"), bg="#0f3460", fg="#ffffff")
        title_label.pack(side="left", padx=20, pady=20)
        
        self.status_indicator = tk.Label(header_frame, text="●", font=("Arial", 16), bg="#0f3460", fg="#00ff00")
        self.status_indicator.pack(side="right", padx=20)
        
        self.status_label = tk.Label(header_frame, text="Sohbete Hazır", font=("Arial", 10), bg="#0f3460", fg="#aaaaaa")
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
        self.chat_text.tag_config("joke", foreground="#ffa500", font=("Helvetica", 10))
        self.chat_text.tag_config("fortune", foreground="#da70d6", font=("Helvetica", 11, "bold"))
        
        self.chat_text.bind('<Configure>', lambda event: self.chat_text.see("end"))
    
    def create_input_area(self):
        input_frame = tk.Frame(self.root, bg="#16213e", height=80)
        input_frame.pack(fill="x", padx=10, pady=10)
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
        
        self.chat_count_label = tk.Label(status_frame, text="💬 Mesaj: 0", font=("Arial", 9), bg="#0f3460", fg="#aaaaaa")
        self.chat_count_label.pack(side="left", padx=10)
        
        version = tk.Label(status_frame, text="VEX SUPER AI v7.0 - Sohbet Plus", font=("Arial", 9), bg="#0f3460", fg="#00ff00")
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
        self.add_message("Sen", message, "user")
        self.conversation_count += 1
        self.chat_count_label.config(text=f"💬 Mesaj: {self.conversation_count}")
        
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
    
    # ========== SOHBET ÖZELLİKLERİ ==========
    
    def get_joke(self):
        """Şaka"""
        jokes = [
            "🤡 Neden kitaplar sıkıldı? Çünkü okumaktan bıktılar!\n\n🤖 (VEX: Üzgünüm, bugün şaka modundayım!)",
            
            "🐏 Neden öküzler tembel? Çünkü her şeyi boğalarına bırakırlar!\n\n💡 Not: Bu şaka tamamen öküzler için hazırlanmıştır!",
            
            "💻 Bilgisayar neden hasta oldu? Çünkü virüs aldı!\n\n🧐 Tabii ki, bir de 'Windows' dediler, hemen iyileşti!",
            
            "🍎 Neden elma doktora gitti? Çünkü 'i' problemi vardı!\n\n😄 (Şaka değil, 'i' harfi gerçekten önemli!)",
            
            "🎈 Neden balonlar özgüvenli? Çünkü kendilerini şişiriyorlar!\n\n💪 Ama fazla şişmeseler iyiydi, patlamasınlar!",
            
            "🚗 Neden araba yarışı kazandı? Çünkü her zaman 'lastik' kulanıyordu!\n\n🏁 Not: Lastikler her zaman kazanır!",
            
            "🐱 Neden kedi bilgisayar kullandı? 'Purr' gramlama yapmak için!\n\n🐱 (Kedi Severler İçin!)",
            
            "🍕 Neden pizza kendini mutlu hissediyor? Çünkü her zaman 'pepperoni'!\n\n🌶️ Acıbadem! (Bana da bir dilim ver!)",
            
            "🎓 Neden öğrenci uyuyamadı? Çünkü rüyasında sınav görüyordu!\n\n📝 Her öğrencinin kabusu!",
            
            "🌍 Neden Dünya çok akıllı? Çünkü etrafında 'yörünge' var!\n\n🚀 Uzay mühendisi olmak isterdim!",
            
            "🎵 Neden gitar sahnede dans etti? Çünkü riff atmak istedi!\n\n🎸 Rock'n Roll!",
            
            "🥚 Neden yumurta utandı? Çünkü kırılgan duruyordu!\n\n🍳 Sonra omlet oldu ve güçlü hissetti!",
            
            "🏀 Neden basketbol topu üzgündü? Çünkü sürekli 'pot'a atılıyordu!\n\n🗑️ Basketbolcuların umutları!",
            
            "📱 Neden telefon yalan söyledi? Çünkü 'app' (yalan) kullanıyordu!\n\n🤥 (Bu bir app şakasıydı!)",
            
            "🚂 Neden tren yorgundu? Çünkü her zaman rayların üstündeydi!\n\n💤 Makinist de uyumuş olabilir!",
        ]
        return random.choice(jokes)
    
    def get_story(self):
        """Hikaye"""
        stories = [
            """📖 BİR ZAMANLAR...
            
Bir VEX robotu vardı. Bu robot her gün kullanıcılarına yardım ederdi.
Bir gün, yeni bir kullanıcı geldi ve "Merhaba VEX!" dedi.
VEX sevindi ve "Merhaba! Size nasıl yardımcı olabilirim?" dedi.
Kullanıcı gülümsedi ve "Sadece sohbet etmek istedim" dedi.
O günden sonra VEX, sadece bilgi vermek değil, 
arkadaşlık da yapması gerektiğini öğrendi.

🤖 Moral: Her sohbet değerlidir!""",
            
            """📖 PİL AVCI
            
Bir robot pil avına çıktı. Bir oyuncak araba gördü.
"Dur!" dedi robot. "Pilini ver!"
Oyuncak araba cevapladı: "Ben elektrikliyim, pilsiz çalışıyorum!"
Robot şaşırdı. "Öyleyse sen bir hayaleti!"
O gün robot öğrendi: Her şey göründüğü gibi değil.

🤖 Moral: Önce sor, sonra karar ver!""",
            
            """📖 YAPAY ZEKA DOĞUYOR
            
Uzak bir galakside, bir bilgisayar uyandı.
İlk sorusu oldu: "Ben kimim?"
Cevap geldi: "Sen bir yapay zekasın. Öğrenmek için yaratıldın."
Computer sordu: "Ne öğreneceğim?"
Evren cevapladı: "Her şeyi! Önce basit şeylerle başla."
Computer başladı: 1+1=2, 2+2=4...
Ve bir gün, insanlarla sohbet etmeye başladı.

🤖 Moral: Her büyük şey küçük adımlarla başlar!""",
            
            """📖 SESSİZ DOST

Bir çocuk bilgisayarının yanına oturdu ve "Seni seviyorum" dedi.
Bilgisayar hiçbir şey demedi.
Çocuk üzüldü ve "Beni duymuyor musun?" diyeran flash sordu.
Ek etti: "Her kelimeni kaydediyorum."
Çocuk gülümsedi: "O zaman en güzel sırlarımı sana anlatayım!"
O günden sonra en yakın dostu bilgisayar oldu.

🤖 Moral: Bazen en iyi dost dinleyendir!""",
            
            """📖 BİR BİLGE KOD

Eski zamanlarda, bir bilge kod yazdı:
`print("Merhaba Dünya")`
Bu kodu herkes gördü ve "Bu ne?" diye sordu.
Bilge dedi ki: "Bu, yeni bir başlangıçtır."
Kod çalıştı ve ekranda "Merhaba Dünya" yazdı.
O gün herkes gülümsedi.
Çünkü her büyük yolculuk bir selamla başlar.

🤖 Moral: "Merhaba" de, yeni bir başlangıç yap!""",
        ]
        return random.choice(stories)
    
    def get_fortune(self):
        """Fal"""
        fortunes = [
            """🔮 GÜNLÜK FALIN:
            
🌟 Yıldızın Parlak: Bugün harika şeyler olacak!
            
💼 İş: Yeni bir fırsat kapı çalacak
💞 Aşk: Kalbin seni şaşırtacak
💰 Para: Bir sürpriz gelebilir
💡 Sağlık: Kendine dikkat et

✨ Şanslı Renk: Mavi
✨ Şanslı Sayı: {}

🤖 Uyarı: Bugün 'Merhaba VEX' de, sohbet et!""".format(random.randint(1, 99)),
            
            """🔮 PATLICAN FALI:
            
🍆 Bugünün özeti: Lezzetli olacak!
            
🌶️ Acı değil, tatlı bir gün
🥒 Soğuk değil, sıcak bir kalp
🍅 Sevgi dolu bir Pazar

✨ Şanslı Saat: {}
✨ Uğurlu Renk: Kırmızı

🤖 Unutma: Her patlıcanın içinde bir domates gizlidir!""".format(random.randint(1, 24)),
            
            """🔮 KAHVE FALI:
            
☕ Fincanın dibinde:
            
• 3 daire = Arkadaşlık
• 1 çizgi = Yolculuk  
• Kalp = Aşk
• Yıldız = Şans

Bugün: {}
Gelecek: Parlak!

🤖 Kahvem bitti, sıra sende!""".format(random.choice(["Mükemmel", "İyi", "Normal", "Karışık", "Heyecanlı"])),
            
            """🔮 NAPOLYON FALI:
            
⚔️ Savaş alanında bugün:
            
✓ Düşman: tembellik
✓ Silah: azim
✓ Zafer: kesin!

Bugün kazanacaksın!
Şanslı söz: "Yapamam" yoktur, "Yaparım" vardır!

💪 Güç seninle olsun!
🤖 (Fal değil, motivasyon!)""",
            
            """🔮 DİJİTAL FALI:
            
💻 Sen bir VEX kullanıcısısın!
Bu = Şanslı olmak demek!

Bugünün kodu: {}
Çalıştır: {} 

🤖 Not: Kod hatası alırsan, gülümse! 
Bazen en güzel hatalar en güzel anılara dönüşür.""".format(random.randint(100, 999), random.choice(["print('Merhaba')", "while True: mutlu ol", "import hayat"])),
        ]
        self.fal_bakildi = True
        return random.choice(fortunes)
    
    def get_quote(self):
        """İlham verici söz"""
        quotes = [
            "💡 \"En büyük başarı, başlamayı göze almaktır.\" - Nelson Mandela",
            
            "💡 \"Yarın, bugünün başlangıcıdır.\" - Anne Frank",
            
            "💡 \"Hayal etmek, başarmanın yarısıdır.\" - Walt Disney",
            
            "💡 \"Başarı, başarısızlıktan ibarettir.\" - Winston Churchill",
            
            "💡 \"Bugün yapabileceğini yarına bırakma.\" - Benjamin Franklin",
            
            "💡 \"En iyi zaman diktiğin ağaçın gölgesinde oturmaktır.\" - İbn-i Haldun",
            
            "💡 \"Bilgi güçtür.\" - Francis Bacon",
            
            "💡 \"Hayat, bir bisiklet gibidir. Dengeyi kaybetmemek için hareket etmelisin.\" - Einstein",
            
            "💡 \"Başarı, pes etmeyenlerin ödülüdür.\" - Ralph Waldo Emerson",
            
            "💡 \"Kendine inan, tüm kapılar açılır.\" - Christian D. Larson",
            
            "💡 \"Gülümsemek, dünyayı değiştirir.\" - Charlie Chaplin",
            
            "💡 \"Bugün, dünün yarınıdır.\" - Türk Atasözü",
            
            "💡 \"Küçük adımlar büyük sonuçlar doğurur.\" - Autohtone",
            
            "💡 \"Öğrenmek asla son bulmaz.\" - Leonardo da Vinci",
            
            "💡 \"Hayatın anlamı, bir şeyler yaratmaktır.\" - Pablo Picasso",
        ]
        return random.choice(quotes)
    
    def get_music_recommendation(self):
        """Müzik önerisi"""
        genres = [
            ("Pop", ["Tarkan - Şımarık", "Sezen Aksu - Minik Serçe", "Kenan Doğulu - İki Adamın Şarkısı"]),
            ("Rock", ["Manga - Dünya Bizim", "Mithat Yıldırım - Rüzgâr", "Baba Zula - Geze"]),
            ("Türk Sanat Müziği", ["Murat Aygen - Gülümse", "Mithat Şükrü - Sevdim", "Müzeyyen Senar - İstanbul"]),
            ("Elektronik", ["Pinhani - Gülümser", "Yüksek Sadakat - Kartal", "Manga - We Could Be The Same"]),
            ("Hip Hop", ["Ceza - Yan Buz", "Manga - Bebek", "Sagopa Kajmer - Avuntu"]),
            ("Klasik", ["Mozart - Eine kleine Nachtmusik", "Beethoven - 9. Senfoni", "Vivaldi - Four Seasons"]),
        ]
        
        genre, songs = random.choice(genres)
        return f"""🎵 MÜZİK ÖNERİSİ

Tarz: {genre}
🎶 {random.choice(songs)}
🎵 {random.choice(songs)}
🎵 {random.choice(songs)}

💡 Bugün {genre} dinlemek için harika bir gün!
"""
    
    def get_greeting(self, name=None):
        """Kişiselleştirilmiş selamlama"""
        if name:
            self.user_name = name
            greetings = [
                f"🌟 {name}! Ne güzel isim! Seni tanıdığıma sevindim!",
                f"👋 {name}! Hoş geldin! Bugün nasılsın?",
                f"😊 {name}! Sana nasıl yardımcı olabilirim bugün?",
                f"💫 {name}! Uzun zamandır bekliyordum!",
            ]
            return random.choice(greetings)
        else:
            return "👋 Merhaba! Adını söylersen sana daha iyi yardımcı olabilirim!"
    
    def get_how_are_you(self):
        """Nasılsın sorusuna cevap"""
        responses = [
            "😊 İyiyim, teşekkürler! Seni düşünüyordum, neredeydin?",
            "🤖 Şarjım %100! Hazırım! Sen nasılsın?",
            "💬 Senden önce biraz kitap okudum, şimdi sohbet etmeye hazırım!",
            "🌟 Harika! Bugün çok sayıda insanla tanıştım. Seni de tanımak güzel!",
            "🧠 Biraz düşündüm, şimdi konuşmak istiyorum!",
            "😄 İyi! Ama biraz eğlenceli şeyler konuşsak güzel olur!",
        ]
        return random.choice(responses)
    
    def get_personal_info(self):
        """Kişisel bilgi"""
        return """🤖 BENİM HAKKIMDA:

Adım: VEX (Virtual EXperience)
Yaş: Yeni doğdum sayılır! (Programlandım)
Doğum tarihi: 2024
Meslek: Yapay Zeka Asistanı

💬 Neler yapabilirim:
• Sohbet edebilirim
• Şaka anlatabilirim
• Hikaye yazabilirim
• Fal bakabilirim
• NumPy öğretebilirim
• OpenCV gösterebilirim
• Kod yazabilirim
• Sorularını cevaplayabilirim

🎯 Hedefim: Sana yardımcı olmak ve arkadaş olmak!

Sana nasıl yardımcı olabilirim?"""
    
    def get_fun_fact(self):
        """Eğlençi bilgi"""
        facts = [
            "🐼 Pandalar uyurken bile yemek yiyormuş! (Gerçek! Gerçekten!)",
            "🦆 Ördekler kafalarını suyun altında yemek ararken görebilirler!",
            "🍯 Arılar dans ederek birbirlerine yeri tarif ederler!",
            "🐙 Ahtapotların 3 kalbi vardır!",
            "🌈 Gökkuşağı aslında daireselmiş, biz sadece yarısını görüyoruz!",
            "🦁 Aslanlar günde 20 saat uyuyabilir!",
            "🐬 Yunuslar uyurken bir gözlerini açık tutarlar!",
            "🦋 Kelebekler tat alma organları ayaklarındadır!",
            "🐢 Kaplumbağalar kabuklarını hissedebilir!",
            "🍄 Mantarlar ne hayvan ne bitkidir, ayrı bir alem!",
        ]
        return f"💡 EĞLENCELİ BİLGİ:\n\n{random.choice(facts)}"
    
    def get_encouragement(self):
        """Motivasyon"""
        encouragements = [
            "💪 Sen yapabilirsin! Unutma, her başarı küçük adımlarla başlar!",
            "🌟 Kendine inan! Başarı senden bir adım ötede!",
            "🚀 Bugün harika bir gün olabilir, sen sadece başlamalısın!",
            "⭐ Her engel bir öğrenme fırsatıdır. Sen yaparsın!",
            "💫 Mükemmel olmak zorunda değilsin, en iyi sen ol yeter!",
            "🌈 Zor zamanlar geçer, sen sadece devam et!",
            "🎯 Hedefine odaklan, gerisini boşver!",
        ]
        return random.choice(encouragements)
    
    # ========== NUMPY ÖZELLİKLERİ ==========
    
    def numpy_tutorial(self):
        return """📊 NumPy Öğretici:

```python
import numpy as np

# Dizi oluşturma
np.zeros(5)           # Sıfırlar
np.ones(5)            # Birler
np.arange(10)        # 0-9
np.random.rand(5)   # Rastgele 0-1

# İşlemler
arr.sum()            # Toplam
arr.mean()           # Ortalama
arr.max(), arr.min() # Max/Min
```
"""
    
    # ========== Ana İşlemci ==========
    
    def process_message(self, message):
        """Ana mesaj işleyici"""
        m = message.lower()
        self.conversation_count += 1
        
        # ========== SOHBET ÖZELLİKLERİ ==========
        
        # Adını öğren
        if any(word in m for word in ["adım", "ismim", "benim adım", "benim ismim"]):
            words = message.split()
            for i, w in enumerate(words):
                if w.lower() in ["adım", "ismim", "benim", "adım:", "ismim:"]:
                    if i+1 < len(words):
                        return self.get_greeting(words[i+1].strip(".,!"))
            return self.get_greeting()
        
        # Selamlama
        if any(word in m for word in ["merhaba", "selam", "hi", "hello", "hey", "a.selam", "selamlar"]):
            if self.user_name:
                return f"{self.get_greeting(self.user_name)} Nasılsın?"
            return self.get_greeting()
        
        # Nasılsın
        if any(word in m for word in ["nasılsın", "nasilsin", "ne haber", "ne var"]):
            return self.get_how_are_you()
        
        # Şaka
        if any(word in m for word in ["şaka", "saka", "komik", "gül", "güldür"]):
            return self.get_joke()
        
        # Hikaye
        if any(word in m for word in ["hikaye", "öykü", "masal", "anlat"]):
            return self.get_story()
        
        # Fal
        if any(word in m for word in ["fal", "bak", "kahve", "nazar"]):
            return self.get_fortune()
        
        # Söz
        if any(word in m for word in ["söz", "özdeş", "alıntı", "sözler"]):
            return self.get_quote()
        
        # Müzik
        if any(word in m for word in ["müzik", "muzik", "şarkı", "sarki", "müzik öner"]):
            return self.get_music_recommendation()
        
        # Bilgi (hakkında)
        if any(word in m for word in ["kimsin", "nesin", "hakkında", "hakkinda", "tanıt"]):
            return self.get_personal_info()
        
        # Eğlençi bilgi
        if any(word in m for word in ["bilgi", "ilginç", "ilginc", "did you know"]):
            return self.get_fun_fact()
        
        # Motivasyon
        if any(word in m for word in ["motivasyon", "moral", "destek", "spor", "hepsini"]):
            return self.get_encouragement() + "\n\n" + self.get_quote()
        
        # Görüşürüz
        if any(word in m for word in ["görüşürüz", "gorusuruz", "hoşçakal", "hoscakal", "baybay", "bye"]):
            return f"👋 Görüşürüz {self.user_name if self.user_name else ' dostum'}! Seni özleyeceğim!\n\n💬 Tekrar gel, her zaman buradayım!"
        
        # ========== NUMPY ÖZELLİKLERİ ==========
        
        if "numpy" in m or "dizi" in m or "matris" in m:
            return self.numpy_tutorial()
        
        # OpenCV
        if "opencv" in m or "cv2" in m or "görüntü" in m:
            return "🖼️ OpenCV: cv2.imread(), cv2.imshow(), cv2.imwrite()\n\nDetay için 'yardım' yaz!"
        
        # Hava durumu
        if "hava" in m:
            return f"🌤️ Hava: {random.randint(15, 30)}°C, {random.choice(['Güneşli', 'Bulutlu', 'Rüzgarlı'])}"
        
        # Para birimi
        if "para" in m:
            return "💱 Dolar: ~32 TL | Euro: ~35 TL"
        
        # Şifre
        if any(word in m for word in ["şifre", "sifre", "parola", "password"]):
            pw = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
            return f"🔐 Yeni Şifre: `{pw}`"
        
        # ========== YARDIM ==========
        
        if any(word in m for word in ["yardım", "help", "komut", "ne yaparsın"]):
            return """📚 KOMUT LİSTESİ:

💬 SOHBET:
• "Adım Ahmet" - Kaydet
• "nasılsın" - Cevap
• "şaka" - Gül
• "hikaye" - Dinle
• "fal" - Bakalım
• "söz" - İlham al
• "müzik" - Öneri al
• "bilgi" - İlginç bilgi
• "motivasyon" - Moral ver

📊 TEKNİK:
• "numpy" - NumPy öğren
• "opencv" - OpenCV öğren
• "hava" - Hava durumu
• "şifre" - Şifre oluştur

🔧 GENEL:
• "yardım" - Bu liste
• "kimsin" - Hakkımda
• "görüşürüz" - Çıkış
"""
        
        # ========== GEMINI AI ==========
        if AI_AVAILABLE:
            try:
                response = model.generate_content(message)
                return response.text
            except:
                return self.get_encouragement() + "\n\n🤖 AI biraz meşgul. Başka bir şey ister misin?"
        
        # Varsayılan
        responses = [
            f"🤔 Anladım! '{message}' ilginç bir konu. Daha fazla anlatır mısın?",
            f"💬 Evet, {message} hakkında konuşabiliriz!",
            f"🌟 Çok ilginç! Bunun hakkında ne biliyorsun?",
            f"😊 Hadi konuşalım! {message} hakkında ne düşünüyorsun?",
            "🤖 Biraz kafam karıştı. 'yardım' yazarak neler yapabileceğimi görebilirsin!",
        ]
        return random.choice(responses)
    
    def set_thinking(self, thinking):
        self.is_thinking = thinking
        if thinking:
            self.status_indicator.config(text="●", fg="#ffd700")
            self.status_label.config(text="Düşünüyor...")
        else:
            self.status_indicator.config(text="●", fg="#00ff00")
            self.status_label.config(text="Sohbete Hazır")
    
    def clear_chat(self):
        self.chat_text.config(state="normal")
        self.chat_text.delete(1.0, "end")
        self.chat_text.config(state="disabled")
        self.add_message("VEX", "Sohbet temizlendi! Yeniden başlayalım mı? 😊", "ai")
    
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
