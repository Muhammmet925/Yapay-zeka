"""
VEX PRO - Ust Seviye Yapay Zeka Asistenti
=========================================
"""

import random
import re
import os
import json
import datetime

# --- GEMINI AI ---
import google.generativeai as genai
genai.configure(api_key="AIzaSyD21iLD8C6NZz5fARyvB2AqxatO92vQfGk")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- VERI TABANI ---
DATA_FILE = "yapay_zeka_data.json"

class SmartHome:
    """Akilli Ev Kontrol Sistemi"""
    def __init__(self):
        self.devices = {
            "isiklar": False,
            "klima": 22,
            "perde": "kapali",
            "kapi": "kilitli",
            "alarm": False
        }
    
    def control(self, device, action):
        if device == "isik":
            self.devices["isiklar"] = action == "ac"
            return f"Isiklar {'acildi' if action == 'ac' else 'kapandi'}"
        elif device == "kapi":
            self.devices["kapi"] = action
            return f"Kapi {action}"
        elif device == "alarm":
            self.devices["alarm"] = action == "ac"
            return f"Alarm {'aktif' if action == 'ac' else 'pasif'}"
        elif device == "perde":
            self.devices["perde"] = action
            return f"Perdeler {action}"
        elif device == "klima":
            try:
                self.devices["klima"] = int(action)
                return f"Klima {action} dereceye ayarlandi"
            except:
                return "Klima sicakligini anlayamadim"
        return "Cihaz bulunamadi"
    
    def get_status(self):
        return json.dumps(self.devices, ensure_ascii=False, indent=2)

class PersistentMemory:
    """Kalici Hafiza ve Ogrenme"""
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.data = self.load()
    
    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return {"bilgiler": {}, "tercihler": {}, "gecmis": []}
        return {"bilgiler": {}, "tercihler": {}, "gecmis": []}
    
    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def learn(self, question, answer):
        self.data["bilgiler"][question.lower()] = answer
        self.save()
        return f"Ogrendim: {question} -> {answer}"
    
    def add_to_history(self, user, bot, time):
        self.data["gecmis"].append({"kullanici": user, "bot": bot, "zaman": time})
        if len(self.data["gecmis"]) > 100:
            self.data["gecmis"] = self.data["gecmis"][-100:]
        self.save()

