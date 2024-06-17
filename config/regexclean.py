import re
def fix_salary(path:str):
    with open(path, "r") as filein, open(f'{path}.output', "w") as fileout:
        salary_pattern = r'\"(\d{1,3}(,\d{1,3})*\.\d*)\"'
        for line in filein:
            salary_match = re.search(salary_pattern, line)
            if salary_match:
                salary = salary_match.group(1)
                salary = f"{float(salary.replace(',', ''))}"
                print(salary)
                line = re.sub(salary_pattern, salary, line)
            fileout.write(line)

def del_last_commas(path:str):
    with open(path, "r") as filein, open(f'{path}.output', "w") as fileout:
        for line in filein:
            linelist = line.split()
            if linelist[-1][-1] == ',':
                linelist[-1] = linelist[-1][:-1]
            fileout.write(" ".join(linelist) + '\n')

if __name__ == "__main__":
    fix_salary("config/2021-PSSD-York-University.csv")