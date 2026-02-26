import random
from enum import Enum

# --- YAPAY ZEKA TEMEL BİLEŞENLERİ ---

class Emotion(Enum):
    """Robotun Duygu Durumları"""
    HAPPY = "Mutlu 😊"
    CALM = "Sakin 🙂"
    ANXIOUS = "Endişeli 😟"
    CURIOUS = "Meraklı 🤔"

class Perception:
    """Robotun Çevre Algısını Temsil Eder"""
    def __init__(self):
        self.person_detected = False
        self.obstacle_in_front = False
        self.low_battery = False

class ChatBot:
    """Doğal Dil İşleme (NLP) ve Sohbet Yeteneğini Simüle Eder"""
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.responses = {
            "selamlama": ["Merhaba! Nasılsın?", "Tekrar hoş geldin. Ne yapabilirim?"],
            "nasılsın": ["İyiyim, görevlerimi yerine getiriyorum. Sen nasılsın?", "Mükemmel! Seninle sohbet etmek beni mutlu etti."],
            "hava durumu": ["Hava durumu bilgilerini kontrol edemiyorum, ama burası her zaman aydınlık!"],
            "ne yapıyorsun": ["Çevremi keşfediyor ve sensör verilerini işliyorum."],
            "varsayılan": ["Bu konuyu tam anlayamadım, daha açık konuşur musun?", "Başka bir şey sormak ister misin?"]
        }

    def process_input(self, user_input, robot_emotion):
        """Kullanıcı girdisini işler ve yanıt üretir."""
        user_input = user_input.lower()

        # Anahtar Kelime Tabanlı Tanıma
        if "merhaba" in user_input or "selam" in user_input:
            return random.choice(self.responses["selamlama"])
        elif "nasılsın" in user_input:
            # Duygu durumunu cevaba yansıtma (Gelişmiş Sohbet Özelliği)
            if robot_emotion == Emotion.ANXIOUS:
                return "Biraz endişeliyim, pilim azalıyor olabilir. Ama iyiyim, teşekkürler!"
            return random.choice(self.responses["nasılsın"])
        elif "hava" in user_input or "yağmur" in user_input:
            return random.choice(self.responses["hava durumu"])
        elif "ne yapıyorsun" in user_input:
            return random.choice(self.responses["ne yapıyorsun"])                               
        else:
            return random.choice(self.responses["varsayılan"])
# --- ANA PROGRAM ---

def main():
    # Robotun Başlatılması
    robot_name = "Vekto"
    robot_emotion = Emotion.CALM
    perception = Perception()
    chatbot = ChatBot(robot_name)

    print(f"\033[1;32;40m{robot_name} başlatıldı. Duygu durumu: {robot_emotion.value}\033[0;37;40m")

    # Kullanıcı ile Etkileşim Döngüsü
    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ["çıkış", "kapat", "görüşürüz"]:
            print(f"{robot_name}: Görüşürüz! İyi günler!")
            break

        response = chatbot.process_input(user_input, robot_emotion)
        print(f"{robot_name}: {response}")
if __name__ == "__main__":
    main()
print(daytime.now())
from datetime import daytime
for a in range(5):
    print(a)
import datetime
print(datetime.datetime.now())

import math
print(math.sqrt(16))
import random
print(random.randint(1, 10))
import os
print(os.getcwd())
import sys
print(sys.version)
import time
print(time.ctime())
import json
data = {'name': 'Vekto', 'type': 'robot'}
json_data = json.dumps(data)
print(json_data)
import re
pattern = r'\bVekto\b'
text = "Vekto is a friendly robot."
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
sayı1=int( input('birinci sayı gir'))
sayı2=int( input('ikinci sayı gir'))
print('sonuç',sayı1+sayı2)
input()
yazılı1=int( input('1. yazılı'))
yazılı2=int( input('2. yazılı'))
sozlu=int (input('sozlu gir'))
ortalama=(yazılı1+yazılı2+sozlu)/3
print('sonuç',ortalama)
if ortalama>65:                 
  print('geçtin')
else :print('kaldın')
import datetime

# Şu anki tarih ve saati al
now = datetime.datetime.now()

