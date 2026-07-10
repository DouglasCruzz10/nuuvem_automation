def abrir_nuuvem(pagina):
    pagina.goto("https://www.nuuvem.com/")
    pagina.get_by_role("link", name="Ofertas", exact=True).click()
    pagina.wait_for_selector("a[data-default-tracker-product-id-param]")