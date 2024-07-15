# Author : Eduardo Esteves - copilotlabxgmail.com
# Egresado de SENATI 2024


import socket
import re
import nmap


def solicitar_ip():
    while True:
        ip = input("Ingrese una dirección IP en formato xxx.xxx.xxx.xxx: ")
        if validar_ip(ip):
            return ip
        else:
            print("La dirección IP ingresada no es válida. Inténtelo de nuevo.")

def validar_ip(ip):
    patron_ip = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(patron_ip, ip):
        partes = ip.split('.')
        if all(0 <= int(p) <= 255 for p in partes):
            return True
    return False


ip = solicitar_ip()
print(f"La dirección IP válida ingresada es: {ip}")
# Lista de puertos
puertos = [20, 21, 22, 25, 53, 67, 68, 69, 80, 110, 123, 143, 161, 162, 389, 443,445, 514, 520, 3306, 3389]

# Iterar sobre la lista de puertos de los puertos mas comunes usando el modulo socket
mi_lista_open = []
for puerto in puertos:
#for puerto in range(1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, puerto))
    
    if result == 0:
       mi_lista_open.append(puerto)       
       #print("El puerto abierto es: "  + str(puerto))
       #sock.close
    #else:
      # print("Nimgun Puerto de los mas usados esta abierto" )
if len(mi_lista_open) > 0:
     
     for i in range(len(mi_lista_open)):
           print("El puerto abierto: " + str(mi_lista_open[i]))
else:
     print("Ningún puerto(TCP/UDP) de los más usados está abierto." ) 

# Iterar sobre la lista de los 200 primeros puertos usando el modulo socket
print("Revisando el estado de los primeros 200 puertos con socket." ) 
mi_lista_open = []

for puerto in range(1,500):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, puerto))
    
    if result == 0:
       mi_lista_open.append(puerto)       
       
       sock.close
   
if (len(mi_lista_open)) > 0:
     
     for i in range(len(mi_lista_open)):
           print("El puerto abierto: " + str(mi_lista_open[i]))
else:
     print("Ningún de los primeros 200 puertos(TCP/UDP) están abierto." )

#Iterar sobre la lista de 500 primeros puertos con el modulo nmap
print("Revisando el estado de los primeros 500 puertos con nmap." ) 
nm = nmap.PortScanner()
nm.scan(ip, '1-500')
# Mostrar los resultados del escaneo
for host in nm.all_hosts():
    print(f'Host : {host} ({nm[host].hostname()})')
    print(f'State : {nm[host].state()}')
    
    for proto in nm[host].all_protocols():
        print('----------')
        print(f'Protocol : {proto}')

        lport = nm[host][proto].keys()
        for port in sorted(lport):
            print(f'Port : {port}\tState : {nm[host][proto][port]["state"]}')

#Iterar sobre la lista de 1000 primeros puertos con el modulo nmap
print("Revisando el estado de los primeros 1000 puertos con nmap." ) 
nm = nmap.PortScanner()
nm.scan(ip, '1-1000')
# Mostrar los resultados del escaneo
for host in nm.all_hosts():
    print(f'Host : {host} ({nm[host].hostname()})')
    print(f'State : {nm[host].state()}')
    
    for proto in nm[host].all_protocols():
        print('----------')
        print(f'Protocol : {proto}')

        lport = nm[host][proto].keys()
        for port in sorted(lport):
            print(f'Port : {port}\tState : {nm[host][proto][port]["state"]}')




