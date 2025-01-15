# Python Insights - Analisando Dados com Python

### Case - Cancelamento de Clientes
"""
Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.

Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.

Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link

"""

#passo a passo
# !pip install pandas numpy openpyxl nbformat ipykernel plotly
#1-Importar a base de dados

import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")


#2-Visualizar a base de dados
# informaçoes que nao te ajudam, te atrapalham
#CustomerID
display(tabela)


#3-corrigir os problemas da base de dados(tratamento de dados)
#4-analise inicial -> quantos clientes cancelaram e qual a % de cliente
#5-analise da causa de cancelamento dos clientes

#3-corrigir os problemas da base de dados(tratamento de dados)
display(tabela.info())

tabela = tabela.dropna()

display(tabela.info())

#4-analise inicial -> quantos clientes cancelaram e qual a % de cliente
display(tabela["cancelou"].value_counts())

#percentual
display(tabela["cancelou"].value_counts(normalize=True))


display(tabela["assinatura"].value_counts())


#5-analise da causa de cancelamento dos clientes
#comparar assinatura 
#sempre que quiser usar grafico vai 2 etapas criar e exibir 
import plotly.express as px

for coluna in tabela.columns:
    #criar grafico
    grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto="True")
    #exibir grafico
    grafico.show()
    
    #duracao_contrato -> diferente de mensal
condicao = tabela["duracao_contrato"] != "Monthly"
tabela = tabela[condicao]

#ligacoes_callcenter -> menor ou igual a 4
condicao = tabela["ligacoes_callcenter"] <=4
tabela = tabela[condicao]

#atraso_pagamento <= 20 dias>
condicao = tabela["dias_atraso"] <=20
tabela = tabela[condicao]



#percentual
display(tabela["cancelou"].value_counts(normalize=True))
