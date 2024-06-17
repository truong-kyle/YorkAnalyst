import sqlite3
from config.dataloader import load_data
## Rebuild the databases from the contents of the CSV files
def build_db(year):
    url = f"https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/20{year}-PSSD-York-University-output.csv"
    dataframe = load_data(url)
    print(dataframe)
    dataframe.to_sql('salaries'+str(year), sqlite3.connect(f'salaries{year}.db'), if_exists='replace', index=False)

if __name__ == "__main__":
    build_db(23)