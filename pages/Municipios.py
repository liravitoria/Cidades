import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Carregar dados do arquivo CSV
file_path = "municio.csv"
data = pd.read_csv(file_path, delimiter=';')

# Verificar se a coluna 'População 2010' existe no DataFrame
if 'População 2010' not in data.columns:
    st.error("A coluna 'População 2010' não foi encontrada no arquivo CSV.")
else:
    # Configuração da página do Streamlit
    st.title("Top 10 Estados/Municípios por População em 2010")

    # Ordenar os dados pela população de forma decrescente
    top_10_data = data.sort_values(by='População 2010', ascending=False).head(10)

    # Criar gráfico de barras
    st.bar_chart(top_10_data.set_index('UF')['População 2010'])

    # Criar mapa
    st.subheader("Mapa dos 10 Maiores Estados/Municípios por População em 2010")

    # Load GeoJSON data from a local file
    geojson_file_path = "path/to/map.geojson"  # Replace with the actual path
    try:
        geojson_data = json.load(open(geojson_file_path, "r"))
    except FileNotFoundError:
        st.error(f"Arquivo GeoJSON não encontrado em: {geojson_file_path}")
        st.stop()

    fig = px.choropleth(
        top_10_data,
        geojson=geojson_data,
        featureidkey='properties.ISO_A3',
        locations='UF',
        color='População 2010',
        color_continuous_scale='Viridis',
        scope="south america",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)

    # Exibir tabela com os dados ordenados
    st.subheader("Tabela dos 10 Maiores Estados/Municípios por População em 2010")
    st.write(top_10_data)