def abrir_nuuvem(pagina):
    pagina.goto("https://www.nuuvem.com/br-pt")
    pagina.get_by_title("Menu").click()
    pagina.get_by_role("link", name=" PC ").click()
    pagina.get_by_role("link", name="Ofertas", exact=True).click()
    pagina.wait_for_selector("a[data-default-tracker-product-id-param]")