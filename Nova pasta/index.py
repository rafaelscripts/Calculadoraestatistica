import matplotlib.pyplot as plt
import pandas as pd

# Criando um dataframe com os dados da imagem
data = {
    'Você toma café?': ['Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim'],
    'Que tipo de café você prefere?': ['Café preto', 'Café preto, Café com leite, Café expresso', 
                                       'Café com leite, Cappuccino', 'Café preto, Café com leite', 
                                       'Café preto', 'Café preto', 'Cappuccino', 'Cappuccino', 
                                       'Café preto', 'Café com leite', 'Café com leite', 'Café com leite'],
    'Como prefere seu café?': ['Quente', 'Quente', 'Morno', 'Gelado', 'Morno', 'Quente', 
                               'Quente', 'Quente', 'Quente', 'Quente', 'Quente', 'Morno'],
    'Quantas vezes no dia você geralmente toma': ['Normal (2 no dia)', 'Bastante (3 a 4 no dia)', 'Normal (2 no dia)', 
                                                  'Poucas vezes (1 no dia)', 'Poucas vezes (1 no dia)', 
                                                  'Poucas vezes (1 no dia)', 'Extremamente (5+ no dia)', 
                                                  'Poucas vezes (1 no dia)', 'Poucas vezes (1 no dia)', 
                                                  'Bastante (3 a 4 no dia)', 'Extremamente (5+ no dia)', 'Normal (2 no dia)']
}

df = pd.DataFrame(data)

# Contagem dos tipos de café preferidos
tipo_cafe = df['Que tipo de café você prefere?'].value_counts()

# Contagem das vezes que tomam café por dia
vezes_por_dia = df['Quantas vezes no dia você geralmente toma'].value_counts()

# Criando os gráficos
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Gráfico de barras - Tipo de café preferido
axs[0].bar(tipo_cafe.index, tipo_cafe.values, color='c')
axs[0].set_title('Preferência de Tipo de Café')
axs[0].set_ylabel('Número de Respostas')
axs[0].tick_params(axis='x', rotation=90)

# Gráfico de barras - Quantas vezes tomam café no dia
axs[1].bar(vezes_por_dia.index, vezes_por_dia.values, color='m')
axs[1].set_title('Frequência de Consumo de Café por Dia')
axs[1].set_ylabel('Número de Respostas')
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()

# Salvando o gráfico como PNG
# Atualize o caminho para um local onde você tenha permissão para salvar ou use o caminho relativo
fig.savefig('grafico_cafe.png')  # O arquivo será salvo na pasta onde o script está rodando
