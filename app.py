from flask import Flask, render_template, request
from stroke import get_table, get_table_by_search

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize year variable
    year = 23  # Default year

    if request.method == 'POST':
        # Update year based on form input
        year = request.form['year'] if request.form.get('year') else year
        lname = request.form['lname']
        fname = request.form['fname']
        title = request.form['position']
        min_sal = request.form['minsal']
        max_sal = request.form['maxsal']
        data = get_table_by_search(year, lname, fname, title, min_sal, max_sal)
    else:
        # Fetch data for the default year
        data = get_table(year)

    count = len(data)
    return render_template('index.html', results=data, year=year, count=count)

if __name__ == "__main__":
    app.run()