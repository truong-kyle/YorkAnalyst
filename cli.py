import time
import os
from config import dataloader
from rich import print

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
offline = "data/2023-PSSD-York-University-output.csv"
url = "https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/2023-PSSD-York-University-output.csv"
try: df = dataloader.load_data(url)
except Exception as e:
    print(e)
    exit()
print("Data loaded!")
time.sleep(1)
cls()
time.sleep(0.5)
while True:
    print("[red]York University Salary Data: 2023")
    print("==================================")
    print("1. [green]Display the first [red]X [green]rows")
    print("2. [green]Search")
    print("3. [red]Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        cls()
        rows = int(input("Enter number of rows to display, or [red]0 to exit: "))
        if (rows==0): 
            cls()
            continue
        print(df.head(rows))
        input("Press Enter to continue...")
        cls()
    elif choice == "2":
        cls()
        print(df.columns)
        column = input("Please select a column to search by: ")
        search = input("Enter search term: ")
        print(df[df['Position Title'].str.contains(search, case=False)])
    elif choice == "3":
        exit()
    else:
        print("Invalid choice!")
        input("Press Enter to continue...")
        cls()