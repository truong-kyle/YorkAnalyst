from reader import load_data
from os import remove, path
import pandas as pd
import numpy as np

if not(path.isfile("output.csv")):
    load_data()

df = pd.read_csv("output.csv", header=None, names=['Last Name', 'First Name', 'Position Title', 'Salary Paid', 'Taxable Benefits'], na_values='-', on_bad_lines='warn')
df['Salary Paid'] = df['Salary Paid'].str.replace(",","").astype(float)
df['Taxable Benefits'] = df['Taxable Benefits'].str.replace(" ", "").str.replace(",","").astype(float)
print(df)