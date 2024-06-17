import os, time
from tools.load import load_data
from rich import print
import pandas as pd
import tools.search as search

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(year: int):
    print(f"[red]York University Salary Data: 20{year}")
    print("==================================")
    print("1. [green]Display the first [red]X [green]rows")
    print("2. [green]Search")
    print("3. [red]Exit")

def main():
    try :
        year = int(input("Please select a year (21, 22, 23): "))
        if year == 21:
            print("You selected 2021")
        elif year == 22:
            print("You selected 2022")
        elif year == 23:
            print("You selected 2023")
        else:
            print("Invalid year")
    except ValueError:
        print("Invalid input! Please enter a valid option.")
        return
    print("[blue]Loading data...")
    offline = f"data/20{year}-PSSD-York-University-output.csv"
    url = f"https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/20{year}-PSSD-York-University-output.csv"
    df = load_data(offline, url)
    print("[blue]Data loaded!")
    time.sleep(1)
    cls()
    time.sleep(0.5)
    
    while True:
        cls()
        display_menu(year)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            cls()
            while True:
                try:
                    rows = int(input("Enter number of rows to display, or 0 to exit: "))
                    if rows == 0:
                        break
                    print(df.head(rows))
                    input("Press Enter to continue...")
                    break
                except ValueError:
                    print("[red]Invalid input! Please enter a valid option.")
        
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
                        name = input("Enter name to search: ")
                        result = search.name(name, df)
                        print(result if result is not None else "No results found.")
                        input("Press Enter to continue...")
                        break
                    
                    elif option == 2:
                        position = input("Enter position title to search: ")
                        result = search.position(position, df)
                        print(result if not result.empty else "No results found.")
                        input("Press Enter to continue...")
                        break
                    
                    elif option == 3:
                        while True:
                            try:
                                min_salary = float(input("Enter minimum salary: "))
                                break
                            except ValueError:
                                print("[red]Invalid input! Please enter a valid option.")
                        
                        while True:
                            try:
                                max_salary = float(input("Enter maximum salary: "))
                                break
                            except ValueError:
                                print("[red]Invalid input! Please enter a valid option.")
                        
                        result = search.salary(min_salary, max_salary, df)
                        print(result if not result.empty else "No results found.")
                        input("Press Enter to continue...")
                        break
                    
                    elif option == 4:
                        break
                    else:
                        print("[red]Invalid choice!")
                        input("Press Enter to continue...")
                except ValueError:
                    print("[red]Invalid input! Please enter a valid option.")
        
        elif choice == "3":
            break
        
        else:
            print("[red]Invalid input! Please enter a valid option.")

if __name__ == "__main__":
    main()
