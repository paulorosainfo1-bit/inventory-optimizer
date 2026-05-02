import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Business Intelligence - Inventory Optimizer", layout="wide")

st.title("📊 Global Inventory & Profit Optimizer")
st.markdown("Trabalho de consultoria técnica para otimização de estoques e lucros.")

# 1. Upload do Arquivo
st.sidebar.header("Configurações")
uploaded_file = st.sidebar.file_uploader("Faça o upload do seu CSV de vendas", type=["csv"])

if uploaded_file is not None:
    # Lendo os dados
    df = pd.read_csv(uploaded_file)
    
    # Cálculos Automáticos
    df['Revenue'] = df['Unit_Price'] * df['Units_Sold']
    df['Profit'] = (df['Unit_Price'] - df['Unit_Cost']) * df['Units_Sold']
    
    # Métricas Principais (Os cartões no topo)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Receita Total", f"${df['Revenue'].sum():,.2f}")
    with col2:
        st.metric("Lucro Total", f"${df['Profit'].sum():,.2f}", delta=f"{(df['Profit'].sum()/df['Revenue'].sum()*100):.1f}% Margem")
    with col3:
        st.metric("Produtos Vendidos", f"{df['Units_Sold'].sum():,}")

    # 2. Gráfico Interativo
    st.subheader("Análise de Lucro por Categoria")
    fig = px.bar(df.groupby('Category')['Profit'].sum().reset_index(), 
                 x='Category', y='Profit', color='Category',
                 title="Onde está o seu maior lucro?")
    st.plotly_chart(fig, use_container_width=True)

    # 3. Tabela de Dados com Filtro
    st.subheader("Visão Detalhada do Estoque")
    st.dataframe(df)

else:
    st.info("Aguardando upload do arquivo CSV para iniciar a análise.")
    st.warning("Dica: Você pode usar o arquivo 'mock_sales_data.csv' que geramos antes!")