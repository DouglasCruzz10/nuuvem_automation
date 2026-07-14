from playwright.sync_api import sync_playwright
from app.selecao_produtos import selecionar_produtos
from app.filtro_dados import filtrar_dados
from app.acessar_nuuvem import abrir_nuuvem
from app.enviar_email import enviar_email, modelo_email

def main():
    """
    Função principal que executa o fluxo de automação:
        1. Abre o navegador e acessa o site da Nuuvem.
        2. Seleciona os produtos disponíveis.
        3. Filtra os dados dos produtos.
        4. Gera o modelo de email com os produtos filtrados.
        5. Envia o email com a lista de produtos em promoção.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        pagina = browser.new_page()
        abrir_nuuvem(pagina=pagina)
        produtos = selecionar_produtos(pagina)
        dados_filtrados = filtrar_dados(produtos)
        linhas_html = modelo_email(produtos, dados_filtrados)
        enviar_email(linhas=linhas_html)
main()
   

    
