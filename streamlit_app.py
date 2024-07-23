import streamlit as st
from datetime import date

# Welcome message
st.title("Bem-vindo(a) ao Portal Financeiro")
st.write("Selecione a categoria para visualizar os gráficos e informações:")

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

# Display buttons for each category with date inputs
for category in categories:
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        button_clicked = st.button(category, key=category)
        
        if button_clicked:
            st.session_state.selected_category = category
        
        if st.session_state.selected_category == category:
            button_style = "background-color: #4CAF50; color: white; border: none; padding: 10px 24px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px;"
        else:
            button_style = "background-color: #f1f1f1; color: black; border: none; padding: 10px 24px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px;"

        # Apply custom button style using HTML
        st.markdown(f'<button style="{button_style}">{category}</button>', unsafe_allow_html=True)

    # Show date inputs if the category is selected
    if st.session_state.selected_category == category:
        with col2:
            data_inicial = st.date_input("Data Inicial", key=f"{category}_data_inicial", value=date.today())
        with col3:
            data_final = st.date_input("Data Final", key=f"{category}_data_final", value=date.today())

        # Display the selected dates
        st.write(f"Para a categoria {category}, você selecionou as datas:")
        st.write(f"Data Inicial: {data_inicial}")
        st.write(f"Data Final: {data_final}")
