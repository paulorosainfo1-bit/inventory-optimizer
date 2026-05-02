import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="Business Intelligence - Inventory Optimizer", layout="wide")

st.title("📊 Global Inventory & Profit Optimizer")
st.markdown("Automated Business Intelligence Engine for Inventory and Profitability Analysis.")

# 1. File Upload
st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Upload your sales CSV data", type=["csv"])

if uploaded_file is not None:
    # Reading data
    df = pd.read_csv(uploaded_file)
    
    # Auto Calculations
    df['Revenue'] = df['Unit_Price'] * df['Units_Sold']
    df['Profit'] = (df['Unit_Price'] - df['Unit_Cost']) * df['Units_Sold']
    
    # Main Metrics (Top Cards)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")
    with col2:
        st.metric("Total Profit", f"${df['Profit'].sum():,.2f}", delta=f"{(df['Profit'].sum()/df['Revenue'].sum()*100):.1f}% Margin")
    with col3:
        st.metric("Units Sold", f"{df['Units_Sold'].sum():,}")

    # 2. Interactive Chart
    st.subheader("Profit Analysis by Category")
    fig = px.bar(df.groupby('Category')['Profit'].sum().reset_index(), 
                 x='Category', y='Profit', color='Category',
                 title="Profit Distribution by Category")
    st.plotly_chart(fig, use_container_width=True)

    # 3. Detailed Data Table
    st.subheader("Detailed Inventory View")
    st.dataframe(df)

else:
    # AQUI ESTÁ A CORREÇÃO: Mensagem profissional em inglês
    st.info("💡 Awaiting CSV file upload to begin the analysis. For demonstration purposes, you can use a csv file.")
