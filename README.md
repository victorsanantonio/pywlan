# wlanvenom
Aplicación de consola escrita en Python la cual incluye algunas utilidades empleando el módulo scapy.
## Introducción

Las utilidades que contiene la aplicación son las siguientes:
1. Escaneo de dispositivos (Scan devices on WLAN)
2. Escaneo de puertos (Scan ports of an specific device)
3. Suplantación de ARP (ARP spoofing)
<details>
  <summary>Saber más</summary>
- Desde que me empecé a interesar por la _ciberseguridad_ mientras me formaba en _Python_, siempre había deseado crear mi propia aplicación con utilidades para este campo.
- He decidido recopilar _tres sencillas utilidades_ en una única _aplicación_ de consola para así poder afianzar mi _proceso de aprendizaje_.
- La aplicación consume, principalmente, métodos del módulo _scapy_. Muy útil y comúnmente empleado para la _manipulación de paquetes en red_.
</details>
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
