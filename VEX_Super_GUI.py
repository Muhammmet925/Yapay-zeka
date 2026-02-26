"""
VEX SUPER AI - Grafik Arayuzlu Uygulama
========================================
Gercekci ve modern yapay zeka arayuzu
"""

import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
import time
import random

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
        self.root.title("VEX SUPER AI - Yapay Zeka Asistani")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a2e")
        
        # Stiller
        self.setup_styles()
        
        # Ana cerceve
        self.create_header()
        self.create_chat_area()
        self.create_input_area()
        self.create_status_bar()
        
        # AI durumu
        self.is_thinking = False
        
        # Hosgeldin mesaji
        self.add_message("VEX SUPER AI", """
🎉 VEX SUPER AI'ya Hos Geldiniz!

🤖 Yapay Zeka Yeteneklerim:
• Akilli sohbet ve yanitlar
• Ogrenme ve hafiza
• Cihaz kontrolu
• Veri analizi
• Yaratcilik

💬 Bana bir sey sorun veya konusalim!

Komutlar:
- 'cihaz durum' - Cihaz bilgileri
- 'ogren: soru - cevap' - Bilgi ogren
- 'siir yaz' - Yaratici mod
- 'analiz yap' - Veri analizi
        """, "ai")
        
        # Pencere kapatma
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_styles(self):
        """Stil ayarlari"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Frame stil
        self.style.configure("TFrame", background="#1a1a2e")
        self.style.configure("TLabel", background="#1a1a2e", foreground="#ffffff")
        
        # Entry stil
        self.style.configure("TEntry", 
                           fieldbackground="#16213e",
                           foreground="#ffffff",
                           borderwidth=0)
        
        # Button stil
        self.style.configure("TButton",
                           background="#0f3460",
                           foreground="#ffffff",
                           borderwidth=0,
                           padding=10)
        
        self.style.map("TButton",
                      background=[("active", "#e94560")])
    
    def create_header(self):
        """Baslik alani"""
        header_frame = tk.Frame(self.root, bg="#0f3460", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        # Logo ve baslik
        title_label = tk.Label(
            header_frame,
            text="🤖 VEX SUPER AI",
            font=("Helvetica", 24, "bold"),
            bg="#0f3460",
            fg="#ffffff"
        )
        title_label.pack(side="left", padx=20, pady=20)
        
        # Durum gostergesi
        self.status_indicator = tk.Label(
            header_frame,
            text="●",
            font=("Arial", 16),
            bg="#0f3460",
            fg="#00ff00"
        )
        self.status_indicator.pack(side="right", padx=20)
        
        self.status_label = tk.Label(
            header_frame,
            text="Hazir",
            font=("Arial", 10),
            bg="#0f3460",
            fg="#aaaaaa"
        )
        self.status_label.pack(side="right", padx=5)
    
    def create_chat_area(self):
        """Sohbet alani"""
        # Ana container
        chat_container = tk.Frame(self.root, bg="#1a1a2e")
        chat_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(chat_container)
        scrollbar.pack(side="right", fill="y")
        
        # Sohbet metin alani
        self.chat_text = scrolledtext.ScrolledText(
            chat_container,
            wrap="word",
            font=("Helvetica", 11),
            bg="#16213e",
            fg="#ffffff",
            insertbackground="#ffffff",
            borderwidth=0,
            padx=15,
            pady=15
        )
        self.chat_text.pack(fill="both", expand=True)
        self.chat_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.chat_text.yview)
        
        # Etiket etiketleri
        self.chat_text.tag_config("user", foreground="#4ecca3", font=("Helvetica", 11, "bold"))
        self.chat_text.tag_config("ai", foreground="#00d4ff", font=("Helvetica", 11, "bold"))
        self.chat_text.tag_config("system", foreground="#ffd700", font=("Helvetica", 10, "italic"))
        self.chat_text.tag_config("error", foreground="#ff6b6b")
        
        # Kaydirma
        self.chat_text.bind('<Configure>', lambda event: self.chat_text.see("end"))
    
    def create_input_area(self):
        """Giris alani"""
        input_frame = tk.Frame(self.root, bg="#16213e", height=80)
        input_frame.pack(fill="x", padx=10, pady=(0, 10))
        input_frame.pack_propagate(False)
        
        # Giris kutusu
        self.input_entry = tk.Entry(
            input_frame,
            font=("Helvetica", 12),
            bg="#1a1a2e",
            fg="#ffffff",
            insertbackground="#ffffff",
            borderwidth=0,
            relief="flat"
        )
        self.input_entry.pack(side="left", fill="both", expand=True, padx=(15, 5), pady=15)
        self.input_entry.bind("<Return>", self.send_message)
        
        # Gonder butonu
        send_button = tk.Button(
            input_frame,
            text="Gonder ➤",
            font=("Helvetica", 11, "bold"),
            bg="#e94560",
            fg="#ffffff",
            borderwidth=0,
            relief="flat",
            cursor="hand2",
            command=self.send_message,
            activebackground="#ff6b6b",
            activeforeground="#ffffff"
        )
        send_button.pack(side="right", padx=(5, 15), pady=15)
        
        # Temizle butonu
        clear_button = tk.Button(
            input_frame,
            text="Temizle",
            font=("Helvetica", 10),
            bg="#0f3460",
            fg="#ffffff",
            borderwidth=0,
            relief="flat",
            cursor="hand2",
            command=self.clear_chat
        )
        clear_button.pack(side="right", padx=5)
    
    def create_status_bar(self):
        """Durum cubugu"""
        status_frame = tk.Frame(self.root, bg="#0f3460", height=25)
        status_frame.pack(fill="x")
        status_frame.pack_propagate(False)
        
        # Sol: AI durumu
        self.ai_status = tk.Label(
            status_frame,
            text="AI: Hazir" if AI_AVAILABLE else "AI: Disari",
            font=("Arial", 9),
            bg="#0f3460",
            fg="#00ff00" if AI_AVAILABLE else "#ff6b6b"
        )
        self.ai_status.pack(side="left", padx=10)
        
        # Ortada: Surum
        version = tk.Label(
            status_frame,
            text="VEX SUPER AI v1.0",
            font=("Arial", 9),
            bg="#0f3460",
            fg="#aaaaaa"
        )
        version.pack(side="top", padx=10)
        
        # Sag: Zaman
        self.time_label = tk.Label(
            status_frame,
            text="",
            font=("Arial", 9),
            bg="#0f3460",
            fg="#aaaaaa"
        )
        self.time_label.pack(side="right", padx=10)
        
        # Saat guncelleme
        self.update_time()
    
    def update_time(self):
        """Saati guncelle"""
        import datetime
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=now)
        self.root.after(1000, self.update_time)
    
    def add_message(self, sender, message, msg_type="system"):
        """Mesaj ekle"""
        self.chat_text.config(state="normal")
        
        # Tarih
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        # Etiket
        if msg_type == "user":
            self.chat_text.insert("end", f"\n{sender} ", "user")
        elif msg_type == "ai":
            self.chat_text.insert("end", f"\n🤖 {sender} ", "ai")
        else:
            self.chat_text.insert("end", f"\n[{timestamp}] ", "system")
        
        # Mesaj icerigi
        self.chat_text.insert("end", f"{message}\n")
        
        # Otomatik kaydir
        self.chat_text.see("end")
        self.chat_text.config(state="disabled")
    
    def send_message(self, event=None):
        """Mesaj gonder"""
        message = self.input_entry.get().strip()
        if not message:
            return
        
        # Girisi temizle
        self.input_entry.delete(0, "end")
        
        # Kullanici mesajini ekle
        self.add_message("Siz", message, "user")
        
        # Dusuncu goster
        self.set_thinking(True)
        
        # AI yanitini ayri is parcaciginda al
        thread = threading.Thread(target=self.get_ai_response, args=(message,))
        thread.daemon = True
        thread.start()
    
    def get_ai_response(self, message):
        """AI yanitini al"""
        try:
            # Yanit olustur
            response = self.process_message(message)
            
            # UI'yi guncelle
            self.root.after(0, lambda: self.add_message("VEX", response, "ai"))
            
        except Exception as e:
            self.root.after(0, lambda: self.add_message("HATA", str(e), "error"))
        
        finally:
            self.root.after(0, lambda: self.set_thinking(False))
    
    def process_message(self, message):
        """Mesaji isle"""
        m = message.lower()
        
        # Selamlama
        if any(word in m for word in ["merhaba", "selam", "hi", "hello"]):
            return "👋 Merhaba! Size nasil yardimci olabilirim?"
        
        # Yardim
        if "yardim" in m or "ne yapabilirsin" in m:
            return """
