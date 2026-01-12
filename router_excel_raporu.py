import csv
from netmiko import ConnectHandler

# 1. Cihaz Bilgileri
cisco_router = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
    # Hata almamak için güvenlik uyarılarını geçiyoruz
    'global_delay_factor': 2  
}

print("Router'a bağlanılıyor ve veriler çekiliyor...")

try:
    baglanti = ConnectHandler(**cisco_router)
    
    # Komutu gönderiyoruz
    ham_cikti = baglanti.send_command("show ip interface brief")
    
    # 2. Veriyi İşleme (Parsing) Kısmı
    # Çıktıyı satır satır bölüyoruz
    satirlar = ham_cikti.splitlines()
    
    # CSV (Excel) dosyasını oluşturuyoruz
    dosya_adi = "network_envanteri.csv"
    
    with open(dosya_adi, mode='w', newline='', encoding='utf-8') as dosya:
        yazici = csv.writer(dosya)
        
        # Başlıkları yazalım
        yazici.writerow(["Interface", "IP Adresi", "Durum (Status)", "Protokol"])
        
        print("Veriler Excel formatına dönüştürülüyor...")
        
        # İlk 2 satır genelde başlıktır, onları atlıyoruz (IOS-XR için)
        for satir in satirlar[2:]:
            # Boş satırları atla
            if not satir.strip():
                continue
                
            # Satırı kelimelere ayır (Python boşlukları otomatik algılar)
            kelimeler = satir.split()
            
            # Eğer satırda yeterince bilgi varsa al
            if len(kelimeler) >= 4:
                interface_adi = kelimeler[0]
                ip_adresi = kelimeler[1]
                durum = kelimeler[2]
                protokol = kelimeler[3]
                
                # Excel'e yaz
                yazici.writerow([interface_adi, ip_adresi, durum, protokol])

    print(f"✅ Başarılı! Masaüstünüzdeki '{dosya_adi}' dosyasını açabilirsiniz.")
    baglanti.disconnect()

except Exception as hata:
    print(f"Hata: {hata}")