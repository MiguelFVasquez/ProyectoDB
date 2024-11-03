import smtplib 
from email.message import EmailMessage 

class EmailService:

    @staticmethod
    def emailMessages(asunto,email, nombre, mensaje):
        email_subject = asunto
        sender_email_address = "mibancouq@gmail.com" 
        receiver_email_address = email
        email_smtp = "smtp.gmail.com" 
        email_password = "jzwchomqjgaqiqir" 

        # Create an email message object 
        message = EmailMessage() 

        # Read and customize HTML file content
        with open('config/message.html', 'r') as file:
            file_content = file.read()
            file_content = file_content.format(nombre=nombre, mensaje=mensaje)

        # Configure email headers 
        message['Subject'] = email_subject 
        message['From'] = sender_email_address 
        message['To'] = receiver_email_address 

        # Set email body text 
        message.set_content(file_content, subtype='html') 

        # Set smtp server and port 
        server = smtplib.SMTP(email_smtp, 587) 

        # Identify this client to the SMTP server 
        server.ehlo() 

        # Secure the SMTP connection 
        server.starttls() 

        # Login to email account 
        server.login(sender_email_address, email_password) 

        # Send email 
        server.send_message(message) 

        # Close connection to server 
        server.quit()

