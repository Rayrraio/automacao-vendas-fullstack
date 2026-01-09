# 🚀 Automação de Vendas Fullstack

Projeto de automação de testes End-to-End (E2E) em uma aplicação de Marketplace.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Framework de Teste:** Playwright
- **Relatórios:** Pytest-html
- **Frontend:** HTML5 / JavaScript

## 🧪 Cenários de Teste
1. **Fluxo de Venda Completo:** Valida desde o login até o checkout e screenshot final.
2. **Segurança de Login (Teste Negativo):** Garante que o sistema não permita acesso com credenciais inválidas.

## 📊 Como rodar os testes
1. Instale as dependências: `pip install playwright pytest pytest-html`
2. Instale os navegadores: `playwright install`
3. Execute: `pytest --html=relatorio.html`