# HTTP Spoofer

**HTTP Spoofer** es una herramienta que intercepta y modifica el tráfico HTTP entre un cliente y un servidor. Utiliza `scapy` para manipular paquetes en la capa de transporte TCP y eliminar ciertos encabezados como `Accept-Encoding`. Esto puede ser útil para realizar pruebas de seguridad y análisis de tráfico en redes locales.

## Requisitos

- Python 3.x
- Biblioteca `scapy` (puede instalarse con `pip install scapy`)
- Biblioteca `netfilterqueue` (puede instalarse con `pip install netfilterqueue`)
- Paquete `iptables` en Linux (para redirigir el tráfico)

## Instalación

1. Instala las dependencias necesarias:
    ```bash
    pip install scapy netfilterqueue
    ```

2. Configura `iptables` para redirigir el tráfico HTTP a la cola de Netfilter:
    ```bash
    sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
    ```

    Si estás probando en la misma máquina, puedes usar:
    ```bash
    sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
    sudo iptables -I INPUT -j NFQUEUE --queue-num 0
    ```

## Uso

1. Ejecuta el script:
    ```bash
    sudo python3 http_spoofer.py
    ```

2. El programa comenzará a interceptar solicitudes HTTP en el puerto 80 y eliminará el encabezado `Accept-Encoding` de las peticiones.

3. Para detener el programa y restablecer las reglas de iptables, usa:
    ```bash
    sudo iptables --flush
    ```

## Explicación del Código

- **set_load(packet, load)**: Modifica la carga (`payload`) de un paquete, recalculando los checksums y la longitud del paquete después de la modificación.

- **process_packet(packet)**: Intercepta paquetes HTTP. Si el paquete es una solicitud al puerto 80 (HTTP), elimina el encabezado `Accept-Encoding` para evitar que el servidor envíe respuestas comprimidas. Si el paquete es una respuesta del servidor, imprime los detalles del paquete en la terminal.

- **queue.run()**: Inicia la captura y procesamiento de los paquetes interceptados por Netfilter.

## Ejemplo de Salida

Cuando el script intercepta una solicitud HTTP, mostrará algo como:

```bash
[+] Solicitud:

[+] Respuesta del servidor:
```
*Muestra detalles del paquete HTTP interceptado.*
