# analitics.py
import pandas as pd
import streamlit as st
from humanities_visualizations import show_humanities_visualizations

# Configuração do layout
st.set_page_config(layout="wide", page_title="Análise de Dados")
st.title("📊 Painel de Análise")

# --- SIDEBAR (Filtros e Upload) ---
with st.sidebar:
    st.header("📂 Configurações")
    
    # Upload do arquivo
    uploaded_file = st.file_uploader(
        "Carregar arquivo de dados",
        type=["csv", "xlsx"],
        key="file_upload"
    )
    
    st.markdown("---")
    
    # Carregar dados mesmo sem arquivo (exemplo)
    @st.cache_data
    def load_data(file):
        if file is None:
            return pd.DataFrame({
                'Categoria': ['A', 'B', 'C'] * 10,
                'Valor': range(30, 60),
                'Região': ['Norte', 'Sul'] * 15,
                'Data': pd.date_range('2023-01-01', periods=30)
            })
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        return pd.read_excel(file)
    
    df = load_data(uploaded_file)
    
    # Filtros dinâmicos
    with st.expander("🔍 Filtros Avançados"):
        filters = {}
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                min_val, max_val = float(df[col].min()), float(df[col].max())
                filters[col] = st.slider(
                    f"Intervalo de {col}",
                    min_val, max_val, (min_val, max_val)
                )  # Faltava fechar este parênteses
            elif df[col].nunique() < 20:
                options = sorted(df[col].unique())
                filters[col] = st.multiselect(
                    f"Selecionar {col}",
                    options,
                    default=options
                )

# Aplicar filtros
df_filtered = df.copy()
for col, val in filters.items():
    if pd.api.types.is_numeric_dtype(df[col]):
        df_filtered = df_filtered[
            (df_filtered[col] >= val[0]) & 
            (df_filtered[col] <= val[1])
        ]
    else:
        df_filtered = df_filtered[df_filtered[col].isin(val)]

# --- ÁREA PRINCIPAL ---
tab1, tab2 = st.tabs(["📈 Visualizações", "🗃 Dados"])

with tab1:
    show_humanities_visualizations(df_filtered)

with tab2:
    st.header("Dados Filtrados")
    st.dataframe(df_filtered, height=400)
    st.download_button(
        label="Baixar dados filtrados",
        data=df_filtered.to_csv(index=False).encode('utf-8'),
        file_name='dados_filtrados.csv',
        mime='text/csv'
    ) 