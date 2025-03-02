# ARPscanner
**ARPscanner** es un programa de red desarrollado en Python que utiliza la biblioteca `scapy` para realizar escaneos ARP en un host o rango de IPs objetivo. El programa permite identificar dispositivos activos en la red a través del protocolo ARP (Address Resolution Protocol).

## Características
- Escaneo de dispositivos en una red local utilizando ARP.
- Capacidad para especificar un host o rango de IPs objetivo.
- Muestra una lista de dispositivos que han respondido al paquete ARP.
- Manejo de señales SIGINT (Ctrl+C) para salir del programa de manera segura.

## Requisitos

- Python 3.x
- Biblioteca `scapy` (puede instalarse con `pip install scapy`)
- Biblioteca `termcolor` (puede instalarse con `pip install termcolor`)

## Uso

1. Abre una terminal y ejecuta el programa con privilegios de administrador (ya que las operaciones ARP suelen requerir permisos elevados).
2. Proporciona el parámetro `-t` o `--target` seguido del host o rango de IPs que deseas escanear. Por ejemplo:
    ```bash
    sudo python3 ARPscanner.py -t 192.168.1.0/24
    ```

   - El argumento `-t` (o `--target`) es obligatorio y define el host o rango de IPs a escanear. Ejemplo: `192.168.1.0/24` para escanear toda la subred.

3. Si deseas detener el programa durante el escaneo, presiona `Ctrl+C`. El programa manejará la interrupción de manera segura y mostrará un mensaje de salida.

## Ejemplo de Salida

Al ejecutar el programa correctamente, se verá una salida similar a la siguiente:

```bash
Ether / ARP who has 192.168.1.1 says 192.168.1.10
Ether / ARP who has 192.168.1.2 says 192.168.1.20
```
