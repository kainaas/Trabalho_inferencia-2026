import pandas as pd
import matplotlib.pyplot as plt

file_in = "../cars_data.csv"
folder_out = "../plots/"
plot_quali = folder_out + "plots_quali.pdf"
table_quali = folder_out + "table_quali"

df = pd.read_csv(file_in)


#Treating the qualitative data "origin", which has the origin of the studied penguins
origin = df['origin'].value_counts().reset_index()
origin.columns = ['origin', 'frequency']
print(origin)


#Plots for the qualitative variable
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

#TODO: change the name of the suptitle
fig.suptitle('Origem dos carros produzidos', fontsize=14)

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


#Table
freq_cumsum = origin['frequency'].cumsum().reset_index()
freq_cumsum.columns = ['index', 'cumulative frequency']
table = pd.merge(origin, freq_cumsum['cumulative frequency'], left_index = True, right_index = True)
table.to_latex(table_quali, index=False)