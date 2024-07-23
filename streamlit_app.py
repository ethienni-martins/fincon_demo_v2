import streamlit as st
from datetime import date

# Align everything to the left
st.markdown(
    """
    <style>
    .css-1lcbmhc.e1fqkh3o2 {
        justify-content: flex-start;
    }
    .css-1lcbmhc.e1fqkh3o2 > div {
        flex: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Welcome message
st.title("Bem-vindo(a) ao Portal Financeiro")
st.write("Escolha as datas para visualizar as categorias:")

# Date input boxes at the beginning
col1, col2 = st.columns(2)
with col1:
    data_inicial = st.date_input("Data Inicial", value=date.today())
with col2:
    data_final = st.date_input("Data Final", value=date.today())

# Category options
categories = [
    "Comissão Estorno", 
    "Liberação", 
    "Pagamento Geral", 
    "Pagamento Recebido", 
    "Parcela", 
    "Pix", 
    "Pix Recebido", 
    "Saldo"
]

# State to keep track of the selected category
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None

# Display buttons for each category
for category in ca
