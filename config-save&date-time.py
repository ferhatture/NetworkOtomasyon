from netmiko import ConnectHandler
import datetime  # 1. YENİ KÜTÜPHANE: Zamanı yönetmek için

# Cihaz Bilgileri
eve_ng_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.78.129', # Kendi IP'niz
    'username': 'ferhat',
    'password': 'cisco',
    'port': 22,
}

# 2. ZAMANI AYARLAMA (Logic Kısmı)
# Şu anki zamanı alıyoruz
anlik_zaman = datetime.datetime.now()

# Zamanı temiz bir metne çeviriyoruz (Yıl-Ay-Gün_Saat-Dakika)
# %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute
zaman_damgasi = anlik_zaman.strftime("%Y-%m-%d_%H-%M-%S")

print(f"İşlem saati: {zaman_damgasi}")
print("Router'a bağlanılıyor...")

baglanti = ConnectHandler(**eve_ng_router)

# save_config()
# Bu komut router'a 'write memory' gönderir ve tamamlanmasını bekler.
print("Router üzerindeki konfigürasyon diske yazılıyor (write mem)...")
kayit_sonucu = baglanti.save_config()
print(kayit_sonucu)

# 4. KONFIGURASYONU ÇEKME
print("Show run çekiliyor...")
tam_konfig = baglanti.send_command("show run")

# 5. DOSYA İSMİNİ OLUŞTURMA (Dinamik İsimlendirme)
# Dosya adı şöyle olacak: backup_192.168.78.129_2023-10-27_14-30-05.txt
dosya_adi = f"backup_{eve_ng_router['host']}_{zaman_damgasi}.txt"

# Dosyayı kaydetme
with open(dosya_adi, "w") as dosya:
    dosya.write(tam_konfig)

print(f"✅ YEDEK ALINDI! Dosya adı: {dosya_adi}")

baglanti.disconnect()