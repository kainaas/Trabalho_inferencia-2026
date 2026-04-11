import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def find_quantile_aux(p, freqs, freq_cumsum, n, k, Ac, LI):
    P = p*n
    j=0
    for i in range(1,k):
        if P <= freq_cumsum[i]:
            j = i
            break
    F_anterior = 0
    if j != 0:
        F_anterior = freq_cumsum[j-1]
    return Ac[j]*(P - F_anterior)/freqs[j] + LI[j]


def quantile_freqs(p):
    return float(find_quantile_aux(p, freqs_np, freq_cumsum_np, n, k, Ac, LI))


file_in = "../cars_data.csv"
folder_out = "../plots/"
plot_cont = folder_out + "plots_cont.pdf"
table_cont = folder_out + "table_cont"

df = pd.read_csv(file_in)

#The continuous variable is the acceleration in mph^2, usually calculated by accelerating from 0 to 60mph at max power
continua = df['acceleration']


#Creates the ordered data (rol) 
continua = continua.sort_values()

#number of observations
n = continua.count()

#number of classes
k = 10

#a)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
mean = continua.mean()
print(f"media: {mean}")

Mo = continua.mode().to_numpy()[0]
print(f"moda: {Mo}")

Me = continua.median()
print(f"mediana: {Me}")
print('==========================================')

#b)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
quartis = continua.quantile([0.25, 0.5, 0.75])
quartis = quartis.to_numpy()
print(f"quartis: {quartis}")
print('==========================================')

#c)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
A = continua.max() - continua.min()
print(f"amplitude: {A}")

A_inter_quartil = quartis[2] - quartis[0]
print(f"amplitude interquartilica: {A_inter_quartil}")

standard_deviation = continua.std() #by defauld, divides by N-1
print(f"desvio-padrao: {standard_deviation}")

CV = standard_deviation/mean
print(f"Coeficiente de variacao: {CV}")
print('==========================================')

#d) data is slightly assymetrical to the right mean > Me > Mo %%%%%%%%%%%%%%%%%%%%%%%%%%

#e)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
freqs = pd.cut(continua, bins = k)
freqs_table = freqs.value_counts(sort = False) #maybe this works
freqs_table = freqs_table.reset_index()
freqs_table.columns = ['acceleration', 'frequency']

freq_cumsum = freqs_table['frequency'].cumsum().reset_index()
freq_cumsum.columns = ['index', 'cumulative frequency']

freqs_table = pd.merge(freqs_table, freq_cumsum['cumulative frequency'], left_index = True, right_index = True)
freqs_table.to_latex(table_cont)


#f)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
classes_np = freqs_table['acceleration'].to_numpy()
freqs_np = freqs_table['frequency'].to_numpy()

Pm = np.zeros(k) #mean points of the classes
for i in range(len(classes_np)): #calculate the mean points
    Pm[i] = (classes_np[i].right + classes_np[i].left)/2

Ac = np.zeros(k) #classes amplitude
for i in range(len(classes_np)): #calculate the mean points
    Ac[i] = classes_np[i].right - classes_np[i].left

LI = np.zeros(k) #Class inferior limit
for i in range(len(classes_np)): #calculate the mean points
    LI[i] = classes_np[i].left

freq_cumsum_np = freq_cumsum.to_numpy()[:,1]


mean_table = (np.array([(Pm[i]*freqs_np[i]) for i in range(k)]).sum())/n
print(f"media da tabela: {mean_table}")

Mo_table = Pm[freqs_np.argmax()] #picks the class with the most observations. Then, the mode is the mean point
print(f"moda da tabela: {Mo_table}")

quartis_table = [quantile_freqs(0.25), quantile_freqs(0.5), quantile_freqs(0.75)]
Me_table = quartis_table[1]
print(f"mediana da tabela: {Me_table}")
print(f"quartis da tabela: {quartis_table}")

standard_deviation_table = float(np.sqrt(np.array([freqs_np[i]*(Pm[i] - mean_table)**2 for i in range(k)]).sum()/(n-1)))
print(f"desvio-padrao da tabela: {standard_deviation_table}")
print('==========================================')

#g)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#Plots for the continuous variable
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

fig.suptitle('Aceleração dos carros produzido (mph)', fontsize=14)

#histogram
axs[0].hist(continua, bins=k)
axs[0].set_title('Histograma')

#boxplot
axs[1].boxplot(continua)
axs[1].set_title('Boxplot')
plt.show()