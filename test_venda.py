from playwright.sync_api import sync_playwright
import os

# TESTE 1: Sucesso (Login e Compra)
def test_fluxo_venda_completo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        caminho = "file://" + os.path.abspath("index.html")
        page.goto(caminho)

        page.fill("#user", "admin")
        page.fill("#pass", "123")
        page.click("#btn-login")
        page.click("#add-item")
        page.fill("#cartao", "4444 5555 6666 7777")
        page.fill("#nome", "RAYANE ROCHA")
        page.on("dialog", lambda d: d.accept())
        page.click("#btn-finalizar")
        page.screenshot(path="resultado_venda.png")
        browser.close()

# TESTE 2: Caminho Infeliz (Senha Errada)
def test_login_senha_incorreta():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        caminho = "file://" + os.path.abspath("index.html")
        page.goto(caminho)

        page.fill("#user", "admin")
        page.fill("#pass", "SENHA_ERRADA")
        page.click("#btn-login")

        # Verifica se a loja continuou escondida
        is_hidden = page.locator("#vitrine").is_hidden()
        assert is_hidden
        print("✅ Sucesso: O sistema bloqueou o acesso com senha errada!")
        browser.close()