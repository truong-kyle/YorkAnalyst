import time
import os
from setup import dataloader
from rich import print

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def search_name(df, name):
    #input is a dataframe and name, but name can be first name, last name or both. need to match specific cases
    #return the row that matches the name
    #if no match, return None
    name = name.lower()
    name = name.split(" ")
    if len(name) == 1:
        #search for first name or last name
        result = df[(df['First Name'].str.contains(name[0], case=False)) | (df['Last Name'].str.contains(name[0], case=False))]
    else:
        #search for both first name and last name
        result = df[(df['First Name'].str.contains(name[0], case=False)) & (df['Last Name'].str.contains(name[1], case=False))]
    if result.empty:
        return None
    else:
        return result


print("Loading data...")

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
    print("York University Salary Data: 2023")
    print("==================================")
    print("1. Display the first X rows")
    print("2. Search")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        rows = int(input("Enter number of rows to display: "))
        print(df.head(rows))
        input("Press Enter to continue...")
        cls()
    elif choice == "2":
        result = input("Enter name to search: ")
        print(search_name(df, result))
        input("Press Enter to continue...")
    elif choice == "3":
        exit()
    else:
        print("Invalid choice!")
        input("Press Enter to continue...")
        cls()