import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = "../penguins.csv"
df = pd.read_csv(file_name)

print(df.dtypes)

species_quali = df['species']
species_quali_freq = pd.DataFrame(species_quali.value_counts())
species_quali.value_counts().plot.pie(y = 'count')
plt.show()
#prints a lot of information (like mean, min, max, percentile...)
#print(df.describe())