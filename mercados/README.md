
# Web Scraping - Preços de Produtos em Mercados

## Descrição
Este projeto visa coletar e armazenar os preços de diversos produtos em diferentes mercados da minha região. O objetivo é construir uma API que permita aos usuários consultar os preços de produtos específicos e realizar análises de preços, como identificar o dia mais barato para determinado produto ou prever os preços para os próximos meses.

## Funcionalidades
- **Coleta de preços**: O sistema irá coletar e armazenar diariamente os preços dos produtos dos mercados selecionados.
- **Consulta de preços**: A API permitirá que os usuários consultem os preços de produtos em diferentes mercados.
- **Análise de preços**:
  - Comparação dos preços de produtos entre diferentes mercados.
  - Identificação do dia mais barato para um produto.
  - Previsões de preços de produtos para os próximos meses.


## Requisitos
- Python 3.x
- Bibliotecas:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `flask` (para a API)
  - `sklearn` (para análise de dados)
  - `matplotlib` (para gráficos)

## Como Rodar o Projeto

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/lfqcamargo/web_scraping.git
   cd web_scraping
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows use .venv\Scriptsctivate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Coleta de Dados
O script de coleta de preços irá acessar os sites dos mercados e armazenar os preços dos produtos em um banco de dados ou arquivo.

### API
A API foi desenvolvida com o framework Flask e permite consultar os preços de produtos. Para rodá-la, execute o seguinte comando:
```bash
python api/app.py
```

A API estará disponível em `http://localhost:5000`.

### Análise de Preços
Para realizar análises de preços, como a identificação do dia mais barato ou previsões de preços, utilize os scripts na pasta `analises/`.

## Exemplo de Uso
1. **Consulta de Preços**:
   - Endpoint: `GET /precos?produto=frango`
   - Resposta: Lista de preços do produto `frango` nos diferentes mercados.

2. **Análise de Preços**:
   - O script de análise pode ser executado para gerar gráficos sobre a variação dos preços ao longo do tempo ou fazer previsões.
