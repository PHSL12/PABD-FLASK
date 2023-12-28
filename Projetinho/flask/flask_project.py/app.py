# app.py
from flask import Flask, render_template
from database import get_books

app = Flask(__name__)

@app.route('/create')
def books_create():
    books = get_books()
    return render_template('create.html', books=books)

@app.route('/list')
def books_list():
    books = get_books()
    return render_template('create.html', books=books)

@app.route('/')
def books():
    books = get_books()
    return render_template('base.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
