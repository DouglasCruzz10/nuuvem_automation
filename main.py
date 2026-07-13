from playwright.sync_api import sync_playwright
from app.selecao_produtos import selecionar_produtos
from app.filtro_dados import filtrar_dados
from app.acessar_nuuvem import abrir_nuuvem
from app.enviar_email import enviar_email

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        pagina = browser.new_page()
        abrir_nuuvem(pagina=pagina)

        produtos = selecionar_produtos(pagina)
        dados_filtrados = filtrar_dados(produtos)

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
        enviar_email(linhas=linhas_html)

main()
   

    
