import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = (accounts['income'] < 20000).sum()
    mid = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    hig = (accounts['income'] > 50000).sum()

    return pd.DataFrame(data={'category': ['Low Salary','Average Salary','High Salary'], 'accounts_count': [low,mid,hig]})

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})
print('data:\n', Accounts)
print('results:\n',count_salary_categories(Accounts))
