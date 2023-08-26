import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    filter = store[store['amount'].apply(lambda x: x > 500)]['customer_id'].nunique()
    return pd.DataFrame(data={'rich_count': [filter]})

data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
Store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})
print ("Recipt List:\n",Store)
print ("Rich People:\n",count_rich_customers(Store))
