#callbacks.py
import sqlite3
import pandas as pd
from dash.dependencies import Input, Output, State
from dash import callback_context, html
from datetime import datetime

def register_callbacks(app):
    # Callback para atualizar a tabela com os filtros aplicados
    @app.callback(
        [
            Output('data-table', 'data'),
            Output('data-table', 'columns'),
            Output('dropdown-filter', 'value'),
            Output('input-filter-empresa', 'value'),
            Output('input-filter-palavra-chave', 'value'),
            Output('input-filter-pasta', 'value'),
            Output('input-filter-titulo', 'value'),
            Output('input-filter-cnpj', 'value'),
            Output('input-filter-data-documento', 'date'),
        ],
        [
            Input('search-button', 'n_clicks'),
            Input('clear-button', 'n_clicks')
        ],
        [
            State('dropdown-filter', 'value'),
            State('input-filter-empresa', 'value'),
            State('input-filter-palavra-chave', 'value'),
            State('input-filter-pasta', 'value'),
            State('input-filter-titulo', 'value'),
            State('input-filter-cnpj', 'value'),
            State('input-filter-data-documento', 'date'),
        ]
    )
    def update_table(search_clicks, clear_clicks, selected_area, input_empresa, input_palavra_chave, input_pasta, input_titulo, input_cnpj, input_data_documento):
        ctx = callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else ''

        if trigger_id == 'search-button' and search_clicks:
            conn = sqlite3.connect('arquivo.db')
            query = "SELECT * FROM docjur_csv WHERE 1=1"
            params = []
            
            # Filtros
            if selected_area:
                query += f" AND Area = '{selected_area}'"
            if input_empresa:
                query += f" AND Empresa LIKE '%{input_empresa}%'"
            if input_palavra_chave:
                palavras_chave = [p.strip() for p in input_palavra_chave.split(';')]
                for palavra in palavras_chave:
                    query += " AND \"Palavras Chave\" LIKE ?"
                    params.append(f"%{palavra}%")
            if input_titulo:
                query += f" AND Titulo LIKE '%{input_titulo}%'"
            if input_pasta:
                query += f" AND Pasta LIKE '%{input_pasta}%'"
            if input_cnpj:
                query += f" AND CNPJ LIKE '%{input_cnpj}%'"

            # Filtro por data do documento
            if input_data_documento:
                try:
                    input_data_documento_db = datetime.strptime(input_data_documento, "%Y-%m-%d").strftime("%d/%m/%Y")
                    query += f' AND TRIM("Data do Documento") = "{input_data_documento_db}"'
                except ValueError as e:
                    print(f"Erro ao converter a data do documento: {e}")

            # Executa a consulta
            df = pd.read_sql_query(query, conn, params=params)
            conn.close()
            
            colunas_exibidas = ["Area", "Palavras Chave", "Pasta", "Empresa", "Titulo", "CNPJ", "Data do Documento", "Link"]
            if not all(col in df.columns for col in colunas_exibidas):
                raise ValueError(f"Uma ou mais colunas necessárias não estão presentes no banco de dados: {colunas_exibidas}")
            df_exibicao = df[colunas_exibidas]
            
            # Garantir que a coluna Data do Documento seja string
            if "Data do Documento" in df.columns:
                df["Data do Documento"] = df["Data do Documento"].astype(str)

            # Converte a coluna Link para HTML com imagem clicável
            if "Link" in df.columns:
                df["Link"] = df["Link"].apply(
                    lambda url: f"[![PDF](/assets/pdflogo.png)]({url})"
                )

            # Define as colunas da tabela
            columns = [
                {'name': 'Área', 'id': 'Area'},
                {'name': 'Empresa', 'id': 'Empresa'},
                {'name': 'CNPJ', 'id': 'CNPJ'},
                {'name': 'Pasta', 'id': 'Pasta'},
                {'name': 'Título', 'id': 'Titulo'},
                {'name': 'Data do Documento', 'id': 'Data do Documento'},
                {'name': 'Link', 'id': 'Link', 'presentation': 'markdown'}
            ]

            data = df.to_dict('records')

            return data, columns, selected_area, input_empresa, input_palavra_chave, input_pasta, input_titulo, input_cnpj, input_data_documento 

        elif trigger_id == 'clear-button' and clear_clicks:
            # Limpar filtros e tabela
            return [], [], None, '', '', '', None, None, None

        # Se nenhum botão foi acionado, retorna valores padrão
        return [], [], selected_area, input_empresa, input_palavra_chave, input_pasta, input_titulo, input_cnpj, input_data_documento

    # Callback para abrir o Painel de Detalhes ao clicar em uma linha
    @app.callback(
        Output("detail-panel", "is_open"),
        Output("detail-content", "children"),
        Input("data-table", "active_cell"),
        Input("close-detail-panel", "n_clicks"),
        State("data-table", "data"),
        prevent_initial_call=True
    )
    def toggle_detail_panel(active_cell, close_clicks, rows):
        ctx = callback_context
        if not ctx.triggered:
            return False, []

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

        # Fechar o painel
        if trigger_id == "close-detail-panel":
            return False, []

        # Abrir o painel ao clicar na linha
        if active_cell and rows:
            row_index = active_cell.get('row')
            if row_index is not None and row_index < len(rows):
                selected_row = rows[row_index]

                # Detalhes formatados para o painel
                details = [
                    html.P(f"{col}: {selected_row.get(col, '')}") for col in [
                        "Area", "Empresa", "Pasta", "Titulo", "Data do Documento",
                        "Data de Indexacao", "Anexo", "Classe do documento",
                        "Palavras Chave", "Idioma", "Aplicacao", "Localizacao Fisica",
                        "Data de Expurgo", "Versao", "Status", "AutoNum", "Usuario",
                        "Emprestado para", "CNPJ", "Data de emprestimo"
                    ]
                ]

                return True, details

        return False, []
