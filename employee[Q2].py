import pandas as pd
file_path = "employee.csv"  
df = pd.read_csv(r"C:\Users\ARTHI\OneDrive\Documents\Query Processing\employee.csv")
job_counts = df.groupby('EMPLOYEE_ID')['JOB-ID'].nunique()
multiple_jobs = job_counts[job_counts >= 2]
print("Employee IDs who have had two or more jobs in the past:")
print(multiple_jobs.index)
