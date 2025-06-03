# Docjur - Aplicação de Gestão Documental

## Descrição
Docjur é uma aplicação web desenvolvida em Python com o framework Dash. Ela permite filtrar, visualizar e gerenciar documentos com base em informações como CNPJ, área, títulos e datas.

## Tecnologias Utilizadas
- **Python** 3.10
- **Dash** e **Dash Bootstrap Components**
- **SQLite** para banco de dados
- **Pandas** para manipulação de dados
- **Git** e **GitHub** para versionamento

## Requisitos
- Python instalado: [Instalar Python](https://www.python.org/)
- Ambiente virtual configurado.

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/docjur.git
   cd docjur

## Ambiente Virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

## Dependências
pip install -r requirements.txt

## Estrutura do Projeto
docjur/
│-- app.py           # Arquivo principal para executar a aplicação
│-- layout.py        # Layout da interface com Dash
│-- callbacks.py     # Callbacks para a lógica interativa
│-- arquivo.db       # Banco de dados SQLite
│-- assets/          # Arquivos CSS e imagens
│   ├── pdflogo.png  # Ícone do PDF
│   ├── logoOR.png   # Ícone da empresa
│   ├── custom.css   # Estilização personalizada
│-- README.md        # Documentação inicial
