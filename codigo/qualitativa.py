import pandas as pd
import matplotlib.pyplot as plt

file_in = "../cars_data.csv"
folder_out = "../plots/"
plot_quali = folder_out + "plots_quali.pdf"
table_quali = folder_out + "table_quali"

df = pd.read_csv(file_in)

#print(df.dtypes)

#Treating the qualitative data "origin", which has the origin of the studied penguins
origin = df['origin'].value_counts().reset_index()
origin.columns = ['origin', 'frequency']
print(origin)


#Plots for the qualitative variable
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

fig.suptitle('Distribuição das Espécies de Pinguins', fontsize=14)

# Pie chart
axs[0].pie(origin['frequency'], labels=origin['origin'], autopct='%1.1f%%')
axs[0].set_title('Distribuição (Pizza)')

# bars
bars = axs[1].bar(origin['origin'], origin['frequency'])
axs[1].set_title('Frequência (Barras)')
axs[1].set_xlabel('Origem')
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
#plt.show()

origin.to_latex(table_quali)





#prints a lot of information (like mean, min, max, percentile...)
#print(df.describe())