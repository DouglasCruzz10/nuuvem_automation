from email.mime.text import MIMEText   
from email.mime.multipart import MIMEMultipart
from utils.logger import info_log, error
from dotenv import load_dotenv
import smtplib
import os

def modelo_email(produto, dados_filtrados):
    """
    Função para gerar o modelo de email com a lista de produtos em promoção.
    Args:
        produto: Lista de produtos disponíveis.
        dados_filtrados: Lista de produtos filtrados com informações relevantes.
        Returns:
        linhas_html: String contendo o modelo de email em formato HTML.
    """
    
    linhas_html = """
                <p>Segue abaixo a lista de produtos em promoção:</p>
                <table border="1" cellspacing="0" cellpadding="5">
                    <tr>
                        <th>Nome</th>
                        <th>Preço Original</th>
                        <th>Preço Promocional</th>
                        <th>Gênero</th>
                        <th>Expira em</th>
                    </tr>
                """
    for produto in dados_filtrados:
            linhas_html += f"""
            <tr>
                <td>{produto['nome']}</td>
                <td>{produto['preco_original']}</td>
                <td>{produto['preco_promocional']}</td>
                <td>{produto['genero']}</td>
                <td>{produto['expira_em']}</td>
            </tr>
            """
    linhas_html += "</table>"

    return linhas_html


def enviar_email(linhas):

    """
    Função para enviar o email com a lista de produtos em promoção.
    Args:
        linhas: String contendo o modelo de email em formato HTML.
    Raises:
        smtplib.SMTPAuthenticationError: Se houver erro de autenticação ao enviar o email.
        smtplib.SMTPRecipientsRefused: Se o destinatário for recusado ou inválido.
        smtplib.SMTPException: Para outros erros gerais no SMTP.
    """
    try:
        load_dotenv('credentials.env')
        EMAIL_USUARIO = os.getenv('EMAIL')
        SENHA_USUARIO = os.getenv('SENHA')
        ASSUNTO_EMAIL = "Lista de Produtos em Promoção"
        DESTINATARIO_EMAIL = os.getenv('DESTINATARIO')

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