import pandas as pd
df=pd.read_csv("pokemon.csv",index_col="Name")
pokemon=input("enter the name of pokemon:")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} was not found")