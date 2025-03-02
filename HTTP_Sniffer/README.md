# HTTP Sniffer

**HTTP Sniffer** es una herramienta en Python que monitorea el tráfico HTTP en una red, buscando URLs visitadas y posibles credenciales sensibles enviadas en las peticiones. Utiliza la biblioteca `scapy` para interceptar paquetes y analizar sus contenidos.

## Requisitos

- Python 3.x
- Biblioteca `scapy` (puede instalarse con `pip install scapy`)
- Biblioteca `termcolor` (opcional, para salida de texto en color: `pip install termcolor`)

## Uso

1. Inicia el programa ejecutando el script:
    ```bash
    sudo python3 Http_sniffer.py
    ```

    **Nota**: El programa requiere privilegios de superusuario para capturar tráfico en la red.

2. El sniffer comenzará a capturar el tráfico HTTP en la interfaz de red especificada (por defecto, `eth0`). 

3. Si detecta peticiones HTTP con palabras clave relacionadas con credenciales, como "login", "user", "pass", o "mail", mostrará posibles credenciales en la terminal.

4. Para detener el programa, presiona `Ctrl + C`.

## Explicación del Código

- **def_handler(sig, frame)**: Manejador de señal que captura `Ctrl + C` para salir del programa limpiamente.
  
- **process_packet(packet)**: Procesa cada paquete capturado. Si el paquete contiene una solicitud HTTP, extrae la URL visitada y busca datos sensibles en el contenido de la solicitud. Si detecta palabras clave como "login" o "pass", intenta imprimir posibles credenciales.

- **sniff(interface)**: Comienza a capturar tráfico en la interfaz de red especificada, pasando cada paquete a `process_packet`.

## Ejemplo de Salida

Cuando el programa detecta una URL visitada, imprimirá algo como:

```bash
[+] URL visitada por la víctima: http://example.com/login
