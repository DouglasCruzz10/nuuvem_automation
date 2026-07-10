from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
import smtplib

def enviar_email(linhas):
    import smtplib
    from email.mime.text import MIMEText
    from dotenv import load_dotenv
    import os

    load_dotenv('credentials.env')
    EMAIL_USUARIO = os.getenv('EMAIL')
    SENHA_USUARIO = os.getenv('SENHA')
    CORPO_EMAIL = "Segue abaixo a lista de produtos filtrados:\n\n" +  "\n".join(linhas)
    ASSUNTO_EMAIL = "Lista de Produtos em Promoção"
    DESTINATARIO_EMAIL = ""

    msg = MIMEText(CORPO_EMAIL, "plain", "utf-8")
    msg["Subject"] = ASSUNTO_EMAIL
    msg["From"] = EMAIL_USUARIO
    msg["To"] = DESTINATARIO_EMAIL

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor_email:
        servidor_email.starttls()
        servidor_email.login(EMAIL_USUARIO, SENHA_USUARIO)
        servidor_email.send_message(msg)
        servidor_email.quit()