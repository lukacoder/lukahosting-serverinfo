import platform
import socket

def get_server_info():
    # İşletim sistemi bilgilerini al
    os_name = platform.system()
    os_version = platform.release()

    # Host adını ve IP adresini al
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Server özelliklerini ve işletim sistemi bilgilerini ekrana yazdır
    print("Server Özellikleri:")
    print("Hostname:", hostname)
    print("IP Adresi:", ip_address)
    print("İşletim Sistemi:", os_name)
    print("İşletim Sistemi Sürümü:", os_version)

# Server bilgilerini al
get_server_info()
