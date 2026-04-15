import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



file_in = "../cars_data.csv"
folder_out = "../plots/"
plot_disc = folder_out + "plots_disc.pdf"
table_disc = folder_out + "table_disc"

df = pd.read_csv(file_in)

#amount of cylinder in the car engine
disc = df['cylinders']

#Creates the ordered data (rol) 
disc = disc.sort_values()


#number of observations
n = disc.count()

#a)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
mean = disc.mean()
print(f"media: {mean}")

Mo = disc.mode().to_numpy()[0]
print(f"moda: {Mo}")

Me = disc.median()
print(f"mediana: {Me}")
print('==========================================')

#b)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
quartis = disc.quantile([0.25, 0.5, 0.75])
quartis = quartis.to_numpy()
print(f"quartis: {quartis}")
print('==========================================')

#c)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
A = disc.max() - disc.min()
print(f"amplitude: {A}")

A_inter_quartil = quartis[2] - quartis[0]
print(f"amplitude interquartilica: {A_inter_quartil}")

standard_deviation = disc.std() #by defauld, divides by N-1
print(f"desvio-padrao: {standard_deviation}")

CV = standard_deviation/mean
print(f"Coeficiente de variacao: {CV}")
print('==========================================')

#d) data is slightly assymetrical to the right mean > Me = Mo %%%%%%%%%%%%%%%%%%%%%%%%%%


#e)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
unique = disc.nunique()
print(f"numero de valores diferentes: {unique}")

freqs_table = disc.value_counts(sort = False) #maybe this works
freqs_table = freqs_table.reset_index()
freqs_table.columns = ['cylinders', 'frequency']

freq_cumsum = freqs_table['frequency'].cumsum().reset_index()
freq_cumsum.columns = ['index', 'cumulative frequency']

freqs_np = freqs_table['frequency'].to_numpy()

freq_cumsum_np = freq_cumsum.to_numpy()[:,1]

freqs_relative = pd.DataFrame(freqs_np/n)
freqs_relative.columns = ['relative frequency']

freqs_relative_cumsum = pd.DataFrame(freq_cumsum_np/n)
freqs_relative_cumsum.columns = ['relative cumulative frequency']

freqs_table = pd.merge(freqs_table, freq_cumsum['cumulative frequency'], left_index = True, right_index = True)
freqs_table = pd.merge(freqs_table, freqs_relative, left_index = True, right_index = True)
freqs_table = pd.merge(freqs_table, freqs_relative_cumsum, left_index = True, right_index = True)
freqs_table.to_latex(table_disc, index=False)
print('==========================================')


#f) table info is the same as the rol info

#g)
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

fig.suptitle(r'Número de cilindros nos motores dos carros produzidos', fontsize=14)

#bar
axs[0].bar(freqs_table['cylinders'], freqs_table['frequency'])
axs[0].set_title('Gráfico de Barras')

#boxplot
axs[1].boxplot(disc)
axs[1].set_title('Boxplot')

fig.savefig(plot_disc)
plt.show()