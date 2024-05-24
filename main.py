from src.files import read_config
from src.files import read_schema
from src.database import save_data
from src.database import create_tables
import pandas as pd
import numpy as np

##configuração de filtragen
config_path = "archives/config.yml"
parametros = read_config(config_path)

##Leitura do arquivo raw.npz
raw_path = "archives/data/raw.npz"
data = np.load(raw_path,allow_pickle=True)
arrays = list(data.keys())
for name in arrays:
    array = data[name]
df = pd.DataFrame(array)

##Filtragem dos valores
data_filtrado = df[(df.iloc[:, 10] == 'GASOLINA') &
                   pd.to_numeric(df.iloc[:, 12].replace(',', '.', regex=True), errors='coerce').ge(3) &
                   pd.to_numeric(df.iloc[:, 12].replace(',', '.', regex=True), errors='coerce').le(6) & 
                   (df.iloc[:, 0].isin(["N", "S"]))
                   ]

##Salvar arquivos filtrados em Json
result = data_filtrado.to_json("./archives/target/result.json",orient="index")

## Leitura do esquema e criação da tabela
schema = read_schema("./archives/schema.sql")
create_tables(schema)

## Leitura dos arquivos CSV
localization = pd.read_csv("./archives/data/localizations.csv")
prices = pd.read_csv("./archives/data/prices.csv")
products = pd.read_csv("./archives/data/products.csv")

## Criação de dataframes a partir dos CSVs
dflocals = pd.DataFrame(localization)
dfprices = pd.DataFrame(prices)
dfproducts = pd.DataFrame(products)

## Salvar os dataframes nas respectivas tabelas
save_data("localizations",dflocals)
save_data("prices",dfprices)
save_data("products",dfproducts)

schema2 = read_schema("./archives/schema2.sql")
create_tables(schema2)

merge = pd.merge(localization,prices, on = "id")
print(merge)