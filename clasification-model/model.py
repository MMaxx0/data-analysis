import pandas as pd
import zipfile

# ZIP route
zip_path = "poker+hand.zip"

# Cols
cols = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','hand']

with zipfile.ZipFile(zip_path) as z:
    with z.open("poker-hand-training-true.data") as f:
        train_df = pd.read_csv(f, names=cols)
    with z.open("poker-hand-testing.data") as f:
        test_df = pd.read_csv(f, names=cols)

# Revisar
print("\n",train_df.head())
print("\n", test_df.head())
