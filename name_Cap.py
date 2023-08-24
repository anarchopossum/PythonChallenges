import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(lambda x: '' + x[0].upper() + x[1:].lower())
    return users.sort_values(by='user_id')

data = [[1, 'aLice'], [2, 'bOB']]
Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

print("Users:\n", Users, )
print("\nFixed Names:\n", fix_names(Users))
