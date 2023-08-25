import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains('\sDIAB1|^DIAB1',0)]

data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], 
        [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
Patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})

print("Patient info:\n", Patients)
print("\nPatients with Diabetes:\n", find_patients(Patients))
