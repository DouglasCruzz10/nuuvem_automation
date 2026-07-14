from utils.logger import info_log, error
from playwright.sync_api import TimeoutError, Error

def abrir_nuuvem(pagina):
    """
    Função para abrir o site da Nuuvem e navegar até a seção de ofertas.
    Args:
        pagina: Objeto da página do Playwright.
    Raises:
        TimeoutError: Se a página demorar muito para carregar.
        Error: Se houver algum erro ao abrir a página da Nuuvem.
    """
    try:
        pagina.goto("https://www.nuuvem.com/br-pt")
        pagina.get_by_title("Menu").click()
        pagina.get_by_role("link", name=" PC ").click()
        pagina.get_by_role("link", name="Ofertas", exact=True).click()
        pagina.wait_for_selector("a[data-default-tracker-product-id-param]")
        info_log("✅ fluxo /Acesso Nuuvem/ executado com sucesso.")
    except TimeoutError as e:
        error("⏳TimeoutError: A página demorou muito para carregar.", exc=e)
    except Error as e:
        error("❌Erro ao abrir a página da Nuuvem.", exc=e)
    