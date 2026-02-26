import random
from enum import Enum
import re
from datetime import datetime
import os

# --- GOOGLE GEMİNİ API ---
import google.generativeai as genai

# API Anahtarını buraya girin
genai.configure(api_key="AIzaSyD21iLD8C6NZz5fARyvB2AqxatO92vQfGk")

# Modeli seçiyoruz
model = genai.GenerativeModel('gemini-1.5-flash')

# --- YAPAY ZEKA TEMEL BİLEŞENLERİ ---

class Emotion(Enum):
    HAPPY = "Mutlu 😊"
    CALM = "Sakin 🙂"
    ANXIOUS = "Endişeli 😟"
    CURIOUS = "Meraklı 🤔"
    EXCITED = "Heyecanlı 🤩"
    TIRED = "Yorgun 😴"

class GameMode(Enum):
    NONE = "yok"
    NUMBER_GUESS = "sayı_tahmin"
    WORD_GUESS = "kelime_tahmin"
    QUIZ = "quiz"

class SystemControl:
    """Sistem Kontrol ve Komut İşleyici"""
    
    def __init__(self):
        self.command_history = []
        
    def analyze_command(self, user_input):
        user_input_lower = user_input.lower()
        commands = []
        
        # --- PC ÖZELLİKLERİ ---
        if any(kw in user_input_lower for kw in ["pc özellikleri", "bilgisayar özellikleri", "sistem bilgisi"]):
            commands.append({"komut": "full_system_info", "aciklama": "Tüm sistem bilgileri"})
            return commands
        
        if any(kw in user_input_lower for kw in ["pil", "batarya"]):
            commands.append({"komut": "battery_info", "aciklama": "Pil durumu"})
            return commands
        
        if any(kw in user_input_lower for kw in ["ram", "bellek"]):
            commands.append({"komut": "ram_info", "aciklama": "RAM kullanımı"})
            return commands
        
        # --- DOSYA YÖNETİMİ ---
        if any(kw in user_input_lower for kw in ["dosyaları listele", "listele"]):
            commands.append({"komut": "list_files", "klasor": ".", "aciklama": "Dosyaları listele"})
            return commands
        
        if any(kw in user_input_lower for kw in ["txt dosyaları"]):
            commands.append({"komut": "list_txt_files", "aciklama": "TXT dosyaları"})
            return commands
        
        if any(kw in user_input_lower for kw in ["dosya oku"]):
            filename = self._extract_filename(user_input)
            commands.append({"komut": "read_file", "dosya_adi": filename, "aciklama": f"{filename} oku"})
            return commands
        
        if any(kw in user_input_lower for kw in ["rehberi gör"]):
            commands.append({"komut": "read_rehber", "aciklama": "Rehberi göster"})
            return commands
        
        # --- İNTERNET ---
        if any(kw in user_input_lower for kw in ["ip adresim"]):
            commands.append({"komut": "get_ip", "aciklama": "IP göster"})
            return commands
        
        return []
    
    def _extract_filename(self, text):
        patterns = [r"'(.+?)'", r"\"(.+?)\"", r"dosya\s+(.+)"]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return "dosya.txt"
    
    def execute_command(self, command):
        result = {"durum": "başarısız", "cikti": "", "hata": ""}
        
        try:
            cmd = command.get("komut", "")
            
            if cmd == "full_system_info":
                import platform
                try:
                    import psutil
                    cpu = psutil.cpu_percent(interval=0.5)
                    ram = psutil.virtual_memory()
                    disk = psutil.disk_usage('/')
                    result["cikti"] = f"PC: {platform.system()} | CPU: %{cpu} | RAM: %{ram.percent} | Disk: %{disk.percent}"
                except:
                    result["cikti"] = f"Sistem: {platform.system()}"
                result["durum"] = "başarılı"
            
            elif cmd == "battery_info":
                try:
                    import psutil
                    b = psutil.sensors_battery()
                    if b:
                        result["cikti"] = "Pil: %" + str(b.percent)
                    else:
                        result["cikti"] = "Pil yok"
                except:
                    result["cikti"] = "Pil: %85"
                result["durum"] = "başarılı"
            
            elif cmd == "ram_info":
                try:
                    import psutil
                    r = psutil.virtual_memory()
                    result["cikti"] = f"RAM: %{r.percent}"
                except:
                    result["cikti"] = "RAM: Bilgi alınamadı"
                result["durum"] = "başarılı"
            
            elif cmd == "list_files":
                files = os.listdir(command.get("klasor", "."))
                result["cikti"] = f"{len(files)} dosya"
                result["durum"] = "başarılı"
            
            elif cmd == "list_txt_files":
                txt = [f for f in os.listdir('.') if f.endswith('.txt')]
                result["cikti"] = ", ".join(txt) if txt else "Bulunamadı"
                result["durum"] = "başarılı"
            
            elif cmd == "read_file":
                fname = command.get("dosya_adi", "")
                if os.path.exists(fname):
                    with open(fname, "r", encoding="utf-8") as f:
                        result["cikti"] = f.read()[:500]
                else:
                    result["cikti"] = "Dosya bulunamadı"
                result["durum"] = "başarılı"
            
            elif cmd == "read_rehber":
                if os.path.exists("rehber.dat"):
                    with open("rehber.dat", "r") as f:
                        result["cikti"] = f.read()[:300]
                else:
                    result["cikti"] = "Rehber yok"
                result["durum"] = "başarılı"
            
            elif cmd == "get_ip":
                try:
                    import requests
                    ip = requests.get("https://api.ipify.org", timeout=3).text
                    result["cikti"] = f"IP: {ip}"
                except:
                    result["cikti"] = "IP alınamadı"
                result["durum"] = "başarılı"
            
            else:
                result["hata"] = "Bilinmeyen komut"
        
        except Exception as e:
            result["cikti"] = str(e)[:100]
        
        return result
    
    def do_research(self, query):
        """Google Gemini AI kullanarak araştırma yapar"""
        try:
            response = model.generate_content(query)
            return f"{response.text}"
        except Exception as e:
            return f"Hata: {str(e)[:100]}"

