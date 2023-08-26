# 1173. food_delivery I
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_count = delivery[delivery['order_date'] == delivery ['customer_pref_delivery_date']]
    return pd.DataFrame(data={'immediate_percentage':[round(len(immediate_count) * 100 / len(delivery), 2)]})

data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 5, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-11'], [4, 3, '2019-08-24', '2019-08-26'], [5, 4, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13']]
Delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})
print('Food Orders:\n',Delivery)
print('Immediate Order Percentage:\n',food_delivery(Delivery))
