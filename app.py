# app.py
import dash
import dash_bootstrap_components as dbc
from layout import create_layout
from callbacks import register_callbacks

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://use.fontawesome.com/releases/v5.15.4/css/all.css",
    "/assets/style.css",
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    title="Docjur"  # Nome da aba no navegador
)

# Define o layout da aplicação
app.layout = create_layout()

# Registra todos os callbacks da aplicação
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
