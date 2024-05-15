import pandas as pd 

url = "https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/2023-PSSD-York-University-output.csv"
df = pd.read_csv(url, header=None, names=['Last Name', 'First Name', 'Position Title', 'Salary Paid', 'Taxable Benefits'], na_values='-', on_bad_lines='warn')
df['Salary Paid'] = df['Salary Paid'].astype(float)
df['Taxable Benefits'] = df['Taxable Benefits'].astype(float)
print(df)