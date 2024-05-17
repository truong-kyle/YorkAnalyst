import time
import os
from config import dataloader
from rich import print

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def search_name(df, name):
    name = name.lower()
    name = name.split(" ")
    if len(name) == 1:
        result = df[(df['First Name'].str.contains(name[0], case=False)) | (df['Last Name'].str.contains(name[0], case=False))]
    else:
        result = df[(df['First Name'].str.contains(name[0], case=False)) & (df['Last Name'].str.contains(name[1], case=False))]
    if result.empty:
        return None
    else:
        return result


print("[blue]Loading data...")

offline = "data/2023-PSSD-York-University-output.csv"
url = "https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/2023-PSSD-York-University-output.csv"
try:
    df = dataloader.load_data(url)
except Exception as e:
    print(e)
    exit()
print("[blue]Data loaded!")
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
        while True:
            try:
                rows = int(input("Enter number of rows to display, or 0 to exit: "))
                if rows == 0:
                    cls()
                    break
                print(df.head(rows))
                input("Press Enter to continue...")
                cls()
                break
            except ValueError:
                print("[red]Invalid input! Please enter a valid number.")
    elif choice == "2":
        cls()
        print("1. [green]Search by name")
        print("2. [green]Search by position title")
        print("3. [green]Search by salary range")
        print("4. [red]Back to main menu")
        while True:
            try:
                option = int(input("Enter your choice: "))
                if option == 1:
                    result = input("Enter name to search: ")
                    print(search_name(df, result))
                    input("Press Enter to continue...")
                    cls()
                    break
                elif option == 2:
                    result = input("Enter position title to search: ")
                    print(df[df['Position Title'].str.contains(result, case=False)])
                    input("Press Enter to continue...")
                    cls()
                    break
                elif option == 3:
                    while True:
                        try:
                            min_salary = float(input("Enter minimum salary: "))
                            max_salary = float(input("Enter maximum salary: "))
                            print(df[(df['Salary Paid'] >= min_salary) & (df['Salary Paid'] <= max_salary)])
                            input("Press Enter to continue...")
                            cls()
                            break
                        except ValueError:
                            input("[red]Invalid input! Please enter a valid number.")
                elif option == 4:
                    cls()
                    break
                else:
                    print("[red]Invalid choice!")
                    input("Press Enter to continue...")
                    cls()
            except ValueError:
                input("[red]Invalid input! Please enter a valid number.")
                cls()
    elif choice == "3":
        exit()
    else:
        print("[red]Invalid choice!")
        input("Press Enter to continue...")
        cls()