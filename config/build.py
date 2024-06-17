import sqlite3
from dataloader import load_data
## Rebuild the databases from the contents of the CSV files
def build_db(year):
    url = f"https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/20{year}-PSSD-York-University-output.csv"
    dataframe = load_data(url)
    print(dataframe)
    dataframe.to_sql('salaries', sqlite3.connect(f'db/salaries{year}.db'), if_exists='replace', index=False)

if __name__ == "__main__":
    build_db(23)