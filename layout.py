#layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
from dash import dash_table

def create_layout():
    return html.Div([
        # Cabeçalho com título e logo
        html.Div([
            html.H1("Docjur", style={
                'textAlign': 'left',
                'color': '#345F6C',
                'margin': '0',
                'display': 'inline-block',
                'verticalAlign': 'middle',
                'fontSize': '48px',
                'fontWeight': 'bold'
            }),
            html.Img(
                src='/assets/logoOR.png',
                style={
                    'height': '60px',
                    'margin-left': 'auto',
                    'display': 'inline-block',
                    'verticalAlign': 'middle'
                }
            )
        ], style={
            'display': 'flex',
            'align-items': 'center',
            'justify-content': 'space-between',
            'width': '100%'
        }),

        html.Hr(style={'border-color': '#FFA80B', 'border-width': '2px', 'margin-bottom': '20px'}),

        # Seção de filtros dentro de um Card
        dbc.Container(
            dbc.Card(
                dbc.CardBody([
                    # Primeira linha: Área (dropdown) e Palavras Chave (input)
                    dbc.Row([
                        dbc.Col([
                            dbc.Label([
                                DashIconify(icon="bx:area", width=18),
                                html.Span(" Área", style={'margin-left': '5px'})
                            ], style={'color': 'white'}),
                            dcc.Dropdown(
                                id='dropdown-filter',
                                options=[
                                    {'label': 'E119506', 'value': 'E119506'},
                                    {'label': 'FINANCEIRO', 'value': 'FINANCEIRO'},
                                    {'label': 'FINANCEIRO IMOBILIARIO', 'value': 'FINANCEIRO IMOBILIARIO'},
                                    {'label': 'MARCAS E PATENTES', 'value': 'MARCAS E PATENTES'},
                                    {'label': 'NEGOCIAL', 'value': 'NEGOCIAL'},
                                    {'label': 'SOCIETARIO', 'value': 'SOCIETARIO'}
                                ],
                                placeholder="Selecione uma área (opcional)"
                            ),
                        ], md=6),
                        dbc.Col([
                            dbc.Label([
                                DashIconify(icon="bx:hash", width=20),
                                html.Span(" Palavras Chave", style={'margin-left': '5px'})
                            ], style={'color': 'white'}),
                            dbc.Input(
                                id='input-filter-palavra-chave',
                                type='text',
                                placeholder='Pesquisar por palavra chave',
                                className="mb-3"
                            ),
                        ], md=6),
                    ], className="mb-4"),

                    # Segunda linha: Empresa (input) e Título (input)
                    dbc.Row([
                        dbc.Col([
                            dbc.Label([
                                DashIconify(icon="bx:building", width=20),
                                html.Span(" Empresa", style={'margin-left': '5px'})
                            ], style={'color': 'white'}),
                            dbc.Input(
                                id='input-filter-empresa',
                                type='text',
                                placeholder='Pesquisar por empresa',
                                className="mb-3"
                            ),
                        ], md=6),
                        dbc.Col([
                            dbc.Label([
                                DashIconify(icon="bx:file", width=20),
                                html.Span(" Título", style={'margin-left': '5px'})
                            ], style={'color': 'white'}),
                            dbc.Input(
                                id='input-filter-titulo',
                                type='text',
                                placeholder='Pesquisar por título',
                                className="mb-3"
                            ),
                        ], md=6),
                    ], className="mb-4"),
                    
                    # Terceira linha: Pasta (input) e CNPJ (input)
                    dbc.Row([
                        dbc.Col([
                            dbc.Label([
                                DashIconify(icon="bx:folder", width=20),
                                html.Span(" Pasta", style={'margin-left': '5px'})
                            ], style={'color': 'white'}),  
                            dbc.Input(
                                id='input-filter-pasta',
                                type='text',
                                placeholder='Pesquisar por pasta',
                                className="mb-3"
                            ),
                        ], md=6),
                        dbc.Col([
                            dbc.Label([
                                DashIconify(icon="mdi:file-document", width=20),
                                html.Span(" CNPJ", style={'margin-left': '5px'})
                            ], style={'color': 'white'}),  
                            dbc.Input(
                                id='input-filter-cnpj',
                                type='text',
                                placeholder='Pesquisar por CNPJ',
                                className="mb-3"
                            ),
                        ], md=6),
                    ], className="mb-4"),
                    
                    # Quarta linha: Data do Documento
                    dbc.Row([
                        dbc.Col([
                            dbc.Label([
                                DashIconify(icon="bx:calendar", width=30),
                                html.Span(" Data do Documento", style={'margin-left': '5px'})
                            ], style={'color': 'white'}),
                            html.Div(
                                dcc.DatePickerSingle(
                                    id='input-filter-data-documento',
                                    placeholder='Selecione...',
                                    display_format='DD/MM/YYYY',
                                    className="custom-date-picker mb-3"
                                ),
                                style={'margin-top': '5px'}
                            )
                        ], md=6),
                    ], className="mb-4"),

                    # Linha dos botões
                    dbc.Row([
                        dbc.Col([
                            html.Button(
                                "Pesquisar",
                                id='search-button',
                                n_clicks=0,
                                style={
                                    'background-color': '#FFA80B',
                                    'color': 'white',
                                    'border': 'none',
                                    'padding': '0 20px',
                                    'height': '38px',
                                    'border-radius': '10px',
                                    'cursor': 'pointer',
                                    'transition': 'background-color 0.3s ease-in-out'
                                }
                            ),
                            html.Button(
                                "Limpar Pesquisa",
                                id='clear-button',
                                n_clicks=0,
                                style={
                                    'background-color': '#7F7F7F',
                                    'color': 'white',
                                    'border': 'none',
                                    'padding': '0 20px',
                                    'height': '38px',
                                    'border-radius': '10px',
                                    'cursor': 'pointer',
                                    'transition': 'background-color 0.3s ease-in-out',
                                    'margin-left': '10px'
                                }
                            )
                        ], md=12, style={'text-align': 'right'})
                    ])
                ]),
                # Card com fundo #345F6C e texto branco
                style={
                    'border-radius': '10px',
                    'padding': '20px',
                    'background-color': '#345F6C',
                    'color': 'white'
                }
            ),
            fluid=True,
            style={'margin-bottom': '20px'}
        ),

        html.Hr(style={'border-color': '#FFA80B', 'border-width': '2px', 'margin-bottom': '20px'}),

        # Tabela de dados com paginação limitada a 30 linhas
        html.Div([
            dcc.Loading(
                children=[
                    dash_table.DataTable(
                        id='data-table',
                        columns=[],  # Inicialmente sem colunas
                        data=[],     # Inicialmente sem dados
                        page_size=30,
                        style_table={'overflowX': 'auto'},
                        style_cell={
                            'color': 'black',
                            'backgroundColor': 'white',
                            'fontsize': '8px',
                            'textAlign': 'center',
                            'border': '1px solid #ccc'
                        },
                        style_header={
                            'backgroundColor': '#345F6C',
                            'fontWeight': 'bold',
                            'border-bottom': '2px solid #007bff',
                            'color': 'white'
                        },
                    )
                ],
                type="circle"
            )
        ], style={'margin-top': '20px'}),

        # Painel de Detalhes (Offcanvas)
        dbc.Offcanvas(
            id="detail-panel",
            is_open=False,
            placement="end",
            children=[
                dbc.Row([
                    dbc.Col(html.H4("Detalhes do Documento", style={'fontWeight': 'bold', 'color': '#345F6C'}), width=10),
                    dbc.Col(html.Button(id="close-detail-panel", style={
                        "background": "none", "border": "none", "fontSize": "24px", "cursor": "pointer", "color": "#345F6C"
                    }), width=2),
                ], style={"margin-bottom": "15px"}),

                html.Hr(),

                html.Div(id="detail-content", style={
                    'padding': '10px 15px',
                    'backgroundColor': '#F9F9F9',
                    'borderRadius': '10px',
                    'boxShadow': '0px 2px 4px rgba(0, 0, 0, 0.1)'
                })
            ],
            style={"width": "450px", "padding": "20px", "backgroundColor": "#FFFFFF", "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.2)", "borderRadius": "10px"}
        )
    ], style={
        'padding': '20px',
        'background-color': 'white',
        'border-radius': '10px',
        'box-shadow': '0 8px 16px rgba(0, 0, 0, 0.6)'
    })
