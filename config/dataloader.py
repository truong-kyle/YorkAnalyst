import pandas as pd 
import sqlite3

def load_data(url:str):
    df = pd.read_csv(url, header=None, names=['Last Name', 'First Name', 'Position Title', 'Salary Paid', 'Taxable Benefits'], na_values='-', on_bad_lines='warn')
    df['Salary Paid'] = df['Salary Paid'].astype(float)
    df.drop(labels=['Taxable Benefits'], axis=1, inplace=True)
    df.fillna(0, inplace=True)
    pd.set_option('display.max_rows', None)
    return df

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/2023-PSSD-York-University-output.csv"
    dataframe = load_data(url)
    print(dataframe)
    dataframe.to_sql('salaries23', sqlite3.connect('salaries.db'), if_exists='replace', index=False)