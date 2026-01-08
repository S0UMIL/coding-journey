import pandas as pd
df=pd.read_csv("pokemon.csv")
# lets prinout pokemons with specific conditions
tall_pokemon=df[df["Height"]>=2]
print(tall_pokemon)
heavy_pokemon=df[df["Weight"]>95]
print(heavy_pokemon)
tall_n_heavy_pokemon=df[(df["Height"]>=2)&(df["Weight"]>95)]
print(tall_n_heavy_pokemon)
water_type_pokemon=df[df["Type1"]=="Water"]
print(water_type_pokemon)
legendary_pokemon=df[df["Legendary"]==True]
print(legendary_pokemon)
