import json
from utils.logger import info_log, error


def selecionar_produtos(pagina):
    """
    Função para selecionar os produtos disponíveis na página da Nuuvem.
    Args:   
        pagina: Objeto da página do Playwright.
    Returns:
        produtos: Lista de produtos disponíveis com informações relevantes.
    """
    # Inicializa a lista de Produtos
    produtos = []

    try:
        cards = pagina.query_selector_all("a[data-default-tracker-product-id-param]")


        for card in cards:
            try:
                raw_tracking = card.get_attribute("data-default-tracker-product-tracking-data-param")
                if not raw_tracking:
                    continue
                info = json.loads(raw_tracking)
                preco_elemento = card.query_selector(".product-price[data-price]")
                preco_promo = None
                desconto = None
                expira_em = None

                if preco_elemento:
                    try:
                        raw_preco = preco_elemento.get_attribute("data-price")
                        preco_data = json.loads(raw_preco)
                        preco_promo = preco_data["v"] / 100
                        expira_em = preco_data.get("e")
                    except (json.JSONDecodeError, KeyError) as e:
                        error(f"Erro ao processar o preço do produto {info.get('name')}: {e}", exc=e)
                discount_el = card.query_selector(".product-price--discount")
                if discount_el:
                    desconto = discount_el.inner_text().strip()
                produtos.append({
                    "nome": info.get("name"),
                    "marca": info.get("brand"),
                    "genero": info.get("genre"),
                    "preco_original": info.get("price"),
                    "preco_promocional": preco_promo,
                    "desconto": desconto,
                    "moeda": info.get("currency"),
                    "url": info.get("url"),
                    "imagem": info.get("image_url"),
                    "expira_em": expira_em,
                })
            except json.JSONDecodeError as e:
                error(f"Erro ao decodificar JSON para o produto: {e}", exc=e)
            except AttributeError as e:
                error(f"Erro ao acessar atributos do produto: {e}", exc=e)  
    except Exception as e:
        error(f"Erro ao selecionar produtos: {e}", exc=e)
    
    info_log(f" ✅ fluxo /Seleção de Produtos/ executado com sucesso. Total de produtos coletados: {len(produtos)}")
    return produtos