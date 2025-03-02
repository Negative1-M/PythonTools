# Keylogger

**Keylogger** es una herramienta en Python que captura las teclas presionadas por el usuario y envía informes periódicos de la actividad registrada a un correo electrónico especificado. Utiliza la biblioteca `pynput` para monitorear la actividad del teclado y `smtplib` para enviar los informes vía email.

## Requisitos

- Python 3.x
- Biblioteca `pynput` (puede instalarse con `pip install pynput`)
- Acceso a una cuenta de correo de Gmail para enviar los reportes (se debe permitir el acceso a aplicaciones menos seguras o generar una contraseña de aplicación).

## Instalación

1. Clona o descarga este repositorio.
2. Instala las dependencias necesarias:
    ```bash
    pip install pynput
    ```

3. Modifica las credenciales del correo electrónico en la función `send_email` con tu correo, destinatarios y contraseña de aplicación:
    ```python
    self.send_email("Keylogger Report", email_body, "tu_correo@gmail.com", ["destinatario@gmail.com"], "tu_contraseña_de_aplicación")
    ```

## Uso

1. Inicia el programa ejecutando el script:
    ```bash
    python3 Keylogger.py
    ```

2. El keylogger comenzará a registrar las teclas presionadas y enviará informes cada 30 segundos al correo configurado.

3. Para detener la ejecución del keylogger, puedes finalizar el proceso manualmente en la terminal.

## Explicación del Código

- **pressed_key(key)**: Esta función registra cada tecla presionada y las almacena en `self.log`. Detecta tanto caracteres normales como teclas especiales (enter, espacio, backspace, etc.).
  
- **send_email(subject, body, sender, recipients, password)**: Envía el registro de teclas recopilado como cuerpo del correo electrónico. Utiliza `smtplib` y un servidor SMTP de Gmail para enviar el correo.

- **report()**: Esta función es invocada periódicamente (cada 30 segundos) para enviar los registros capturados y limpiar el registro de teclas.

- **start()**: Inicia el keylogger y la escucha de teclas presionadas.

- **shutdown()**: Detiene el keylogger cancelando el temporizador y evitando el envío de más informes.

## Notas

- Este keylogger envía los datos de las teclas presionadas a un correo electrónico. Para usarlo, debes configurar tu cuenta de Gmail para permitir aplicaciones menos seguras o generar una contraseña de aplicación.
- **Uso Responsable**: Este software debe utilizarse únicamente en sistemas en los que tienes autorización para realizar monitoreo de teclas.

## Advertencia Legal

El uso no autorizado de esta herramienta en sistemas ajenos es ilegal. Asegúrate de utilizarla únicamente con fines educativos y en sistemas donde tienes permiso para realizar estas actividades.
