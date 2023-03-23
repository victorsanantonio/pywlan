# wlanvenom
Aplicación de consola escrita en Python la cual incluye algunas utilidades empleando el módulo scapy.
## Introducción

Utilidades que incluye
1. Escaneo de dispositivos (Scan devices on WLAN)
2. Escaneo de puertos (Scan ports of an specific device)
3. Suplantación de ARP (ARP spoofing)
<details>
  <summary>Saber más</summary>
  
  ### Aclaraciones
  - Desde que me empecé a interesar por la __ciberseguridad__ mientras me formaba en __Python__, siempre había deseado crear mi propia aplicación con utilidades para este campo.
  - He decidido recopilar __tres sencillas utilidades__ en una única __aplicación__ de consola para así poder afianzar mi __proceso de aprendizaje__.
  - La aplicación consume, principalmente, métodos del módulo __scapy__. Muy útil y comúnmente empleado para la __manipulación de paquetes en red__.
</details>

<details>
  <summary>Requerimientos</summary>
  
  ### Requerimientos técnicos
  - Para instalar y ejecutar correctamente el proyecto, deberás tomar las siguientes consideraciones:
    1. Tener __Git__ instalado.
    2. Sistema operativo __Windows__ con el driver [WinPcap](https://www.winpcap.org) versión __4.1.3__ instalado.
    3. Tener __Python__ instalado.
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

## Uso
- Una vez estés en la raíz del proyecto, ejecuta el siguiente comando.
```
python main.py
```
