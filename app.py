from flask import Flask, render_template, request
import search
from load import load_data
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        first = request.form['fname']
        search.first(first, df)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)