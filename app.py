import streamlit as st
import pandas as pd
from modules.data_generator import generate_fake_breach_data
from modules.visuals import plot_breaches_by_sector, plot_breach_type_pie

st.set_page_config(page_title="🛡️ BreachWatch", layout="wide")

st.title("🛡️ BreachWatch: Explorador de Vazamentos de Dados")
st.markdown("Explore vazamentos de dados **simulados** com foco em **educação sobre segurança e privacidade**.")

# Gerar ou carregar dados
if 'breach_data' not in st.session_state:
    st.session_state.breach_data = generate_fake_breach_data()

df = st.session_state.breach_data

st.sidebar.header("🔎 Filtros")

# Filtro por ano
df['Ano'] = pd.to_datetime(df['Data de Vazamento']).dt.year
anos = sorted(df['Ano'].unique())
ano_selecionado = st.sidebar.selectbox("Ano do vazamento", options=anos)

# Filtro por setor
setores = sorted(df['Setor'].unique())
setor_selecionado = st.sidebar.multiselect("Setor", options=setores, default=setores)

# Aplicar filtros
df_filtrado = df[(df['Ano'] == ano_selecionado) & (df['Setor'].isin(setor_selecionado))]

# Mostrar tabela
st.subheader("📋 Vazamentos encontrados")
st.dataframe(df_filtrado)

# Visualizações
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_breaches_by_sector(df_filtrado), use_container_width=True)
with col2:
    st.plotly_chart(plot_breach_type_pie(df_filtrado), use_container_width=True)

# Rodapé
st.caption("🔒 Os dados exibidos são **fictícios** e gerados para fins educativos.")