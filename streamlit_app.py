import streamlit as st
from datetime import date

# Align everything to the leftmost position on the screen
st.markdown(
    """
    <style>
    .main > div {
        display: flex;
        justify-content: flex-start;
        align-items: flex-start;
    }
    div.stButton > button {
        width: 100%;
        display: inline-block;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Welcome message
st.title("Bem-vindo(a) ao Portal Financeiro")
st.write("Escolha as datas para visualizar as categorias:")

# Date input boxes at the beginning
col1, col2 = st.columns([1, 1])
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
for category in categories:
    button_clicked = st.button(category, key=category)
        
    if button_clicked:
        st.session_state.selected_category = category

# Change button colors using session state
if st.session_state.selected_category:
    selected_button_style = """
    <style>
    div.stButton > button[title="{}"] {{
        background-color: #4CAF50;
        color: white;
        width: 100%;
        display: inline-block;
        text-align: center;
    }}
    </style>
    """.format(st.session_state.selected_category)
    st.markdown(selected_button_style, unsafe_allow_html=True)
