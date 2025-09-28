import pandas as pd
import zipfile
import matplotlib.pyplot as plt
import seaborn as sns

# ZIP route
zip_path = "poker+hand.zip"

# Cols
cols = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','hand']
# S = Palo de la carta 
# C = Valor de la carta
# hand = Clase de mano (0 = valor más alto, 1 = par, etc...)

with zipfile.ZipFile(zip_path) as z:
    with z.open("poker-hand-training-true.data") as f:
        train_df = pd.read_csv(f, names=cols)
    with z.open("poker-hand-testing.data") as f:
        test_df = pd.read_csv(f, names=cols)

print("\n",train_df.head())
print("\n", test_df.head())

# --- EDA  ---
pd.set_option('display.max_columns', None)
print("\nDtypes:\n", train_df.dtypes)
print("\nDistribución objetivo (train):")
print(train_df['hand'].value_counts())
print("\nDistribución relativa (train):")
print(train_df['hand'].value_counts(normalize=True))

# Visualizaciones (frecuencias de clases)
plt.figure(figsize=(8,4))
sns.countplot(x='hand', data=train_df)
plt.title("Frecuencia por clase (train)")
plt.show()

# Distribución de rangos (valores de carta) y palos
val_cols = ['C1','C2','C3','C4','C5']
suit_cols = ['S1','S2','S3','S4','S5']

plt.figure(figsize=(10,4))
sns.histplot(train_df[val_cols].values.ravel(), bins=13, kde=False)
plt.title("Distribución de valores de cartas (todas las posiciones)")
plt.xlabel("Valor (1=ace, ... 13=king)")
plt.show()

plt.figure(figsize=(6,3))
sns.countplot(x=train_df[suit_cols].values.ravel())
plt.title("Distribución de palos (todas las posiciones)")
plt.show()



