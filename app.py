from flask import Flask, render_template, request, g
import sqlite3



app = Flask(__name__)
db = sqlite3.connect('salaries23.db')
@app.route('/', methods=['GET', 'POST'])


def index():
    if request.method == 'POST':
        pass
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)