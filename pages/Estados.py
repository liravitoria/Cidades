import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados do arquivo CSV
file_path = "estados.csv"
data = pd.read_csv(file_path, delimiter=';')

# Verificar se a coluna 'Qtd Mun' existe no DataFrame
if 'Qtd Mun' not in data.columns:
    st.error("A coluna 'Qtd Mun' não foi encontrada no arquivo CSV.")
else:
    # Configuração da página do Streamlit
    st.title("Quantidade de Municípios por Estado")

    # Adicionar filtro de faixa de valores
    min_mun = st.slider('Escolha a quantidade mínima de municípios:', min(data['Qtd Mun']), max(data['Qtd Mun']), min(data['Qtd Mun']))
    max_mun = st.slider('Escolha a quantidade máxima de municípios:', min(data['Qtd Mun']), max(data['Qtd Mun']), max(data['Qtd Mun']))

    # Filtrar os dados com base na faixa escolhida
    filtered_data = data[(data['Qtd Mun'] >= min_mun) & (data['Qtd Mun'] <= max_mun)]

    # Ordenar os dados pela população de forma decrescente
    filtered_data = filtered_data.sort_values(by='Qtd Mun', ascending=False)

    # Criar gráfico de barras
    st.bar_chart(filtered_data.set_index('Estado')['Qtd Mun'])

    # Criar mapa
    st.subheader("Mapa de Quantidade de Municípios por Estado")
    fig = px.choropleth(
        filtered_data,
        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson',
        featureidkey='properties.sigla',
        locations='UF',
        color='Qtd Mun',
        color_continuous_scale='Viridis',
        scope="south america",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)

    # Exibir tabela com os dados ordenados
    st.subheader("Tabela de Quantidade de Municípios por Estado")
    st.write(filtered_data)