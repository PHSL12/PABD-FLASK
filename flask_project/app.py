# app.py
from flask import Flask, render_template, redirect, url_for, request
from database import get_books, create_book, update_book, remove_book, get_book_by_id

app = Flask(__name__)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        autor = request.form["autor"]
        year = request.form["year"]
        gender = request.form["gender"]
        create_book(title, autor, year, gender)
        return redirect(url_for("books_list"))
    return render_template("create.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    book = get_book_by_id(id)
    print(book)
    if request.method == "POST":
        title = request.form["title"]
        autor = request.form["autor"]
        year = request.form["year"]
        gender = request.form["gender"]
        update_book(id, title, autor, year, gender)
        return redirect(url_for("books_list"))
    return render_template("update.html", book=book)


@app.route("/remove/<int:id>", methods=["GET", "POST"])
def remove(id):
    remove_book(id)
    return redirect(url_for("books_list"))


@app.route("/")
def books_list():
    books = get_books()
    print(books)
    return render_template("index.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)
