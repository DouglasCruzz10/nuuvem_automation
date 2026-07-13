from datetime import datetime

def filtrar_dados(produtos):
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
        if jogo['expira_em']:
            dt = datetime.fromisoformat(jogo['expira_em'].replace("Z", "+00:00"))
        else:
            dt = None 
    return dados_filtrados