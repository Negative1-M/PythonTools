# ARPspoofer

**ARPspoofer** es una herramienta de red escrita en Python que realiza un ataque de suplantación ARP (ARP Spoofing). Este ataque permite redirigir el tráfico de red entre un objetivo y un router, haciéndose pasar por ambas partes.

## Requisitos

- Python 3.x
- Biblioteca `scapy` (instalable con `pip install scapy`)

## Instalación

1. Clona o descarga este repositorio.
2. Instala las dependencias ejecutando:
    ```bash
    pip install scapy
    ```

## Uso

1. Ejecuta el programa con permisos de administrador.
2. Proporciona el parámetro `-t` o `--target` seguido de la IP objetivo:
    ```bash
    sudo python3 ARPspoofer.py -t 192.168.1.10
    ```

   - `-t` o `--target`: IP del host objetivo que deseas suplantar.

3. El programa simula ser el router para el objetivo, y ser el objetivo para el router.

## Explicación del Código

- **get_arguments()**: Recibe la IP del objetivo a través de la línea de comandos.
- **spoof(ip_address, spoof_ip)**: Envía un paquete ARP suplantado con `psrc` (IP del supuesto origen) y `pdst` (IP destino).
- **main()**: Ejecuta la suplantación continuamente, actualizando la tabla ARP del objetivo y del router cada 2 segundos.

## Notas Importantes

- **ARP Spoofing** es una técnica que redirige el tráfico de red entre un objetivo y un router, lo que puede ser utilizado en ataques Man-in-the-Middle (MitM).
- Ejecutar este programa sin autorización en una red es ilegal y puede tener graves consecuencias legales.
