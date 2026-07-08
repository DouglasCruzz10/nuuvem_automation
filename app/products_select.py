import json

def selecionar_produtos(page):
    produtos = []
    cards = page.query_selector_all("a[data-default-tracker-product-id-param]")

    for card in cards:
        raw_tracking = card.get_attribute("data-default-tracker-product-tracking-data-param")
        if not raw_tracking:
            continue
        info = json.loads(raw_tracking)
        preco_elemento = card.query_selector(".product-price[data-price]")
        preco_promo = None
        desconto = None
        expira_em = None
        if preco_elemento:
            raw_preco = preco_elemento.get_attribute("data-price")
            preco_data = json.loads(raw_preco)
            preco_promo = preco_data["v"] / 100
            expira_em = preco_data.get("e")
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

    return produtos