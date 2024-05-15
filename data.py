from reader import load_data
from os import remove, path
import pandas as pd

if not(path.isfile("output.csv")):
    load_data()

df = pd.read_csv("output.csv", header=None, names=['Calendar Year', 'Sector', 'Last Name', 'First Name', 'Position Title', 'Organization', 'Salary Paid', 'Taxable Benefits'])
df
