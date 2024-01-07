# app.py
from flask import Flask, render_template
from database import get_books, create_book, update_book, remove_book, get_book_by_id

app = Flask(__name__)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        create_book(nome, data_inicio, data_fim)
        return redirect(url_for('books_list'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    book = get_book_by_id(id)
    print(book)
    if request.method == 'POST':
        nome = request.form['nome']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        update_book(id, nome, data_inicio, data_fim)
        return redirect(url_for('_list'))
    return render_template('update.html', book=book)

@app.route('/remove/<int:id>', methods=['GET', 'POST'])
def remove(id):
    remove_book(id)
    return redirect(url_for('books_list'))

@app.route('/')
def books_list():
    books = get_books()
    print(books)
    return render_template('index.html', books=books)
