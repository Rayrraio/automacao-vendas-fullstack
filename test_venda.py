from playwright.sync_api import sync_playwright
import os

def test_fluxo_venda_completo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        caminho = "file://" + os.path.abspath("index.html")
        page.goto(caminho)

        # 1. Login
        page.fill("#user", "admin")
        page.fill("#pass", "123")
        page.click("#btn-login")

        # 2. Adicionar ao Carrinho
        page.click("#add-item")

        # 3. Checkout (Preencher dados e finalizar)
        page.fill("#cartao", "4444 5555 6666 7777")
        page.fill("#nome", "RAYANE ROCHA")
        
        # Lida com o alerta de sucesso
        page.on("dialog", lambda d: d.accept())
        page.click("#btn-finalizar")
        page.screenshot(path="resultado_venda.png")
        print("✅ Teste de ponta a ponta concluído com sucesso!")
        browser.close()