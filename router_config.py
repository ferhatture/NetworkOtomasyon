from netmiko import ConnectHandler

# 1. Cihaz Bilgileri (IOS-XR)
cisco_router = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
}

print("Router'a bağlanılıyor...")
baglanti = ConnectHandler(**cisco_router)
print("Bağlantı başarılı! Konfigürasyon gönderiliyor...")

# 2. GÖNDERİLECEK KOMUTLAR
# Burada 55 numaralı Loopback'i oluşturuyoruz.
# İstediğiniz numarayı verebilirsiniz (Örn: Loopback88)
komutlar = [
    'interface Loopback60',
    'description BU_INTERFACE_PYTHON_ILE_ACILDI',
    'ipv4 address 60.06.60.06 255.255.255.255',
    'commit'  # IOS-XR cihazlarda değişikliği kaydetmek için 'commit' şarttır!
]

# 3. Komutları Uyguluyoruz (send_config_set kullanılır)
cikti = baglanti.send_config_set(komutlar)
print("Konfigürasyon tamamlandı!")

# 4. Doğrulama Yapıyoruz (Interface gelmiş mi?)
son_durum = baglanti.send_command("show ip interface brief")
print(son_durum)

# 5. Çıktıyı Bilgisayara Kaydediyoruz (Raporlama)
dosya_adi = "router_raporu.txt"
with open(dosya_adi, "w") as dosya:
    dosya.write("--- KONFIGURASYON LOGLARI ---\n")
    dosya.write(cikti)
    dosya.write("\n\n--- SON DURUM ---\n")
    dosya.write(son_durum)

print(f"\nİşlem bitti! Sonuçlar '{dosya_adi}' dosyasına kaydedildi.")

baglanti.disconnect()