import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#number of classes
k = 10

file_in = "../cars_data.csv"
folder_out = "../plots/"
plot_cont = folder_out + "plots_cont.pdf"
table_cont = folder_out + "table_cont"

df = pd.read_csv(file_in)

#The continuous variable is the acceleration in mph^2, usually calculated by accelerating from 0 to 60mph at max power
continua = df['acceleration']


#Creates the ordered data (rol) 
continua = continua.sort_values()

#a)
mean = continua.mean()
Mo = continua.mode().to_numpy()[0]
Me = continua.median()

print(f"media: {mean}")
print(f"moda: {Mo}")
print(f"mediana: {Me}")

#b)
quartis = continua.quantile([0.25, 0.5, 0.75])
quartis = quartis.to_numpy()
print(f"quartis: {quartis}")

#c)
A = continua.max() - continua.min()
print(f"amplitude: {A}")

A_inter_quartil = quartis[2] - quartis[0]
print(f"amplitude interquartilica: {A_inter_quartil}")

standard_deviation = continua.std() #by defauld, divides by N-1
print(f"desvio-padrao: {standard_deviation}")

CV = standard_deviation/mean
print(f"Coeficiente de variacao: {CV}")

#d) data is slightly assymetrical to the right mean > Me > Mo

#e)
freqs = pd.cut(continua, bins = k)
freqs_table = freqs.value_counts(sort = False) #maybe this works
freqs_table = freqs_table.reset_index()
freqs_table.columns = ['acceleration', 'frequency']
freqs_table.to_latex("teste")

classes_np = freqs_table['acceleration'].to_numpy()
freqs_np = freqs_table['frequency'].to_numpy()
print(classes_np[0].left)

#f)
#continua.plot.hist()
#plt.show()