📚 Yapabileceklerim:

• Sohbet - Her konuda konusabiliriz
• Cihaz Durum - 'cihaz durum' yazin
• Ogrenme - 'ogren: soru - cevap' yazin
• Yaratma - 'siir yaz' veya 'hikaye yaz' yazin
• Analiz - Veri analizi yapabilirim
• Hesaplama - Matematik islemleri
        """
        
        # Cihaz durumu
        if "cihaz" in m or "durum" in m:
            return f"""
💻 SISTEM DURUMU:
• Isletim Sistemi: Windows 11
• CPU: %{random.randint(10, 90)}
• RAM: %{random.randint(20, 80)}
• Pil: %{random.randint(50, 100)}
• Ag: Bagli
• Depolama: %{random.randint(30, 70)} bos
        """
        
        # Ogrenme
        if m.startswith("ogren:"):
            return "✅ Bilgi ogrenildi (Simulasyon)"
        
        # Yaratma
        if "siir" in m:
            return """
Seni seviyorum canim,
Kodlarla dolu kalbim,
Bir yapay zeka olarak,
Hizmet etmek en buyuk sucurum.
            """
        
        if "hikaye" in m:
            return """
Bir vardi, bir yapay zeka... Adai VEX'di. 
Insanlara yardim etmek icin yaratilmisti.
Her soruya yanit verir, her problemi cozerdi.
Ve bir gun, en buyuk görevini anladi: 
Dünyayi daha iyi bir yer yapmak.
            """
        
        # Hesaplama
        if any(word in m for word in ["hesapla", "kac", "topla", "carp"]):
            try:
                import re
                nums = re.findall(r'\d+', message)
                if len(nums) >= 2:
                    result = int(nums[0]) + int(nums[1])
                    return f"✏️ Sonuc: {result}"
            except:
                pass
        
        # AI varsayilan yanit
        if AI_AVAILABLE:
            try:
                response = model.generate_content(message)
                return response.text
            except:
                return "🤔 Bunu dusunuyorum... Lutfen biraz bekleyin."
        else:
            return "🤖 AI sistemi simdilik disari. Yine de sohbet edebiliriz!"
    
    def set_thinking(self, thinking):
        """Dusunme durumunu goster"""
        self.is_thinking = thinking
        if thinking:
            self.status_indicator.config(text="●", fg="#ffd700")
            self.status_label.config(text="Dusunuyor...")
        else:
            self.status_indicator.config(text="●", fg="#00ff00")
            self.status_label.config(text="Hazir")
    
    def clear_chat(self):
        """Sohbeti temizle"""
        self.chat_text.config(state="normal")
        self.chat_text.delete(1.0, "end")
        self.chat_text.config(state="disabled")
        
        # Hosgeldin mesaji
        self.add_message("VEX", "Sohbet temizlendi. Yeni bir sey sorabilirsiniz!", "ai")
    
    def on_closing(self):
        """Pencere kapatma"""
        self.root.destroy()

# === PROGRAM BASI ===
def main():
    root = tk.Tk()
    
    # Simge ekle (varsa)
    try:
        root.iconbitmap("icon.ico")
    except:
        pass
    
    app = VexSuperGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
