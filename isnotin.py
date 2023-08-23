import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    '''
     # merge both tables and use the right table (customers) to compare
    output = orders.merge(customers, left_on='customerId', right_on='id', how='right')
     # grab all the values that have N/A on column 'customerId' and only keep column 'name'
    output = output[output.customerId.isna()][['name']]
     # Renames the 'name' to 'Customers'
    output = output.rename(columns={'name' : 'Customers'})
    '''


    '''
    Redo using isin(). We are using '~' to flip the 'isin()' to find all the values that are not in the orders'customerId'.
    Next we say we only want to keep the column 'name'. and finally change the column title from 'name' to 'Customers'
    '''
    output = customers[~customers.id.isin(orders['customerId'])][['name']].rename(columns={'name' : 'Customers'})
    return output


data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

print("\n\nCustomer Table:\n", Customers)
print("\n\nOrders Table:\n", Orders)
print ("\n\n Customers who didn't buy items:\n", find_customers(Customers, Orders))