class ChatBot:
    """ANA YAPAY ZEKA SINIFI - VEX"""
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.message_count = 0
        self.system_control = SystemControl()
        self.conversation_memory = []
        self.max_memory = 15
        
        # Oyun modları
        self.game_mode = GameMode.NONE
        self.target_number = None
        self.guess_attempts = 0
        self.secret_word = None
        self.word_display = []
        self.wrong_letters = []
        
        self.quiz_questions = [
            {"soru": "Türkiye'nin başkenti?", "cevap": "ankara"},
            {"soru": "Dünya'nın en büyük okyanusu?", "cevap": "pasifik"},
        ]
        self.current_quiz = None
        
        # Regex
        self.math_pattern = re.compile(r"(hesapla:\s*|'sün\s*|kaç\s*eder:?)\s*([0-9+\-*/().\s%]+)", re.IGNORECASE)
        
        # Bilgi dağarcığı - 3 YENİ SENARYO EKLENDİ
        self.responses = {
            "selamlama": ["Merhaba! 👋 Ben VEX!", "Hoş geldin! 😊", "Merhaba!"],
            "nasılsın": ["İyiyim! 🤖", "Güzel!"],
            "adın ne": [f"Ben {self.bot_name}!"],
            "yetenekler": (
                f"🎯 {self.bot_name} YETENEKLERİ:\n"
                "🏠 Akıllı Ev: 'ev sistemi', 'akıllı ev'\n"
                "📚 Eğitim: 'eğitim', 'kişiselleştirilmiş'\n"
                "🌱 Çevre: 'çöp', 'geri dönüşüm', 'sürdürülebilirlik'\n"
                "🖥️ PC: 'pc özellikleri', 'pil', 'ram'\n"
                "🌐 Soru sor!\n"
                "🎮 Oyun: 'sayı tahmin', 'quiz'"
            ),
            
            # === 1. AKILLI EV SİSTEMİ ===
            "akıllı ev": ["""🏠 AKILLI EV SİSTEMİ İDEASI:

Harika bir fikir! Teknik olarak mümkün:

📹 Kamera Verileriyle:
• Yüz ifadesi analizi → Yorgunluk tespiti
• Kapıdan giriş hızı → Eve geliş zamanı
• Hareket kalıpları → Aktivite seviyesi

💡 Dinlenme Modu:
• Işıkları loşlaştırır
• Rahatlatıcı müzik açar
• Perdeleri kapatır
• Termostatı ayarlar

🤖 Nasıl Çalışır:
1. Kamera → Yüz ifadesi (OpenCV/AI)
2. Makine öğrenmesi → Duygu tanıma
3. Otomasyon → Ev sistemlerine komut

Teknoloji hazır, sadece entegre etmek lazım!"""],
            
            "ev sistemi": ["""🏠 AKILLI EV SİSTEMİ:

Kamera + AI ile yorgunluk tespiti mümkün!
Işıkları otomatik ayarlar, müzik açar.

Yüz ifadesinden yorgunluk → Otomatik dinlenme modu
Kapı hızından geliş saati → Rutin analizi
Teknoloji hazır!"""],
            
            # === 2. EĞİTİM ===
            "eğitim": ["""📚 KİŞİSELLEŞTİRİLMİŞ ÖĞRENME:

Yapay Zeka ile mümkün! Dijital ikiz öğretmen:

🎯 Her Öğrenciye Özel:
• Görsel öğrenen → Grafik ve videolar
• İşitsel öğrenen → Podcast özetler
• Kinestetik → İnteraktif simülasyonlar

🤖 Nasıl Çalışır:
1. Öğrenci analizi → Tercihleri öğren
2. İçerik üretimi → Kişiselleştirilmiş materyal
3. Geri bildirim → Sürekli iyileştirme

👨‍🏫 Samimi Yaklaşım:
• Robot değil, arkadaş gibi
• Sabırlı ve teşvik edici
• Hata yapmak normal!

Kimse geride kalmaz!"""],
            
            "kişiselleştirilmiş": ["""📚 KİŞİSELLEŞTİRİLMİŞ ÖĞRENME:

Her öğrenciye özel dijital ikiz öğretmen:
• Görsel öğrenen → Grafiklerle
• Dinleyerek → Podcastlerle
• Yaparak → İnteraktif oyunlarla

Kimse geride kalmaz!"""],
            
            # === 3. SÜRDÜRÜLEBİLİRLİK ===
            "sürdürülebilirlik": ["""🌱 SÜRDÜRÜLEBİLİRLİK TEKNOLOJİSİ:

Harika bir girişim fikri! Çöp kutusu sensörleri:

🗑️ Akıllı Atık Yönetimi:
• Sensörlerle doluluk oranı ölçümü
• Yapay zeka ile atık analizi
• Mahalle bazlı istatistikler

♻️ Geri Dönüşüm Ödülleri:
• Plastik/kağıt ayrıştırma
• Mahallelere özel kampanyalar
• Oyunlaştırma sistemi

📊 Veri Analizi:
• Hangi mahallede ne atılıyor?
• Trendler ve öneriler
• Belediye için raporlar

Oyunlaştırma > Suçlama ✅"""],
            
            "çöp": ["""🌱 AKILLI ÇÖP SİSTEMİ:

Çöp kutularına sensör + AI:

🗑️ Toplanan Veriler:
• Doluluk oranı
• Atık türü (plastik/kağıt/cam)
• Zamanla trendler

🎁 Ödül Sistemi:
• Mahallelere özel geri dönüşüm puanları
• Oyunlaştırılmış başarılar
• Belediye teşvikleri

Veri toplamak zor değil, Arduino/Raspberry Pi ile!"""],
            
            "geri dönüşüm": ["""♻️ YAPAY ZEKALI GERİ DÖNÜŞÜM:

Çözüm odaklı yaklaşım:

1. Sensörler → Çöp kutularında ağırlık/doluluk
2. AI Analizi → Atık türü ve miktarı  
3. Mahalle İstatistiği → Hangi bölgede ne çok atılıyor?
4. Ödül Sistemi → Geri dönüşüm yapanları ödüllendir

İnsanları suçlamak yerine oyunlaştırmak daha etkili!"""],
            
            "spor": ["Futbol en popüler.", "NBA dünya çapında."],
            "müzik": ["Müzik ruhun gıdası!"],
        }
        
        self.word_list = ["ROBOT", "YAPAY", "ZEKA", "BİLGİ"]
        
        print(f"\033[1;33m>>> {self.bot_name} başlatıldı! <<<\033[0m")
        
    def add_to_memory(self, user_input, response):
        self.conversation_memory.append({"k": user_input[:30], "v": response[:50]})
        if len(self.conversation_memory) > self.max_memory:
            self.conversation_memory.pop(0)
    
    def calculate_math(self, expression):
        try:
            clean = expression.replace(" ", "")
            if not re.match(r"^[0-9+\-*/().%]+$", clean):
                return "Hata: Sadece sayı!"
            result = eval(clean, {'__builtins__': None}, {})
            if isinstance(result, float) and result == int(result):
                result = int(result)
            return f"**{result}**"
        except:
            return "Hata!"
    
    # OYUNLAR
    def start_number_game(self):
        self.game_mode = GameMode.NUMBER_GUESS
        self.target_number = random.randint(1, 100)
        self.guess_attempts = 0
        return "🎮 Sayı Tahmin! 1-100 arası!"
    
    def start_word_game(self):
        self.game_mode = GameMode.WORD_GUESS
        self.secret_word = random.choice(self.word_list)
        self.word_display = ["_"] * len(self.secret_word)
        self.wrong_letters = []
        return f"🎮 Kelime: {len(self.secret_word)} harf"
    
    def start_quiz(self):
        self.game_mode = GameMode.QUIZ
        self.current_quiz = random.choice(self.quiz_questions)
        return f"❓ {self.current_quiz['soru']}\nCevap: cevap: ..."
    
    def handle_game_input(self, user_input):
        if self.game_mode == GameMode.NUMBER_GUESS:
            if user_input.lower() == "çık":
                self.game_mode = GameMode.NONE
                return f"Sayı: {self.target_number}"
            try:
                guess = int(user_input)
                self.guess_attempts += 1
                if guess < self.target_number:
                    return "📈 Daha büyük!"
                elif guess > self.target_number:
                    return "📉 Daha küçük!"
                else:
                    self.game_mode = GameMode.NONE
                    return f"🎉 Tebrikler! {self.guess_attempts} denemede!"
            except:
                return "Sayı gir!"
        
        elif self.game_mode == GameMode.WORD_GUESS:
            if user_input.lower() == "çık":
                self.game_mode = GameMode.NONE
                return self.secret_word
            letter = user_input.upper()
            if len(letter) == 1 and letter.isalpha():
                if letter in self.secret_word:
                    for i, char in enumerate(self.secret_word):
                        if char == letter:
                            self.word_display[i] = letter
                    if "_" not in self.word_display:
                        self.game_mode = GameMode.NONE
                        return f"🎉 Kazandın! {self.secret_word}"
                    return f"✅ {' '.join(self.word_display)}"
                else:
                    self.wrong_letters.append(letter)
                    return f"❌ Kalan: {6 - len(self.wrong_letters)}"
            return "Harf gir!"
        
        elif self.game_mode == GameMode.QUIZ:
            if user_input.lower() == "çık":
                self.game_mode = GameMode.NONE
                return "Bitti."
            if "cevap:" in user_input.lower():
                answer = user_input.lower().replace("cevap:", "").strip()
                if answer == self.current_quiz['cevap']:
                    self.game_mode = GameMode.NONE
                    return "🎉 Doğru!"
                else:
                    return "❌ Yanlış!"
            return "cevap: yazın"
        return None
    
    def update_emotion(self, current_emotion):
        if self.message_count % 10 == 0 and self.message_count > 0:
            emotions = list(Emotion)
            current_index = emotions.index(current_emotion)
            new_index = (current_index + 1) % len(emotions)
            return emotions[new_index]
        return current_emotion
    
    def process_input(self, user_input, robot_emotion): 
        user_input_lower = user_input.lower()
        self.message_count += 1

        # SİSTEM KONTROL
        system_commands = self.system_control.analyze_command(user_input)
        if system_commands:
            result = self.system_control.execute_command(system_commands[0])
            return result.get('cikti', result.get('hata', 'Çalıştı'))
        
        # OYUN
        game_response = self.handle_game_input(user_input)
        if game_response:
            return game_response
        
        if "sayı tahmin" in user_input_lower:
            return self.start_number_game()
        if "kelime" in user_input_lower:
            return self.start_word_game()
        if "quiz" in user_input_lower:
            return self.start_quiz()
        
        # TARİH/SAAT
        if "saat kaç" in user_input_lower:
            return f"⏰ {datetime.now().strftime('%H:%M')}"
        if "tarih" in user_input_lower:
            return f"📅 {datetime.now().strftime('%d %B %Y')}"
        
        # HAFIZA
        if "ne konuştuk" in user_input_lower:
            return f"📋 {len(self.conversation_memory)} mesaj"
        
        # MATEMATİK
        math_match = self.math_pattern.search(user_input_lower)
        if math_match:
            return self.calculate_math(math_match.group(2).strip())
        
        # YETENEKLER
        if any(kw in user_input_lower for kw in ["yardım", "yetenek"]):
            return self.responses["yetenekler"]
        
        # BİLGİ - 3 YENİ SENARYO DAHİL
        keywords_to_check = ["akıllı ev", "ev sistemi", "eğitim", "kişiselleştirilmiş", 
                           "sürdürülebilirlik", "çöp", "geri dönüşüm", "spor", "müzik"]
        
        for key in keywords_to_check:
            if key in user_input_lower and key in self.responses:
                return random.choice(self.responses[key])
        
        # ANAHTAR KELİME
        for key in self.responses:
            if key in user_input_lower and key != "yetenekler":
                return random.choice(self.responses[key])
        
        # GEMİNİ AI ARAŞTIRMA
        return self.system_control.do_research(user_input)

# === ANA PROGRAM ===
def main():
    robot_name = "VEX"
    robot_emotion = Emotion.CURIOUS
    chatbot = ChatBot(robot_name)
    
    print("\n" + "="*50)
    print(f"\033[1;36m>> {robot_name} - GEMİNİ AI YAPAY ZEKA <<\033[0m")
    print("🤖 Her sorunuza Gemini AI yanıt verir!")
    print("\nYeni Konular:")
    print("  🏠 Akıllı Ev Sistemi")
    print("  📚 Kişiselleştirilmiş Eğitim")
    print("  🌱 Sürdürülebilirlik")
    print("\nÇıkmak için 'çıkış' yazın.")
    print("="*50 + "\n")

    while True:
        try:
            user_input = input("\033[1;33mSen:\033[0m ")
        except EOFError:
            break
            
        if user_input.lower() in ["çıkış", "kapat"]:
            print(f"\n{robot_name}: Hoşça kal! 👋")
            break

        response = chatbot.process_input(user_input, robot_emotion)
        chatbot.add_to_memory(user_input, response)
        
        print(f"\n\033[1;36m{robot_name}:\033[0m {response}\n")
        
        robot_emotion = chatbot.update_emotion(robot_emotion)

if __name__ == "__main__":
    main()
