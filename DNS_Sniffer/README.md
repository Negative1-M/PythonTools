# DNS Packet Sniffer

**DNS Packet Sniffer** es una herramienta escrita en Python que captura y analiza paquetes DNS en una interfaz de red especificada. Filtra y muestra los dominios solicitados que no contienen palabras clave excluidas como "google", "bing", "yahoo", etc.

## Requisitos

- Python 3.x
- Biblioteca `scapy` (puede instalarse con `pip install scapy`)
- Biblioteca `termcolor` (puede instalarse con `pip install termcolor`)

## Uso

1. Asegúrate de ejecutar el programa con permisos de administrador para poder capturar tráfico de red.
2. Inicia el programa en la interfaz de red deseada, por ejemplo, `eth0`:
    ```bash
    sudo python3 DNSsniffer.py
    ```

3. El programa comenzará a capturar y analizar paquetes DNS que pasen por la interfaz de red especificada.

## Explicación del Código

1. **Manejo de señales (Ctrl+C)**: El programa captura la señal `SIGINT` (Ctrl+C) para detener la ejecución de forma segura con un mensaje de salida.

2. **process_dns_packet()**: Esta función procesa cada paquete capturado. Si contiene una solicitud DNS (DNSQR), extrae el dominio. Se excluyen los dominios que contienen ciertas palabras clave, y se muestra cualquier dominio nuevo que no haya sido visto antes.

3. **sniff(interface)**: Utiliza `scapy.sniff()` para capturar paquetes filtrados de DNS (UDP en el puerto 53) en la interfaz de red especificada.

4. **main()**: La función principal que inicia el proceso de captura en la interfaz de red `eth0`.

## Notas

- El programa captura y procesa solo paquetes DNS en la interfaz `eth0`. Si estás utilizando una interfaz de red diferente, reemplaza `eth0` con el nombre de la interfaz deseada.
- Es necesario ejecutarlo con permisos de superusuario, ya que el análisis de paquetes requiere acceso elevado.
- Los dominios que contienen palabras clave comunes como "google" o "bing" son excluidos por el programa.

## Advertencia

Capturar tráfico de red sin autorización es ilegal y puede tener graves consecuencias legales. Asegúrate de tener los permisos necesarios para realizar este tipo de actividades en tu red.
