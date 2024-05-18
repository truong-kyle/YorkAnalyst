import time
import os
from config import dataloader
from rich import print
import pandas as pd

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_name(df, name):
    name = name.lower().split(" ")
    if len(name) == 1:
        result = df[df['First Name'].str.contains(name[0], case=False) | df['Last Name'].str.contains(name[0], case=False)]
    else:
        result = df[df['First Name'].str.contains(name[0], case=False) & df['Last Name'].str.contains(name[1], case=False)]
    return result if not result.empty else None

def load_data(offline, url):
    try:
        df = dataloader.load_data(url)
    except Exception as e:
        print(f"[red]Failed to load data from URL: {e}")
        print(f"[yellow]Loading data from local file: {offline}")
        try:
            df = dataloader.load_data(offline)
        except Exception as e:
            print(f"[red]Failed to load data from local file: {e}")
            exit()
    return df

def display_menu():
    print("[red]York University Salary Data: 2023")
    print("==================================")
    print("1. [green]Display the first [red]X [green]rows")
    print("2. [green]Search")
    print("3. [red]Exit")

def main():
    print("[blue]Loading data...")
    offline = "data/2023-PSSD-York-University-output.csv"
    url = "https://raw.githubusercontent.com/truong-kyle/YorkAnalyst/main/data/2023-PSSD-York-University-output.csv"
    df = load_data(offline, url)
    print("[blue]Data loaded!")
    time.sleep(1)
    cls()
    time.sleep(0.5)
    
    while True:
        cls()
        display_menu()
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
                        result = search_name(df, name)
                        print(result if result is not None else "No results found.")
                        input("Press Enter to continue...")
                        break
                    
                    elif option == 2:
                        position = input("Enter position title to search: ")
                        result = df[df['Position Title'].str.contains(position, case=False)]
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
                        
                        result = df[(df['Salary Paid'] >= min_salary) & (df['Salary Paid'] <= max_salary)]
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
