import cv2
import numpy as np

# 200x200 RGB görüntüsü oluştur (cv2 BGR: [B, G, R])
height, width = 200, 200
r1 = np.full((height, width, 3), [255, 0, 255], dtype=np.uint8)  # Magenta arkaplan [B=255, G=0, R=255]

print("Desenli görüntü oluşturuluyor...")

# Piksel piksel desen uygula
for a in range(height):
    for b in range(width):
        # Yatay şeritler: her 10 satırda 5 siyah
        if a % 10 < 5:
            r1[a, b] = [0, 0, 0]  # Siyah
        
        # Dikey şeritler: her 10 sütunda 5 beyaz
        if b % 10 < 5:
            r1[a, b] = [255, 255, 255]  # Beyaz
        
        # Ana diyagonal (a == b): mavi
        if a == b:
            r1[a, b] = [255, 0, 0]  # Mavi [B=255,G=0,R=0]
        
        # Anti-diyagonal (height - 1 - a == b): yeşil
        if height - 1 - a == b:
            r1[a, b] = [0, 255, 0]  # Yeşil [B=0,G=255,R=0]
        
        # Anti-diyagonal etrafında kırmızı bant (yaklaşık 7 piksel genişlik)
        anti_diag_col = height - 1 - a
        if anti_diag_col - 3 <= b <= anti_diag_col + 3:  # Band genişliği ~7
            r1[a, b] = [0, 0, 255]  # Kırmızı [B=0,G=0,R=255]

# Görüntüyü göster
cv2.imshow("Desenli Görüntü (q ile kapat)", r1)
cv2.imwrite("pattern_image.png", r1)
print("Görüntü kaydedildi: pattern_image.png")
print("Kapatmak için 'q' tuşuna basın...")

tus = cv2.waitKey(0)
while tus != ord('q'):
    tus = cv2.waitKey(0)

cv2.destroyAllWindows()
print("Program tamamlandı.")
