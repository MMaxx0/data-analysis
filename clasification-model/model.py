import pandas as pd
import zipfile

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

# Dimensiones + Tipos de datos
# print("\nTrain shape:", train_df.shape)
# print("\nTest shape:", test_df.shape)
# X filas, 11 Columnas (Test > Training)

# print(f"\n{train_df.dtypes}")
# All = int64, dtype: object

# Estadísticas descriptivas
pd.set_option('display.max_columns', None)
print("\n", train_df.describe())