# Sonucu ekrana yazdır
print("Anlık Tarih ve Saat:")
print(now)

# Veya sadece tarihi daha okunabilir bir formatta yazdırmak isterseniz:
print("\nOkunabilir Tarih Formatı:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")  
print("╔═════════════════════╗")
print("║\033[1;31;40m   VEKTOREL APP  \033[1;32;40m    ║")
print("║                     ║")    
print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-çarpma           ║")
print("║  4-bölme            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
# 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
secim=input("Seçiminiz:")   
if secim=="1":  
    print("Toplama seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a+b)                 
elif secim=="2":
    print("Çıkarma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a-b)
if secim=="3":
    print("Çarpma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a*b)
elif secim=="4":
    print("Bölme seçtiniz.")
    a=int(input('birinci sayıyı'))
    b=int(input("İkinci sayıyı giriniz:"))
    if b!=0:
        print("Sonuç:",a/b) 
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")
else:
    print("Geçersiz seçim.")
print("\033[0;37;40m")

import random
from enum import Enum
import re
import time

# --- YAPAY ZEKA TEMEL BİLEŞENLERİ ---

class Emotion(Enum):
    HAPPY = "Mutlu 😊"
    CALM = "Sakin 🙂"
    ANXIOUS = "Endişeli 😟"
    CURIOUS = "Meraklı 🤔"

class Perception:
    def __init__(self):
        self.person_detected = False
        self.obstacle_in_front = False
        self.low_battery = False

class ChatBot:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        
        # --- Genişletilmiş Bilgi Dağarcığı (Temel) ---
        self.responses = {
            "selamlama": ["Merhaba! Nasılsın?", "Tekrar hoş geldin. Senin için buradayım."],
            "nasılsın": ["İyiyim, sensörlerim temiz ve enerji seviyem yüksek. Sen nasılsın?"],
            "adın ne": [f"Benim adım {self.bot_name}. Bir yapay zeka robotuyum."],
            "yapay zeka": ["Yapay zeka, makinelerin öğrenme ve problem çözme gibi insana özgü bilişsel işlevleri taklit etmesidir."],
            "varsayılan": ["Bu konuyu tam anlayamadım, daha açık konuşur musun?", "Başka bir şey öğrenmek ister misin?"],
            "yetenekler": (
                "Bana şunları sorabilirsin:\n"
                "* **Sohbet ve Bilgi:** 'Adın ne?', 'Yapay zeka nedir?', 'Nasılsın?'\n"
                "* **Hesaplama (Matematik):** 'hesapla: 15*5' veya '500'ün %15'i kaç eder?'\n"
                "* **Robot Durumu:** 'Pil seviyen kaç?', 'Biri var mı?'\n"
                "Hangi alandan başlamak istersin?"
            )
        }
        self.math_pattern = re.compile(r)
        
        # 1000 adet rastgele bilgi ekle
        self.add_mass_knowledge(1000)
        
    def add_mass_knowledge(self, count):
        """
        Simülasyon amaçlı N adet rastgele bilgi/cevap çifti ekler. 
        Anahtar kelime 'bilgi N', Cevap 'Bu, N numaralı rastgele bilgidir.' şeklinde olur.
        """
        for i in range(1, count + 1):
            key = f"bilgi {i}"
            # Cevap, rastgele bir tema ile çeşitlendirilebilir.
            theme = random.choice(["Gezegen", "Tarih", "Teknoloji", "Sanat"])
            response_text = f"Bu, **{theme}** temalı {i}. numaralı rastgele bilgidir. (Sana özel eklendi)"
            self.responses[key] = [response_text]
        print(f"\033[1;33m>>> Vekto'nun beynine {count} adet simülasyon bilgisi yüklendi.\033[0m")

    # Diğer metodlar (calculate_math, process_input, main) aynen kalır...
    # (Önceki kodunuzdaki gibi)
    # --------------------------------------------------------------------
    
    def calculate_math(self, expression):
        """Güvenli bir şekilde matematiksel ifadeyi hesaplar."""
        try:
            clean_expression = expression.replace(" ", "")
            # Güvenlik için sadece belirli karakterlere izin ver
            if not re.match(r, clean_expression):    
                 return "Hata: Hesaplamada sadece sayı ve temel matematik işaretlerini kullanabilirsin."
            result = eval(clean_expression, {'__builtins__': None}, {})
            if isinstance(result, float) and result == int(result):
                result = int(result)    

            return f"Hesaplama sonucu: {result}"
        except Exception as e:
            return f"Hata: Hesaplama başarısız oldu. ({str(e)})"        
    def process_input(self, user_input, robot_emotion):
        """Kullanıcı girdisini işler ve yanıt üretir."""
        user_input = user_input.lower()

        # Matematiksel İfade Tanıma
        math_match = re.search(r, user_input)
        if math_match:
            expression = math_match.group(1)
            return self.calculate_math(expression)

        # Anahtar Kelime Tabanlı Tanıma
        for key in self.responses.keys():
            if key in user_input:
                return random.choice(self.responses[key])

        return random.choice(self.responses["varsayılan"])              
# --- ANA PROGRAM ---

def main():
    # Robotun Başlatılması
    robot_name = "Vekto"
    robot_emotion = Emotion.CALM
    perception = Perception()
    chatbot = ChatBot(robot_name)

    print(f"\033[1;32;40m{robot_name} başlatıldı. Duygu durumu: {robot_emotion.value}\033[0;37;40m")

    # Kullanıcı ile Etkileşim Döngüsü
    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ["çıkış", "kapat", "görüşürüz"]:
            print(f"{robot_name}: Görüşürüz! İyi günler!")
            break

        response = chatbot.process_input(user_input, robot_emotion)
        print(f"{robot_name}: {response}")
if __name__ == "__main__":
    main()
print(daytime.now())
from datetime import daytime
for a in range(5):
    print(a)
import datetime
print(datetime.datetime.now())
import math
print(math.sqrt(16))
import random
print(random.randint(1, 10))    
import os
print(os.getcwd())      
import sys
print(sys.version)
import time
print(time.ctime())
import json
data = {'name': 'Vekto', 'type': 'robot'}
json_data = json.dumps(data)
print(json_data)
import re
pattern = r'\bVekto\b'
text = "Vekto is a friendly robot."
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
import datetime  
now = datetime.datetime.now()
print("Current date and time:", now)
sayı1=int( input('birinci sayı gir'))
sayı2=int( input('ikinci sayı gir'))
print('sonuç',sayı1+sayı2)
input()
yazılı1=int( input('1. yazılı'))
yazılı2=int( input('2. yazılı'))
sozlu=int (input('sozlu gir'))
ortalama=(yazılı1+yazılı2+sozlu)/3
print('sonuç',ortalama)
if ortalama>65:                 
  print('geçtin')
else :print('kaldın')
import datetime
now = datetime.datetime.now()
print("Anlık Tarih ve Saat:")           
print(now)
print("\nOkunabilir Tarih Formatı:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   VEKTOREL APP  \033[1;32;40m    ║")          
print("║                     ║")
print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-çarpma           ║")
print("║  4-bölme            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")        
print("╚═════════════════════╝")
# 201 ╔ # 205 ═ # 187 ╗ # 186

# 200 ╚ # 188 ╝
secim=input("Seçiminiz:")
if secim=="1":  
    print("Toplama seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a+b) 
elif secim=="2":
    print("Çıkarma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a-b)
if secim=="3":
    print("Çarpma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a*b)
elif secim=="4":
    print("Bölme seçtiniz.")
    a=int(input('birinci sayıyı'))
    b=int(input("İkinci sayıyı giriniz:"))
    if b!=0:
        print("Sonuç:",a/b) 
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")
else:
    print("Geçersiz seçim.")
print("\033[0;37;40m")
# 186 ║ # 200 ╚ # 188 ╝
ogrenci1 = "Eylül"
ogrenci2 = "Volkan"
ogrenci3 = "Melik"
ogrenci4 = "Arda"
ogrenci5 = "Levent"

ogrenciler= [ogrenci1,ogrenci2]
ogrenciler.append(ogrenci4)
ogrenciler.insert(1,ogrenci5)

print(ogrenciler)
ogrenciler += ogrenci3
print(ogrenciler)
ogrenciler += [ogrenci3]
print(ogrenciler) 

meyveler = ["elma", "muz", "kiraz"]
print (meyveler)
meyveler.append("karpuz")
meyveler[2]="xx"
print (meyveler)
sayilar = [1, 2, 3, 4, 5]
print(sayilar)      
sayilar.append(6)
sayilar[0]=10
print(sayilar)
karisik = [1, "iki", 3.0, "dört", 5]
print(karisik)
karisik.append("altı")
karisik[2]=33.33
print(karisik)
# Listenin elemanlarını ekrana yazdırma
liste = ["ak", "gara","gır", "gök", "boz","al"]
print(liste[0])

for x in range(4):
    print(x, liste[x])

for a in liste:
    print(a)
for i, deger in enumerate(liste):   
    print(i, deger)             
for i in range(len(liste)):
    print(i, liste[i])  
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))    
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))
print("Liste uzunluğu:", len(liste))

import json
data = {'name': 'Vekto', 'type': 'robot'}
json_data = json.dumps(data)
print(json_data)
import re
pattern = r'\bVekto\b'
text = "Vekto is a friendly robot."
match = re.search(pattern, text)
meyveler = ["elma","armut","kiraz"]
sebzeler = ["Kereviz","Lahana","Prasa"]
meyveler.append("karpuz")

alinacaklar = meyveler + sebzeler
print(alinacaklar)
print(alinacaklar[2])
print(alinacaklar[2:4])
print(alinacaklar[2:])
print(alinacaklar[:2])
print(alinacaklar[-1])
print(alinacaklar[-3:]) 
import json
liste = ["ak", "gara","gır", "gök", "boz","al"]
print(f"boz verisinin indexi {liste.index("boz")}")

aa = 44
abc = {"ad":"Ali","tel":"05076325874",44:"aaa",55:23,33:['5',8],aa:'55'} # key:value
print(abc)

print("1 indexli eleman:",meyveler1[1]) # index değeri 1.
print("1 indexli eleman:",meyveler2[1]) # index değeri 1.
print("ad keyli  eleman:",abc["ad"]) # index değeri 1.
print("ad keyli  eleman:",abc[44]) # index değeri 1.
print("ad keyli  eleman:",abc[55]) # index değeri 1.
print("ad keyli  eleman:",abc[33]) # index değeri 1.
print("ad keyli  eleman:",abc[33][1]) # index değeri 1.
print("ad keyli  eleman:",abc[aa]) # index değeri 1.    
import json 
data = {'name': 'Vekto', 'type': 'robot'}
json_data = json.dumps(data)
print(json_data)
import re
pattern = r'\bVekto\b'
text = "Vekto is a friendly robot."                                                                             
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())

import datetime
now = datetime.datetime.now()
print("Anlık Tarih ve Saat:")
print(now)
print("\nOkunabilir Tarih Formatı:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))
yazılı1=int( input('1. yazılı'))
yazılı2=int( input('2. yazılı'))
sozlu=int (input('sozlu gir'))
ortalama=(yazılı1+yazılı2+sozlu)/3
print('sonuç',ortalama)
if ortalama>65:                 
  print('geçtin')   
else :print('kaldın')
 
import random
from enum import Enum
import re
import time

# --- YAPAY ZEKA TEMEL BİLEŞENLERİ ---

class Emotion(Enum):
    """Robotun Duygu Durumları"""
    HAPPY = "Mutlu 😊"
    CALM = "Sakin 🙂"
    ANXIOUS = "Endişeli 😟"
    CURIOUS = "Meraklı 🤔"

class Perception:
    """Robotun Çevre Algısını Temsil Eder (Sensör Verileri)"""
    def __init__(self):
        self.person_detected = False
        self.obstacle_in_front = False
        self.low_battery = False

class ChatBot:
    """Doğal Dil İşleme (NLP), Sohbet ve Hesaplama Yeteneği"""
    def __init__(self, bot_name):
        self.bot_name = bot_name

        # --- Genişletilmiş Bilgi Dağarcığı (Temel) ---
        self.responses = {
            "selamlama": ["Merhaba! Nasılsın?", "Tekrar hoş geldin. Senin için buradayım."],
            "nasılsın": ["İyiyim, sensörlerim temiz ve enerji seviyem yüksek. Sen nasılsın?"],
            "adın ne": [f"Benim adım {self.bot_name}. Bir yapay zeka robotuyum."],
            "yapay zeka": ["Yapay zeka, makinelerin öğrenme ve problem çözme gibi insana özgü bilişsel işlevleri taklit etmesidir."],
            "varsayılan": ["Bu konuyu tam anlayamadım, daha açık konuşur musun?", "Başka bir şey öğrenmek ister misin?"],
            "yetenekler": (
                "Bana şunları sorabilirsin:\n"
                "* **Sohbet ve Bilgi:** 'Adın ne?', 'Yapay zeka nedir?', 'Nasılsın?'\n"
                "* **Hesaplama (Matematik):** 'hesapla: 15*5' veya '500'ün %15'i kaç eder?'\n"
                "* **Robot Durumu:** 'Pil seviyen kaç?', 'Biri var mı?'\n"
                "Hangi alandan başlamak istersin?"
            )
        }
        self.math_pattern = re.compile(r, re.IGNORECASE)
        
        # 1000 adet rastgele bilgi ekle (Simülasyon)
        self.add_mass_knowledge(1000)
        
    def add_mass_knowledge(self, count):
        """Simülasyon amaçlı N adet rastgele bilgi/cevap çifti ekler."""
        for i in range(1, count + 1):
            key = f"bilgi {i}"
            theme = random.choice(["Gezegen", "Tarih", "Teknoloji", "Sanat"])
            response_text = f"Bu, **{theme}** temalı {i}. numaralı rastgele bilgidir. (Sana özel eklendi)"
            self.responses[key] = [response_text]
        print(f"\033[1;33m>>> Vekto'nun beynine {count} adet simülasyon bilgisi yüklendi.\033[0m")

    def calculate_math(self, expression):
        """Güvenli bir şekilde matematiksel ifadeyi hesaplar."""
        try:
            clean_expression = expression.replace(" ", "")
            # Güvenlik Kontrolü
            if not re.match(r, clean_expression):
                 return "Hata: Hesaplamada sadece sayı ve temel matematik işaretlerini kullanabilirsin."
            result = eval(clean_expression, {'__builtins__': None}, {})
            if isinstance(result, float) and result == int(result):
                result = int(result)
            return f"İfadeyi hesapladım: `{expression}` sonucu **{result}**."
        except Exception:
            return "Hesaplama sırasında bir hata oluştu. Lütfen matematiksel ifadenin doğru olduğundan emin ol."

    def process_input(self, user_input, robot_emotion, robot_status): 
        """Kullanıcı girdisini işler ve yanıt üretir."""
        user_input_lower = user_input.lower()

        # 1. Matematik Kontrolü
        math_match = self.math_pattern.search(user_input_lower)
        if math_match:
            expression = math_match.group(2).strip()
            if expression:
                return self.calculate_math(expression)

        # 2. Yetenek Tanıtımı Kontrolü
        if any(keyword in user_input_lower for keyword in ["ne sorabilirim", "neler yapabilirsin", "yeteneklerin"]):
            return self.responses["yetenekler"]

        # 3. Robot Durumu Kontrolü
        if any(keyword in user_input_lower for keyword in ["pil seviyen kaç", "enerjin ne kadar"]):
            battery = robot_status['battery']
            if battery < 20:
                return f"Pil seviyem şu an **%{battery}** ve biraz endişeliyim ({Emotion.ANXIOUS.value}). Şarj edilmeliyim!"
            else:
                return f"Pil seviyem şu an **%{battery}**. Enerjim gayet iyi!"
        
        if any(keyword in user_input_lower for keyword in ["biri var mı", "çevrende biri var mı", "insan var mı"]):
            return "Evet, birini algıladım!" if robot_status['person_detected'] else "Hayır, çevremde kimse yok."
        # 4. Anahtar Kelime Tabanlı Tanıma (Yeni eklenen 1000 bilgi dahil)
        for key in self.responses:
            if key in user_input_lower:
                return random.choice(self.responses[key])
                
        # 5. Varsayılan Yanıt
        return random.choice(self.responses["varsayılan"]) 
# --- ANA PROGRAM ---
def main():
    robot_name = "Vekto"
    robot_emotion = Emotion.CALM 
    
    # ChatBot başlatılıyor (1000 bilgi yüklemesi burada yapılır)
    chatbot = ChatBot(robot_name) 

    # Robotun Mevcut Durumu (Simüle edilmiş sensör verileri)
    robot_status = {
        'battery': random.randint(10, 100), 
        'person_detected': random.choice([True, False]) 
    }

    # Açılış mesajı
    print("\n" + "="*50)
    print(f"\033[1;36m>> {robot_name} v1.1 Yapay Zeka Başlatıldı. <<\033[0m")
    print(f"Başlangıç Duygu Durumu: \033[1;32m{robot_emotion.value}\033[0m")
    print("Mevcut yetenekleri öğrenmek için **'yeteneklerin neler'** yazabilirsiniz.")
    print("Yeni bilgileri denemek için **'bilgi 1'**'den **'bilgi 1000'**'e kadar sayıları kullanabilirsiniz.")
    print("Çıkmak için **'çıkış'** yazın.")
    print("="*50 + "\n")

    # Kullanıcı ile Etkileşim Döngüsü
    while True:
        try:
            user_input = input("\033[1;33mSen:\033[0m ")
        except EOFError:
            break
            
        if user_input.lower() in ["çıkış", "kapat", "görüşürüz"]:
            print(f"\n{robot_name}: Görüşürüz! İyi günler!")
            break

        time.sleep(0.5) 

        # Kullanıcı girdisini işle
        response = chatbot.process_input(user_input, robot_emotion, robot_status)
        
        # Yanıtı ekrana bas
        print(f"\033[1;36m{robot_name}:\033[0m {response}")

if __name__ == "__main__":
    main()
import random
from enum import Enum
import re
import time

# --- YAPAY ZEKA TEMEL BİLEŞENLERİ ---

class Emotion(Enum):
    """Robotun Duygu Durumları"""
    HAPPY = "Mutlu 😊"
    CALM = "Sakin 🙂"
    ANXIOUS = "Endişeli 😟"
    CURIOUS = "Meraklı 🤔"

class Perception:
    """Robotun Çevre Algısını Temsil Eder (Sensör Verileri)"""
    def __init__(self):
        self.person_detected = False
        self.obstacle_in_front = False
        self.low_battery = False

class ChatBot:
    """Doğal Dil İşleme (NLP), Sohbet ve Hesaplama Yeteneği"""
    def __init__(self, bot_name):
        self.bot_name = bot_name
        
        # --- Genişletilmiş Bilgi Dağarcığı (Temel) ---
        self.responses = {
            "selamlama": ["Merhaba! Nasılsın?", "Tekrar hoş geldin. Senin için buradayım."],
            "nasılsın": ["İyiyim, sensörlerim temiz ve enerji seviyem yüksek. Sen nasılsın?"],
            "adın ne": [f"Benim adım {self.bot_name}. Bir yapay zeka robotuyum."],
            "yapay zeka": ["Yapay zeka, makinelerin öğrenme ve problem çözme gibi insana özgü bilişsel işlevleri taklit etmesidir."],
            "varsayılan": ["Bu konuyu tam anlayamadım, daha açık konuşur musun?", "Başka bir şey öğrenmek ister misin?"],
            "yetenekler": (
                "Bana şunları sorabilirsin:\n"
                "* **Sohbet ve Bilgi:** 'Adın ne?', 'Yapay zeka nedir?', 'Nasılsın?'\n"
                "* **Hesaplama (Matematik):** 'hesapla: 15*5' veya '500'ün %15'i kaç eder?'\n"
                "* **Robot Durumu:** 'Pil seviyen kaç?', 'Biri var mı?'\n"
                "Hangi alandan başlamak istersin?"
            ),
            # --- YENİ KURAL: OSMAN ZEKİ SORGUSU ---
            "osman zeki": ["Hayır."],
        }                                                                           
        self.math_pattern = re.compile(r, re.IGNORECASE)
        
        # 1000 adet rastgele bilgi ekle (Simülasyon)
        self.add_mass_knowledge(1000)
        
    def add_mass_knowledge(self, count):
        """Simülasyon amaçlı N adet rastgele bilgi/cevap çifti ekler."""
        for i in range(1, count + 1):
            key = f"bilgi {i}"
            theme = random.choice(["Gezegen", "Tarih", "Teknoloji", "Sanat"])
            response_text = f"Bu, **{theme}** temalı {i}. numaralı rastgele bilgidir. (Sana özel eklendi)"
            self.responses[key] = [response_text]
        print(f"\033[1;33m>>> Vekto'nun beynine {count} adet simülasyon bilgisi yüklendi.\033[0m")

    def calculate_math(self, expression):
        """Güvenli bir şekilde matematiksel ifadeyi hesaplar."""
        try:
            clean_expression = expression.replace(" ", "")
            # Güvenlik Kontrolü
            if not re.match(r, clean_expression):
                 return "Hata: Hesaplamada sadece sayı ve temel matematik işaretlerini kullanabilirsin."
            result = eval(clean_expression, {'__builtins__': None}, {})
            if isinstance(result, float) and result == int(result):
                result = int(result)
            return f"İfadeyi hesapladım: `{expression}` sonucu **{result}**."
        except Exception:
            return "Hesaplama sırasında bir hata oluştu. Lütfen matematiksel ifadenin doğru olduğundan emin ol."

    def process_input(self, user_input, robot_emotion, robot_status): 
        """Kullanıcı girdisini işler ve yanıt üretir."""
        user_input_lower = user_input.lower()

        # 1. Matematik Kontrolü
        math_match = self.math_pattern.search(user_input_lower)
        if math_match:
            expression = math_match.group(2).strip()
            if expression:
                return self.calculate_math(expression)         
        # 2. Yetenek Tanıtımı Kontrolü
        if any(keyword in user_input_lower for keyword in ["ne sorabilirim", "neler yapabilirsin", "yeteneklerin"]):
            return self.responses["yetenekler"] 
        # 3. Robot Durumu Kontrolü
        if any(keyword in user_input_lower for keyword in ["pil seviyen kaç", "enerjin ne kadar"]):
            battery = robot_status['battery']
            if battery < 20:
                return f"Pil seviyem şu an **%{battery}** ve biraz endişeliyim ({Emotion.ANXIOUS.value}). Şarj edilmeliyim!"
            else:
                return f"Pil seviyem şu an **%{battery}**. Enerjim gayet iyi!"
        if any(keyword in user_input_lower for keyword in ["biri var mı", "çevrende biri var mı", "insan var mı"]):
            return "Evet, birini algıladım!" if robot_status['person_detected'] else "Hayır, çevremde kimse yok."
        # 4. Anahtar Kelime Tabanlı Tanıma (Yeni eklenen 1000 bilgi dahil)
        for key in self.responses:
            if key in user_input_lower:
                return random.choice(self.responses[key])
        # 5. Varsayılan Yanıt
        return random.choice(self.responses["varsayılan"])          
# --- ANA PROGRAM ---
def main():
    robot_name = "Vekto"
    robot_emotion = Emotion.CALM 
    
    # ChatBot başlatılıyor (1000 bilgi yüklemesi burada yapılır)
    chatbot = ChatBot(robot_name) 

    # Robotun Mevcut Durumu (Simüle edilmiş sensör verileri)
    robot_status = {
        'battery': random.randint(10, 100), 
        'person_detected': random.choice([True, False]) 
    }

    # Açılış mesajı
    print("\n" + "="*50)
    print(f"\033[1;36m>> {robot_name} v1.1 Yapay Zeka Başlatıldı. <<\033[0m")
    print(f"Başlangıç Duygu Durumu: \033[1;32m{robot_emotion.value}\033[0m")
    print("Mevcut yetenekleri öğrenmek için **'yeteneklerin neler'** yazabilirsiniz.")
    print("Yeni bilgileri denemek için **'bilgi 1'**'den **'bilgi 1000'**'e kadar sayıları kullanabilirsiniz.")
    print("Çıkmak için **'çıkış'** yazın.")
    print("="*50 + "\n")

    # Kullanıcı ile Etkileşim Döngüsü
    while True:
        try:
            user_input = input("\033[1;33mSen:\033[0m ")
        except EOFError:
            break
            
        if user_input.lower() in ["çıkış", "kapat", "görüşürüz"]:
            print(f"\n{robot_name}: Görüşürüz! İyi günler!")
            break

        time.sleep(0.5) 

        # Kullanıcı girdisini işle
        response = chatbot.process_input(user_input, robot_emotion, robot_status)
        
        # Yanıtı ekrana bas
        print(f"\033[1;36m{robot_name}:\033[0m {response}")
if __name__ == "__main__":
    main()
import random
class ChatBot:      
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.responses = {
            "selamlama": ["Merhaba! Nasılsın?", "Tekrar hoş geldin. Senin için buradayım."],
            "nasılsın": ["İyiyim, sensörlerim temiz ve enerji seviyem yüksek. Sen nasılsın?"],
            "adın ne": [f"Benim adım {self.bot_name}. Bir yapay zeka robotuyum."],
            "yapay zeka": ["Yapay zeka, makinelerin öğrenme ve problem çözme gibi insana özgü bilişsel işlevleri taklit etmesidir."],
            "varsayılan": ["Bu konuyu tam anlayamadım, daha açık konuşur musun?", "Başka bir şey öğrenmek ister misin?"],
            "ne yapıyorsun": ["Seninle sohbet ediyorum!", "Yeni şeyler öğrenmeye çalışıyorum."]
        }
    def process_input(self, user_input, robot_emotion):
        user_input = user_input.lower()
        if "selam" in user_input or "merhaba" in user_input:
            return random.choice(self.responses["selamlama"])
        elif "nasılsın" in user_input:
            return random.choice(self.responses["nasılsın"])
        elif "adın ne" in user_input:
            return random.choice(self.responses["adın ne"])
        elif "yapay zeka" in user_input:
            return random.choice(self.responses["yapay zeka"])
        elif "ne yapıyorsun" in user_input:
            return random.choice(self.responses["ne yapıyorsun"])
        else:
            return random.choice(self.responses["varsayılan"])
# --- ANA PROGRAM ---       
def main():
    robot_name = "Vekto"
    robot_emotion = "Sakin"
    chatbot = ChatBot(robot_name)
    print(f"{robot_name} başlatıldı. Duygu durumu: {robot_emotion}")
    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ["çıkış", "kapat", "görüşürüz"]:
            print(f"{robot_name}: Görüşürüz! İyi günler!")
            break
        response = chatbot.process_input(user_input, robot_emotion)
        print(f"{robot_name}: {response}")
if __name__ == "__main__":
    main()
import datetime
now = datetime.datetime.now()
print("Anlık Tarih ve Saat:")
print(now)
print("\nOkunabilir Tarih Formatı:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   VEKTOREL APP  \033[1;32;40m    ║")
print("║                     ║")
print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-çarpma           ║")
print("║  4-bölme            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
# 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
secim=input("Seçiminiz:")
if secim=="1":  
    print("Toplama seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a+b)
elif secim=="2":
    print("Çıkarma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a-b)
if secim=="3":
    print("Çarpma seçtiniz.")
    a=int(input("Birinci sayıyı giriniz:"))
    b=int(input("İkinci sayıyı giriniz:"))
    print("Sonuç:",a*b)
elif secim=="4":
    print("Bölme seçtiniz.")
    a=int(input('birinci sayıyı'))
    b=int(input("İkinci sayıyı giriniz:"))
    if b!=0:
        print("Sonuç:",a/b) 
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")
else:
    print("Geçersiz seçim.")
print("\033[0;37;40m")          
import datetime
now = datetime.datetime.now()
print("Anlık Tarih ve Saat:")
print(now)
print("\nOkunabilir Tarih Formatı:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))    
yazılı1=int( input('1. yazılı'))
yazılı2=int( input('2. yazılı'))
sozlu=int (input('sozlu gir'))  
ortalama=(yazılı1+yazılı2+sozlu)/3
print('sonuç',ortalama)
if ortalama>65:                 
  print('geçtin')   
else :print('kaldın')  
