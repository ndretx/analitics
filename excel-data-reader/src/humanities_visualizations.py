import pandas as pd
import plotly.express as px
import streamlit as st

def show_humanities_visualizations(data):
    """Mostra visualizações na área principal"""
    if data.empty:
        st.warning("Nenhum dado disponível para visualização")
        return
    
    # Seleção do tipo de gráfico
    chart_type = st.selectbox(
        "Selecione o tipo de visualização:",
        options=[
            "Gráfico de Barras",
            "Gráfico de Linhas",
            "Histograma",
            "Gráfico de Dispersão",
            "Gráfico de Pizza"
        ],
        key="chart_type"
    )
    
    # Configurações específicas para cada gráfico
    if chart_type == "Gráfico de Barras":
        x_col = st.selectbox("Eixo X", data.columns, key="bar_x")
        y_col = st.selectbox("Eixo Y", data.select_dtypes('number').columns, key="bar_y")
        fig = px.bar(data, x=x_col, y=y_col)
    
    elif chart_type == "Gráfico de Linhas":
        x_col = st.selectbox("Eixo X", data.columns, key="line_x")
        y_col = st.selectbox("Eixo Y", data.select_dtypes('number').columns, key="line_y")
        fig = px.line(data, x=x_col, y=y_col)
    
    elif chart_type == "Histograma":
        col = st.selectbox("Coluna", data.select_dtypes('number').columns, key="hist_col")
        fig = px.histogram(data, x=col)
    
    elif chart_type == "Gráfico de Dispersão":
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("Eixo X", data.select_dtypes('number').columns, key="scatter_x")
            y_col = st.selectbox("Eixo Y", data.select_dtypes('number').columns, key="scatter_y")
        with col2:
            hover_col = st.selectbox("Info adicional", data.columns, key="scatter_hover")
        
        # Prepara dados com índice para o hover
        data_with_index = data.reset_index()
        fig = px.scatter(
            data_with_index,
            x=x_col,
            y=y_col,
            hover_data=[hover_col, 'index'],
            custom_data=['index']
        )
        
        fig.update_traces(
            hovertemplate=f"""
            <b>Índice</b>: %{{customdata[0]}}<br>
            <b>{x_col}</b>: %{{x}}<br>
            <b>{y_col}</b>: %{{y}}<br>
            <b>{hover_col}</b>: %{{customdata[1]}}<br>
            <extra></extra>
            """
        )
        
        # Adiciona interatividade de seleção de pontos
        try:
            from streamlit_plotly_events import plotly_events
            selected = plotly_events(fig, click_event=True)
            if selected:
                idx = selected[0]['pointIndex']
                st.write("Dados completos do ponto selecionado:")
                st.write(data.iloc[idx])
        except ImportError:
            pass
    
    elif chart_type == "Gráfico de Pizza":
        col = st.selectbox("Coluna", data.select_dtypes(exclude='number').columns, key="pie_col")
        fig = px.pie(data, names=col)
    
    st.plotly_chart(fig, use_container_width=True)