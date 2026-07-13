from email.mime.text import MIMEText   
from email.mime.multipart import MIMEMultipart
from utils.logger import info_log, error
from dotenv import load_dotenv
import smtplib
import os


def enviar_email(linhas):
    try:
        load_dotenv('credentials.env')
        EMAIL_USUARIO = os.getenv('EMAIL')
        SENHA_USUARIO = os.getenv('SENHA')
        ASSUNTO_EMAIL = "Lista de Produtos em Promoção"
        DESTINATARIO_EMAIL = ""

        msg = MIMEMultipart("alternative")
        msg["Subject"] = ASSUNTO_EMAIL
        msg["From"] = EMAIL_USUARIO
        msg["To"] = DESTINATARIO_EMAIL
        msg.attach(MIMEText(linhas, "html"))
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor_email:
            servidor_email.starttls()
            servidor_email.login(EMAIL_USUARIO, SENHA_USUARIO)
            servidor_email.send_message(msg)
            servidor_email.quit()
        info_log(f"✅ Email enviado com sucesso para {DESTINATARIO_EMAIL}")

    except smtplib.SMTPAuthenticationError as e:
        error(f"❌ Erro de autenticação ao enviar o email: {e}", e)
    except smtplib.SMTPRecipientsRefused as e:
        error(f"❌ Erro: destinatário recusado ou inválido ao enviar o email: {e}", e)
    except smtplib.SMTPException as e:
        error(f"❌ Erro geral no SMTP: {e}", e)
    except Exception as e:
        error(f"❌ Erro ao enviar o email: {e}", e)