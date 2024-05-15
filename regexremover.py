import re

with open("data/2023-PSSD-York-University.csv", "r") as filein, open("data/2023-PSSD-York-University-output.csv", "w") as fileout:
    salary_pattern = r'\"(\d{1,3}(,\d{3})*\.\d{2})\"'
    for line in filein:
        salary_match = re.search(salary_pattern, line)
        if salary_match:
            salary = salary_match.group(1)
            salary = f"{float(salary.replace(',', ''))}"
            print(salary)
            line = re.sub(salary_pattern, salary, line)
        fileout.write(line)