from netmiko import ConnectHandler

# 1. Cihaz Bilgileri (Sizin çalışan bilgileriniz)
eve_ng_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.78.129', # EVE-NG IP'niz
    'username': 'ferhat',     # Kullanıcı adınız
    'password': 'ferhat',
    'port': 22,
}

print("Router'a bağlanılıyor...")
baglanti = ConnectHandler(**eve_ng_router)
print("✅ Bağlantı Başarılı! Toplu işlem başlıyor...")

# 2. CONFIG MODUNA GEÇİŞ VE DÖNGÜ (LOOP)
# Netmiko'da config göndermek için 'send_config_set' kullanılır.
# Ama biz burada Python'un gücünü kullanarak komut listesini otomatik üreteceğiz.

config_komutlari = [] # Boş bir sepet (liste) oluşturduk

# 10'dan 15'e kadar (15 dahil değil) sayıları döndür
# Yani: 10, 11, 12, 13, 14 numaralı loopbackleri açacağız.
for i in range(10, 15):
    print(f"Listeye ekleniyor: Loopback{i}")
    
    # Sepete komutları atıyoruz
    config_komutlari.append(f"interface Loopback{i}")
    config_komutlari.append(f"description Python_ile_Acildi_No_{i}")
    config_komutlari.append(f"ip address 10.10.10.{i} 255.255.255.255")
    # IOS (EVE-NG) cihazlarda 'no shut' demeye gerek yok loopback için ama alışkanlık olsun
    config_komutlari.append("no shutdown")

print("\nHazırlanan komutlar router'a gönderiliyor...")

# 3. HEPSİNİ TEK SEFERDE GÖNDER
cikti = baglanti.send_config_set(config_komutlari)

# 4. SONUCU GÖRELİM
print("\n--- İŞLEM SONUCU ---")
print(baglanti.send_command("show ip int brief | include Loopback"))

baglanti.disconnect()