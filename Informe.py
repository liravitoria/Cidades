import pandas as pd
import streamlit as st

# Adicione um link para buscar a base de dados
st.markdown("[Clique aqui para buscar a base de dados](http://blog.mds.gov.br/redesuas/lista-de-municipios-brasileiros/)")

# Leitura dos arquivos CSV
municio_df = pd.read_csv('municio.csv', delimiter=';')
estados_df = pd.read_csv('estados.csv', delimiter=';')

# Título do aplicativo
st.title('Análise de Estados e Municípios')

# Informações sobre o DataFrame do município
st.header("Informações sobre o DataFrame do município:")
# Use st.dataframe() para exibir o DataFrame
st.dataframe(municio_df)

# Informações sobre o DataFrame do estado
st.header("Informações sobre o DataFrame do estado:")
# Use st.dataframe() para exibir o DataFrame
st.dataframe(estados_df)

# Contagem de estados e municípios
quantidade_estados = estados_df['Estado'].nunique()
quantidade_municio = municio_df['Município'].nunique()

# Exibição da quantidade de estados e municípios
st.header("Quantidade de Estados e Municípios")
st.write(f"Quantidade de estados: {quantidade_estados}")
st.write(f"Quantidade de municípios: {quantidade_municio}")