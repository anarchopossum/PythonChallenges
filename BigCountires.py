import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    data_filter = world[(world['population'] > 25000000) | (world['area'] > 3000000)][['name','population','area']]
    return data_filter

data = [
['Afghanistan', 'Asia',   652230,  25500100, 20343000000 ],
['Albania',     'Europe', 28748,   2831741,  12960000000 ],
['Algeria',     'Africa', 2381741, 37100000, 188681000000],
['Andorra',     'Europe', 468,     78115,    3712000000],
['Angola',      'Africa', 1246700, 20609294, 100990000000]]

world_data =  pd.DataFrame(data, columns=['name','continent','area','population','gdp'])
print("\n\nWorld Data:\n", world_data, "\n\nCountries with Large area or populations:\n")
print(big_countries(world_data))
