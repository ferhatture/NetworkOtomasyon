from netmiko import ConnectHandler

# 1. Cihaz Bilgileri 
eve_ng_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.78.129', #
    'username': 'ferhat',
    'password': 'cisco',
    'port': 22,
}

print("Siber Güvenlik Denetimi Başlıyor...")
try:
    baglanti = ConnectHandler(**eve_ng_router)
    
    # YENİ KOMUT 1: find_prompt()
    # Cihazın o anki promptunu (Örn: Router# veya R1#) otomatik bulur.
    cihaz_adi = baglanti.find_prompt()
    # 
    cihaz_adi = cihaz_adi.replace("#", "").replace(">", "")
    
    print(f"✅ Bağlanılan Cihaz: {cihaz_adi}")
    
    # 2. DENETİM (AUDIT) AŞAMASI
    # Şifreleme servisi açık mı?
    komut = "show running-config | include service password-encryption"
    cikti = baglanti.send_command(komut)
    
    # 3. AKILLI KARAR MEKANİZMASI (Logic)
    # 
    if "service password-encryption" in cikti:
        print("🟢 DURUM: GÜVENLİ. Şifreleme servisi zaten aktif.")
        print("   -> Hiçbir değişiklik yapılmadı.")
        
    else:
        print("🔴 DURUM: RİSKLİ! Şifreleme servisi kapalı.")
        print("   -> 🛠️ Otomatik onarım devreye giriyor...")
        
        # 
        duzeltme = ["service password-encryption"]
        baglanti.send_config_set(duzeltme)
        
        print("   -> ✅ Servis aktif edildi ve açık kapatıldı.")
        
        baglanti.save_config()
        print("   -> Konfigürasyon kaydedildi.")

    baglanti.disconnect()

except Exception as hata:
    print(f"❌ Hata: {hata}")