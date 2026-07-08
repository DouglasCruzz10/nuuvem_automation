from playwright.sync_api import sync_playwright
from app.products_select import selecionar_produtos
from email.mime.text import MIMEText
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os

with sync_playwright() as p:
    load_dotenv('credentials.env')
    USER_MAIL = os.getenv('EMAIL')
    USER_PASSWORD = os.getenv('SENHA')
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.nuuvem.com/br-pt")
    page.get_by_title("Menu").click()
    page.get_by_role("link", name=" PC ").click()
    page.get_by_role("link", name="Ofertas", exact=True).click()

    page.wait_for_selector("a[data-default-tracker-product-id-param]")
    produtos = selecionar_produtos(page)

    for prod in produtos:
        print(f"{prod['nome']} - R${prod['preco_promocional']} ({prod['desconto']}) até {prod['expira_em']}")

    dados_filtrados = [
    {
        'nome': jogo['nome'],
        'preco_original': jogo['preco_original'],
        'preco_promocional': jogo['preco_promocional'],
        'genero': jogo['genero'],
        'expira_em': jogo['expira_em']
    }
    for jogo in produtos
    ]
    for jogo in dados_filtrados:
        dt = datetime.fromisoformat(jogo['expira_em'].replace("Z", "+00:00"))
        jogo['expira_em'] = dt.strftime('%d/%m/%Y %H:%M')

    linhas = []
    for produto in dados_filtrados:
        linha = (
            f"Nome: {produto['nome']}\n"
            f"Preço Original: {produto['preco_original']}\n"
            f"Preço Promocional: {produto['preco_promocional']}\n"
            f"Gênero: {produto['genero']}\n"
            f"Expira em: {produto['expira_em']}\n"
        )
        linhas.append(linha)  

    corpo_email = "Segue abaixo a lista de produtos filtrados:\n\n" +  "\n".join(linhas)
    msg = MIMEText(corpo_email, "plain", "utf-8")
    msg["Subject"] = "Jogos em Promoção - NUUVEM"
    msg["From"] = USER_MAIL
    msg["To"] = ""


    with smtplib.SMTP("smtp.gmail.com", 587) as servidor_email:
        servidor_email.starttls()
        servidor_email.login(USER_MAIL, USER_PASSWORD)
        servidor_email.send_message(msg)
        servidor_email.quit()
   

    
