# wlanvenom
Aplicación de consola escrita en Python la cual incluye algunas utilidades empleando el módulo scapy.
## Introducción
Desde que me empecé a interesar por la ciberseguridad mientras me formaba en Python, siempre había deseado crear mi propia aplicación con utilidades para este campo.
Por ello, he decidido recopilar tres sencillas utilidades en una única aplicación de consola para así poder afianzar mi proceso de aprendizaje.
La aplicación consume, principalmente, métodos del módulo scapy. Muy útil y comúnmente empleado para la manipulación de paquetes de red.
Las utilidades que contiene la aplicación son las siguientes:
1. Escaneo de dispositivos (Scan devices on WLAN)
2. Escaneo de puertos (Scan ports of an specific device)
3. Suplantación de ARP (ARP spoofing)
## Instalación (CLI)
- Descargar repositorio
```sh
git clone https://github.com/victorsanantonio/wlanvenom.git
```
- Posicionarse en la raíz del proyecto
```
cd wlanvenom/
```
- Instalar dependencias
```
pip install -r requirements.txt
```
