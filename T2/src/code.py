import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Dados da Amostra (Lendo diretamente do arquivo txt)
try:
    # Carrega os dados do arquivo txt. 
    # O arquivo precisa estar na mesma pasta que este script Python.
    amostra_15 = np.loadtxt('AMOSTRA_15.txt')
except FileNotFoundError:
    print("ERRO: O arquivo 'AMOSTRA_15.txt' não foi encontrado.")
    print("Verifique se o arquivo está salvo na mesma pasta deste script.")
    exit()

n = len(amostra_15)
soma_y = np.sum(amostra_15)
media_amostral = soma_y / n

print(f"n: {n} | Soma de y: {soma_y} | Média Amostral: {media_amostral:.4f}")

# Hiperparâmetros
alpha_1, beta_1 = 6, 0.5
alpha_2, beta_2 = 12, 1.0

# Parâmetros das Posteriores
alpha_post1 = soma_y + alpha_1
beta_post1 = n + beta_1

alpha_post2 = soma_y + alpha_2
beta_post2 = n + beta_2

print(f"Estimativa Posteriori 1: {alpha_post1 / beta_post1:.4f}")
print(f"Estimativa Posteriori 2: {alpha_post2 / beta_post2:.4f}")

# 2. Definição do Eixo X para plotagem
x = np.linspace(4, 20, 1000)

# Distribuições Priori
pdf_priori1 = stats.gamma.pdf(x, a=alpha_1, scale=1/beta_1)
pdf_priori2 = stats.gamma.pdf(x, a=alpha_2, scale=1/beta_2)

# Distribuições Posteriori
pdf_post1 = stats.gamma.pdf(x, a=alpha_post1, scale=1/beta_post1)
pdf_post2 = stats.gamma.pdf(x, a=alpha_post2, scale=1/beta_post2)

# 3. Plotagem do Item A (Prioris)
plt.figure(figsize=(10, 5))
plt.plot(x, pdf_priori1, label=r'Priori 1 ($\alpha=6, \beta=0.5$)', color='blue')
plt.plot(x, pdf_priori2, label=r'Priori 2 ($\alpha=12, \beta=1.0$)', color='green')
plt.title('Distribuições a Priori')
plt.xlabel(r'$\lambda$')
plt.ylabel('Densidade')

# Colocando a legenda abaixo do gráfico para não sobrepor no relatório
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 4. Plotagem do Item D (Priori vs Posteriori)
plt.figure(figsize=(12, 6))

# Plot Priori 1 e Posteriori 1
plt.subplot(1, 2, 1)
plt.plot(x, pdf_priori1, label='Priori 1', linestyle='--', color='blue')
plt.plot(x, pdf_post1, label='Posteriori 1', color='darkblue')
plt.axvline(media_amostral, color='red', linestyle=':', label='Média Amostral')
plt.title('Cenário 1: Priori x Posteriori')
plt.xlabel(r'$\lambda$')
plt.ylabel('Densidade')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=1, frameon=False)

# Plot Priori 2 e Posteriori 2
plt.subplot(1, 2, 2)
plt.plot(x, pdf_priori2, label='Priori 2', linestyle='--', color='green')
plt.plot(x, pdf_post2, label='Posteriori 2', color='darkgreen')
plt.axvline(media_amostral, color='red', linestyle=':', label='Média Amostral')
plt.title('Cenário 2: Priori x Posteriori')
plt.xlabel(r'$\lambda$')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=1, frameon=False)

plt.tight_layout()
plt.show()