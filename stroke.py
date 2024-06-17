import sqlite3

def get_table(year: int):
    con = sqlite3.connect('db/salaries'+str(year)+'.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM salaries")
    results = cur.fetchall()
    con.close()
    return results

def get_table_by_search(year: int, lname: str, fname: str, title: str, min_sal: int, max_sal: int):
    con = sqlite3.connect('db/salaries'+str(year)+'.db')
    cur = con.cursor()
    que = []

    if lname:
        que.append(f"[Last Name] LIKE '{lname}%'")
    if fname:
        que.append(f"[First Name] LIKE '{fname}%'")
    if title:
        que.append(f"[Position Title] LIKE '%{title}%'")
    if min_sal:
        que.append(f"[Salary Paid] >= {min_sal}")
    if max_sal:
        que.append(f"[Salary Paid] <= {max_sal}")
    
    if que:
        query = "SELECT * FROM salaries WHERE " + " AND ".join(que)
    else:
        query = "SELECT * FROM salaries"
    cur.execute(query)
    results = cur.fetchall()
    con.close()
    return results