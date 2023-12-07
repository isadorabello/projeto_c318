import random
import pandas as pd

random.seed(5)
URL_ARQUIVO = "./arquivos_csv/202112.csv"
URL_ARQUIVO_GEOGRAFICO = "./arquivos_csv/geografia.csv"
URL_ARQUIVO_HISTORICO = "./arquivos_csv/HISTORICO_PLANOS.csv"
URL_ARQUIVO_LAT_LONG = "./arquivos_csv/latitude-longitude-cidades.csv"
DATA_BASE = 2022

vendas = pd.read_csv(URL_ARQUIVO, delimiter=';', skiprows=lambda x: x > 0 and random.random() >= 0.05, na_values="n/a")

historico_ext = pd.read_csv(URL_ARQUIVO_HISTORICO, sep=",", low_memory=False)
historico = historico_ext[['ID_PLANO', 'DT_FIM_STATUS', 'DE_SITUACAO_PRINCIPAL']]

merge_historico = pd.merge(vendas, historico, how='left', on='ID_PLANO').dropna()
merge_historico = merge_historico[merge_historico['DT_FIM_STATUS'].str.slice(6).astype(int) < DATA_BASE]
merge_historico = merge_historico[merge_historico['DE_SITUACAO_PRINCIPAL'] == 'ATIVO']
# merge_historico['VCM'] = merge_historico['VCM'].str.replace(',', '.').astype(float)

geografia_ext = pd.read_csv(URL_ARQUIVO_GEOGRAFICO, delimiter=';')
geografia = geografia_ext[['CD_MUNICIPIO', 'NM_MUNICIPIO', 'SG_UF', 'NM_REGIAO']]

dataset = pd.merge(merge_historico, geografia, how='inner', on='CD_MUNICIPIO')
dataset['VCM'] = dataset['VCM'].str.replace(',', '.').astype(float)
# print(dataset)

# print("A descrição do dataset: \n",dataset.describe())

lat_long = pd.read_csv(URL_ARQUIVO_LAT_LONG, delimiter=',')
lat_long = lat_long[['NM_MUNICIPIO', 'latitude', 'longitude']]
dataset_lat_long = pd.merge(dataset, lat_long, how='inner', on='NM_MUNICIPIO')

# regiao = lat_long['NM_REGIAO'].unique()
# print('Escolha uma região para analisar')
# for r in regiao:
#     print(r, end=' ')

regiao = 'Sudeste'
filtro_regiao = lat_long[lat_long['NM_REGIAO'] == regiao]

# uf = filtro_regiao['SG_UF'].unique()
# print('Escolha um estado para analisar')
# for e in uf:
#     print(e, end=' ')

uf = 'MG'
uf_filtrado = filtro_regiao[filtro_regiao['SG_UF'] == uf]

# cidade = uf_filtrado['NM_MUNICIPIO'].unique()
# print('Escolha um município para analisar')
# for c in cidade:
#     print(c)

c_escolhida = 'Santa Rita do Sapucaí'
cidade_filtrada = uf_filtrado[uf_filtrado['NM_MUNICIPIO'] == c_escolhida]
# cidade_filtrada.plot(kind='scatter', x='longitude', y='latitude')




