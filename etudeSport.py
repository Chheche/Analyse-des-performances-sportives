import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_excel("C:\\Users\\rafae\\OneDrive\\Documents\\Project\datasetSport.xlsx", engine="openpyxl")

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

df.hist(figsize=(10, 8))

# Répartition des niveaux sportifs
sns.countplot(x="Niveau sportif", data=df, hue="Sexe")
plt.title("Répartition des niveaux sportifs par sexe")
plt.show()

# Comparaison du nombre de tractions max par sexe entre pays
sns.boxplot(x='Sexe', y='Nombre de tractions max', data=df, hue='Pays')
plt.show()

# Comparaison par sexe du nombre de tractions max avec un boxplot
sns.boxplot(data=df, x="Sexe", y="Nombre de tractions max")
plt.title("Comparaison des tractions max entre hommes et femmes")
plt.show()

# Comparaison par sexe du temps sur 5km avec un boxplot
sns.boxplot(data=df, x="Sexe", y="Temps sur 5 km (min)", hue='Pays')
plt.title("Comparaison du temps 5 km entre hommes et femmes")
plt.show()

#Comparaison par sexe du nombre de tractions max avec un boxplot
sns.scatterplot(x="Age", y="Temps sur 5 km (min)", data=df, hue="Sexe")
plt.title("Relation entre l'âge et le temps sur 5 km")
plt.show()

# Calcul des corrélations
corr_matrix = df.select_dtypes(include=['number']).corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Matrice de corrélation entre les variables")
plt.show()

X = df["Heures de sport par semaine"]
y = df["Temps sur 5 km (min)"]
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())