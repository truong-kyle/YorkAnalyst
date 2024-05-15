import re
def fix_salary(path:str):
    with open(path, "r") as filein, open(f'{path}.output', "w") as fileout:
        salary_pattern = r'\"(\d{1,3}(,\d{3})*\.\d*)\"'
        for line in filein:
            salary_match = re.search(salary_pattern, line)
            if salary_match:
                salary = salary_match.group(1)
                salary = f"{float(salary.replace(',', ''))}"
                print(salary)
                line = re.sub(salary_pattern, salary, line)
            fileout.write(line)

if __name__ == "__main__":
    fix_salary("data/2023-PSSD-York-University.csv")