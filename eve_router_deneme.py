from netmiko import ConnectHandler

# EVE-NG Router Bilgileri
# Windows CMD hatasından anladığım kadarıyla IP ve Port erişimi var.
# Sorun sadece Python tarafındaki eski parametrelerdeydi.
eve_ng_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.78.129',  # Sizin EVE-NG IP'niz
    'username': 'ferhat',      # Router'da 'username ferhat...' ile oluşturduğunuz kullanıcı
    'password': 'ferhat',       # Şifreniz
    'port': 22,
    # Hata veren o iki satırı SİLDİK.
}

print("EVE-NG Router'ına bağlanılıyor...")

try:
    baglanti = ConnectHandler(**eve_ng_router)
    print("✅ BAĞLANTI BAŞARILI! İçerdeyiz.")
    
    # Basit bir komut deneyelim
    cikti = baglanti.send_command("show ip interface brief")
    
    print("-" * 30)
    print(cikti)
    print("-" * 30)
    
    baglanti.disconnect()

except Exception as hata:
    print(f"❌ Hata Oluştu: {hata}")
    print("\n--- OLASI ÇÖZÜMLER ---")
    print("1. Eğer 'Authentication failed' diyorsa: Kullanıcı adı veya şifre yanlıştır.")
    print("2. Eğer 'Timeout' diyorsa: IP yanlıştır veya router kapalıdır.")