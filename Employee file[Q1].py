import pandas as pd
employees = pd.read_csv(r"C:\Users\ARTHI\OneDrive\Documents\Query Processing\Employee_file.csv")
distinct_department_ids = employees['DEPATMENT-ID'].unique()
print(distinct_department_ids)
