import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. CARREGAMENTO E VISUALIZAÇÃO INICIAL ---

# Simulação: Carregando um arquivo CSV já tratado com dados da PNAD.
# No cenário real, este arquivo conteria as colunas: 'ano', 'sexo', 'cor', 'renda'
# df = pd.read_csv("pnad.csv")

# Criando dados de exemplo para demonstrar que o código funciona
data = {
    'ano': [2012, 2012, 2012, 2012, 2022, 2022, 2022, 2022] * 100,
    'sexo': ['Homem', 'Mulher', 'Homem', 'Mulher', 'Homem', 'Mulher', 'Homem', 'Mulher'] * 100,
    'cor': ['Branca', 'Branca', 'Preta', 'Preta', 'Branca', 'Branca', 'Preta', 'Preta'] * 100,
    'renda': [3500, 2800, 2000, 1500, 4200, 3400, 2500, 1900] * 100 # Valores fictícios
}
df = pd.DataFrame(data)

# Mostrando as primeiras linhas para verificação
print("Amostra dos Dados:")
print(df.head())

# --- 2. TRATAMENTO DE DADOS (PANDAS) ---

# Função para criar a coluna de Perfil combinando Gênero e Raça
def criar_perfil(linha):
    return f"{linha['sexo']} - {linha['cor']}"

df['perfil'] = df.apply(criar_perfil, axis=1)

# --- 3. ANÁLISE DOS DADOS (AGRUPAMENTO) ---

# Cálculo da MÉDIA de renda agrupada por Ano e Perfil
tabela_medias = df.groupby(['ano', 'perfil'])['renda'].mean().reset_index()

print("\nMédia Salarial por Grupo (Dados Agregados):")
print(tabela_medias)

# --- 4. VISUALIZAÇÃO (GRÁFICO) ---

# Configurando o gráfico para melhor visualização
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Criando o gráfico de linhas com Seaborn para mostrar a tendência
sns.lineplot(
    data=tabela_medias,
    x='ano',
    y='renda',
    hue='perfil', # Cada cor de linha representa um perfil
    marker='o',
    linewidth=2.5
)

# Configurações de título e rótulos
plt.title('Evolução da Renda Média por Perfil (2012-2022) - Simulado', fontsize=14, fontweight='bold')
plt.ylabel('Renda Média (R$)', fontsize=12)
plt.xlabel('Ano', fontsize=12)
plt.legend(title='Perfil Demográfico', title_fontsize='13', fontsize='11')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout() # Ajusta o layout para evitar sobreposição
plt.show()

# Fim do Código