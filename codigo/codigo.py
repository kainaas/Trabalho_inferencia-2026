import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_in = "../penguins.csv"
folder_out = "../plots/"
plot_quali = folder_out + "plots_quali.pdf"

df = pd.read_csv(file_in)

#print(df.dtypes)

#Treating the qualitative data "species", which has the species of the studied penguins
species = df['species'].value_counts().reset_index()
species.columns = ['species', 'frequency']
print(species)


#Plots for the qualitative variable
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

fig.suptitle('Distribuição das Espécies de Pinguins', fontsize=14)

# Pie chart
axs[0].pie(species['frequency'], labels=species['species'], autopct='%1.1f%%')
axs[0].set_title('Distribuição (Pizza)')

# bars
bars = axs[1].bar(species['species'], species['frequency'])
axs[1].set_title('Frequência (Barras)')
axs[1].set_xlabel('Espécies')
axs[1].set_ylabel('Frequência')
for bar in bars:
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f'{int(height)}',
        ha='center',
        va='bottom'
    )

fig.savefig(plot_quali)
plt.show()




#prints a lot of information (like mean, min, max, percentile...)
#print(df.describe())