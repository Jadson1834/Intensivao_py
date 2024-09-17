
# passo 1 - Importar dados
import pandas

tabela = pandas.read_csv("cancelamentos_sample.csv")


# passo 2 - Visualizar dados
# tirar colunas inuteis
tabela = tabela.drop(columns="CustomerID")


# passo 3 - Tratar dados - corrigir os dados
# excluir linhas de valores vazios
tabela = tabela.dropna()
print(tabela.info())

# passo 4 - Analise dos cancelamentos
print(tabela["cancelou"].value_counts()) #valores brutos

print(tabela["cancelou"].value_counts(normalize=True)) #porcentagem bruta

print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format)) #porcentagem arredodada
# passo 5 - Analise de causas de cancelamento
import plotly.express as px

for coluna in tabela.columns:
    # criar grafico
    grafico = px.histogram(tabela, x=coluna,color="cancelou")
    # exibe grafico
    grafico.show()
    
# resolver os cancelamentos
# callcenter
tabela = tabela[tabela["ligacoes_callcenter"]<=4]   
# atraso
tabela = tabela[tabela["dias_atraso"]<=20]
# contrato
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]


# exibir
print(tabela["cancelou"].value_counts(normalize=True))
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))