class VexPro:
    """UST SEVIYE YAPAY ZEKA"""
    
    def __init__(self):
        self.name = "VEX PRO"
        self.memory = PersistentMemory()
        self.smart_home = SmartHome()
        self.conversation_count = 0
        
        print("="*60)
        print("VEX PRO - UST SEVIYE YAPAY Zeka")
        print("="*60)
        print("Yeni Ozellikler:")
        print("  - Akilli Ev Kontrolu")
        print("  - Kalici Hafiza ve Ogrenme")
        print("  - Hava Durumu ve Haberler")
        print("="*60)
    
    def process(self, user_input):
        """Ana islemci"""
        self.conversation_count += 1
        user_lower = user_input.lower()
        
        # Tarih/saat
        if "saat" in user_lower or "zaman" in user_lower:
            return self.get_time()
        
        # Hafiza islemleri
        if "ne ogrendin" in user_lower:
            return self.show_memory()
        
        if user_lower.startswith("sil:"):
            key = user_lower.replace("sil:", "").strip()
            return self.delete_memory(key)
        
        # Akilli ev
        if any(word in user_lower for word in ["isik", "kapi", "alarm", "perde", "klima"]):
            return self.control_home(user_lower)
        
        if "ev durumu" in user_lower:
            return f"Ev Durumu:\n{self.smart_home.get_status()}"
        
        # Hava durumu
        if "hava" in user_lower:
            return self.get_weather()
        
        # Haberler
        if "haber" in user_lower:
            return self.get_news()
        
        # Ogrenme
        if user_lower.startswith("ogren:"):
            return self.learn(user_lower)
        
        # Sistem kontrolu
        if "sistem" in user_lower or "pc ozellikleri" in user_lower:
            return self.get_system_info()
        
        # Gemini AI
        return self.ai_response(user_input)
    
    def get_time(self):
        now = datetime.datetime.now()
        return f"Tarih: {now.strftime('%d %B %Y')}\nSaat: {now.strftime('%H:%M')}\nGun: {now.strftime('%A')}"
    
    def show_memory(self):
        bilgiler = self.memory.data.get("bilgiler", {})
        if not bilgiler:
            return "Henuz bir sey ogrenmedim."
        result = "Ogrendigim Bilgiler:\n"
        for i, (s, c) in enumerate(bilgiler.items(), 1):
            result += f"{i}. {s} -> {c}\n"
        return result
    
    def delete_memory(self, key):
        bilgiler = self.memory.data.get("bilgiler", {})
        if key in bilgiler:
            del bilgiler[key]
            self.memory.save()
            return f"Silindi: {key}"
        return "Bulunamadi."
    
    def learn(self, text):
        try:
            parts = text.replace("ogren:", "").split("-")
            if len(parts) == 2:
                return self.memory.learn(parts[0].strip(), parts[1].strip())
        except:
            pass
        return "Ogrenme formati: ogren: soru - cevap"
    
    def control_home(self, text):
        if "isik" in text:
            if "ac" in text:
                return self.smart_home.control("isik", "ac")
            elif "kapat" in text:
                return self.smart_home.control("isik", "kapat")
        
        if "kapi" in text:
            if "ac" in text:
                return self.smart_home.control("kapi", "acik")
            elif "kilit" in text:
                return self.smart_home.control("kapi", "kilitli")
        
        if "alarm" in text:
            if "ac" in text:
                return self.smart_home.control("alarm", "ac")
            elif "kapat" in text:
                return self.smart_home.control("alarm", "kapat")
        
        if "klima" in text:
            match = re.search(r'(\d+)', text)
            if match:
                return self.smart_home.control("klima", match.group(1))
        
        return "Komutu anlayamadim. Ornek: 'isiklari ac', 'kapiyi kilitle', 'alarm acik'"
    
    def get_weather(self):
        conditions = ["gunesli", "yagmurlu", "bulutlu"]
        cond = random.choice(conditions)
        temp = random.randint(5, 35)
        hava = {
            "gunesli": f"Bugun gunesli, {temp}C",
            "yagmurlu": f"Yagmurlu, {temp}C, semsiye al!",
            "bulutlu": f"Bulutlu, {temp}C"
        }
        return hava[cond]
    
    def get_news(self):
        return """
GUNDEM:
1. Yapay zeka teknolojileri hizla gelisiyor
2. Akilli ev sistemleri popülerlesiyor
3. Python en populer programlama dili
4. Turkiye'de teknoloji yatirimlari artiyor
"""
    
    def get_system_info(self):
        import platform
        try:
            import psutil
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            return f"Sistem Bilgileri:\n- Isletim Sistemi: {platform.system()}\n- CPU: %{cpu}\n- RAM: %{ram}\n- Disk: %{disk}"
        except:
            return f"Sistem: {platform.system()}"
    
    def ai_response(self, text):
        """Gemini AI yaniti"""
        try:
            response = model.generate_content(text)
            return response.text
        except Exception as e:
            return f"Bir hata olustu: {str(e)[:100]}"
    
    def run(self):
        """Ana dongu"""
        print("\nVEX PRO hazir! Bir seyler yazin veya 'cikis' yazin.\n")
        
        while True:
            try:
                user_input = input("Siz: ")
            except EOFError:
                break
            
            if user_input.lower() in ["cikis", "exit", "quit"]:
                print("\nVEX PRO: Gorusuruz!")
                break
            
            response = self.process(user_input)
            self.memory.add_to_history(user_input, response[:100], str(datetime.datetime.now()))
            
            print(f"\nVEX PRO: {response}\n")

# === BASLANGIC ===
if __name__ == "__main__":
    vex = VexPro()
    vex.run()
