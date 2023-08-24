import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if ((x['employee_id'] % 2) != 0) and (x['name'][0] != 'M') else 0 , axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by="employee_id")

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})

print("Employees table:\n", Employees)
print("\n\nBonus table:\n", calculate_special_bonus(Employees))
