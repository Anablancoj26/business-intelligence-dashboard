import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="BI Analytics Dashboard", page_icon="📊", layout="wide")

st.title("📊 Business Intelligence & Performance Dashboard")
st.markdown("Dashboard analítico para la toma de decisiones estratégicas basado en datos.")

# Carga de datos
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# Sidebar para filtros
st.sidebar.header("Filtros de Análisis")
region_filter = st.sidebar.selectbox("Seleccione la Región", options=["Todas"] + list(df["Region"].unique()))

if region_filter != "Todas":
    df_filtered = df[df["Region"] == region_filter]
else:
    df_filtered = df

# Cálculo de KPIs principales
total_sales = df_filtered["Ventas"].sum()
total_units = df_filtered["Unidades"].sum()
avg_sale = df_filtered["Ventas"].mean() if not df_filtered.empty else 0

col1, col2, col3 = st.columns(3)
col1.metric("💰 Ventas Totales", f"${total_sales:,.2f}")
col2.metric("📦 Unidades Vendidas", f"{total_units}")
col3.metric("📈 Venta Promedio", f"${avg_sale:,.2f}")

st.markdown("---")

# Visualizaciones con Plotly
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Ventas por Categoría")
    fig_cat = px.bar(df_filtered, x="Categoria", y="Ventas", color="Categoria", title="Ingresos según Categoría de Producto")
    st.plotly_chart(fig_cat, use_container_width=True)

with col_chart2:
    st.subheader("Distribución por Región")
    fig_reg = px.pie(df_filtered, names="Region", values="Ventas", title="Participación de Ventas por Región")
    st.plotly_chart(fig_reg, use_container_width=True)

# Tabla de datos detallados
st.subheader("📋 Registro Detallado de Operaciones")
st.dataframe(df_filtered, use_container_width=True)
