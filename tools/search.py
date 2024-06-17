import pandas as pd

def name(name: str, df: pd.DataFrame):
    name = name.split(" ")
    if len(name) == 1:
        result = df[df['First Name'].str.contains(name[0], case=False) | df['Last Name'].str.contains(name[0], case=False)]
    else:
        result = df[df['First Name'].str.contains(name[0], case=False) & df['Last Name'].str.contains(name[1], case=False)]
    return result if not result.empty else None

def first(name: str, df: pd.DataFrame):
    result = df[df['First Name'].str.contains(name, case=False)]
    return result if not result.empty else None

def last(name: str, df: pd.DataFrame):
    result = df[df['Last Name'].str.contains(name, case=False)]
    return result if not result.empty else None 

def position(position: str, df: pd.DataFrame):
    result = df[df['Position Title'].str.contains(position, case=False)]
    return result if not result.empty else None

def salary(min_salary: float, max_salary: float, df: pd.DataFrame):
    result = df[(df['Salary Paid'] >= min_salary) & (df['Salary Paid'] <= max_salary)]
    return result if not result.empty else None
