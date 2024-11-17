import smtplib
from email.message import EmailMessage

class EmailService:

    @staticmethod
    def emailMessages(asunto, email, nombre, mensaje, archivo_adjunto=None):
        email_subject = asunto
        sender_email_address = "mibancouq@gmail.com"
        receiver_email_address = email
        email_smtp = "smtp.gmail.com"
        email_password = "jzwchomqjgaqiqir"

        # Crear el objeto de mensaje de correo
        message = EmailMessage()

        # Leer y personalizar el contenido del archivo HTML
        with open('config/message.html', 'r') as file:
            file_content = file.read()
            file_content = file_content.format(nombre=nombre, mensaje=mensaje)

        # Configurar los encabezados del correo
        message['Subject'] = email_subject
        message['From'] = sender_email_address
        message['To'] = receiver_email_address

        # Establecer el contenido del correo en formato HTML
        message.set_content(file_content, subtype='html')

        # Agregar archivo adjunto si se proporciona
        if archivo_adjunto:
            try:
                with open(archivo_adjunto, 'rb') as f:
                    file_data = f.read()
                    file_name = archivo_adjunto.split('/')[-1]  # Extraer solo el nombre del archivo

                message.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)
            except Exception as e:
                print(f"Error al adjuntar archivo: {e}")

        # Configurar el servidor SMTP y puerto
        server = smtplib.SMTP(email_smtp, 587)

        # Identificar al cliente ante el servidor SMTP
        server.ehlo()

        # Asegurar la conexión SMTP
        server.starttls()

        # Iniciar sesión en la cuenta de correo
        server.login(sender_email_address, email_password)

        # Enviar el mensaje
        server.send_message(message)

        # Cerrar la conexión con el servidor
        server.quit()
