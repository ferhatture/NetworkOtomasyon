from netmiko import ConnectHandler

# IOS-XR Router Bilgileri (Gereksiz satırlar temizlendi)
cisco_router = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
}

print("Alternatif Router'a (IOS-XR) bağlanılıyor...")

try:
    # Parametreleri temizledik, doğrudan bağlanıyoruz
    baglanti = ConnectHandler(**cisco_router)
    print("Bağlantı Başarılı! Komut gönderiliyor...")
    
    # Komutu gönderiyoruz
    cikti = baglanti.send_command("show ip interface brief")
    
    print("-" * 50)
    print(cikti)
    print("-" * 50)
    
    baglanti.disconnect()

except Exception as hata:
    print(f"BİR HATA OLUŞTU:\n{hata}")