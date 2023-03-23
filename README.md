# wlanvenom
Aplicación de consola escrita en Python la cual incluye algunas utilidades empleando el módulo scapy.

## Índice
- [Introducción](#id_introduccion)
- [Instalación (CLI)](#id_instalacion)
- [Uso](#id_uso)
- [Menú principal](#id_menu_principal)
- [Funcionalidades](#id_funcionalidades)
  - [1. Escáner de dispositivos](#id_escaner_dispositivos)
    -[Exportado de datos](#id_exportado_datos)
  - [2. Escáner de puertos](#id_escaner_puertos)
- [Paradigma](#id_paradigma)
  - [Ejemplos](#id_ejemplos)

## Introducción<a name="id_introduccion"></a>
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
  Para instalar y ejecutar correctamente el proyecto, deberás tomar las siguientes consideraciones:
  1. Tener __Git__ instalado.
  2. Tener __Python 3__ instalado.
  3. Sistema operativo __Windows__ con el driver [WinPcap](https://www.winpcap.org) versión __4.1.3__ instalado.
</details>

## Instalación (CLI)<a name="id_instalacion"></a>
- Descargar repositorio
```sh
git clone https://github.com/victorsanantonio/wlanvenom.git
```
- Posicionarse en la raíz del proyecto
```sh
cd wlanvenom/
```
- Instalar dependencias
```sh
pip install -r requirements.txt
```

## Uso<a name="id_uso"></a>
- Una vez estés en la raíz del proyecto, ejecuta el siguiente comando.
```sh
python main.py
```
## Menú principal<a name="id_menu_principal"></a>
Este es el menú con el que podemos interaccionar con la aplicación.
![image](https://user-images.githubusercontent.com/82669128/227251047-aa060e20-b8a3-4dd2-8900-eb0463e295d3.png)

## Funcionalidades<a name="id_funcionalidades"></a>
### 1. Escáner de dispositivos<a name="id_escaner_dispositivos"></a>
Pulsa la tecla 1 y ENTER para acceder al escáner de dispositivos.
A continuación, solicitará que ingresemos un rango de IP:
![image](https://user-images.githubusercontent.com/82669128/227253167-486b50a1-2147-4ce4-8337-bea42b492ae8.png)

> El rango de IPv4 que introduciremos, en mi caso será: `192.168.1.0/24`

Estos son los dispositivos conectados a mi red:

![image](https://user-images.githubusercontent.com/82669128/227255695-d0c6750c-e034-4223-ab65-71112d53b43a.png)
___Como se puede apreciar, conocemos su IP privada y su dirección de MAC.___

### Exportado de datos<a name="id_exportado_datos"></a>
> Nota: Si deseas exportar los resultados, introduce la palabra `Yes` o la letra `Y`:
> ![image](https://user-images.githubusercontent.com/82669128/227256716-964a378f-99f3-490e-b687-adfa283087d2.png)

> Se generará un directorio `data/` en la raíz del proyecto con un archivo CSV.
> Esto funcionará de igual manera para la utilidad de escaneo de puertos.

### 2. Escáner de puertos<a name="id_escaner_puertos"></a>
Ahora que conocemos los dispositivos conectados a nuestra red...
Pulsa la tecla 2 y ENTER para acceder al escáner de puertos.

## Paradigma<a name="id_paradigma"></a>
Se hace uso principalmente del __paradigma__ de la __orientación a objetos__ con aplicaciones prácticas de __herencia__. Así como la implementación de __dataclasses__.
### Ejemplos<a name="id_ejemplos"></a>
#### Clases y herencia
```python
'''
Scanner es la clase padre.
Comparte métodos que serán usados por las tres funcionalidades principales
'''
class Scanner:
  pass


'''
Las siguientes clases heredan de Scanner.
Esto es debido a que comparten varios métodos, evitando duplicidad de código.
'''
class DeviceScanner(Scanner):
  pass

class PortScanner(Scanner):
  pass

class ARPSpoofer(Scanner):
  pass
```

#### Dataclasses
Para representar más fácilmente los resultados de los escaneos, se ha decidido representar las clases `Client` y `Port` como clases modelo:
```python
'''
Dataclass Cliente con atributos de su IP y su dirección MAC.
'''
class Client:
    ip: str
    mac: str

'''
Dataclass Puerto con atributos de su número y un booleano que indica si está abierto o cerrado.
'''
class Port:
    port: int
    is_opened: bool
```
