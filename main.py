from playwright.sync_api import sync_playwright
from app.selecao_produtos import selecionar_produtos
from app.acessar_nuuvem import abrir_nuuvem
from app.enviar_email import enviar_email
from datetime import datetime

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    pagina = browser.new_page()
    abrir_nuuvem(pagina)

    pagina.get_by_role("link", name=" PC ").click()
    pagina.get_by_role("link", name="Ofertas", exact=True).click()
    pagina.wait_for_selector("a[data-default-tracker-product-id-param]")
    
    produtos = selecionar_produtos(pagina)

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

    enviar_email(linhas=linhas)


   

    
