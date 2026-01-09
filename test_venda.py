from playwright.sync_api import sync_playwright
import os

def test_login_sucesso():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        caminho = "file://" + os.path.abspath("index.html")
        page.goto(caminho)
        page.fill("#user", "admin")
        page.fill("#pass", "123")
        page.click("#btn-login")
        print("✅ Fluxo de login testado com sucesso!")
        browser.close()