import psycopg2
from psycopg2 import sql


DB_NAME = "books_database"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"


def conectar_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )


def criar_db():
    def conectar_servidor():
        return psycopg2.connect(
            dbname="postgres",
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
    conn = conectar_servidor()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
    cursor.close()
    conn.close()



def criar_tabelas(sql):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)



def insert_book(book_id, book_title, book_autor, book_year, book_gender):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO books (id, title, autor, year, gender) VALUES (%s, %s, %s, %s, %s)", 
                (book_id, book_title, book_autor, book_year, book_gender)
            )
            conn.commit()


def get_books():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
    SELECT id, title, autor, year, gender
    FROM books
    """)
    books = cur.fetchall()
    cur.close()
    conn.close()
    return books

def create_books():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
    INSERT books id, title, autor, year, gender
    Values
    """)
    books = cur.fetchall()
    cur.close()
    conn.close()
    return books



if __name__ == "__main__":
    # criar_db()

    sql_create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id integer PRIMARY KEY,
        title text NOT NULL,
        autor text NOT NULL,
        year integer NOT NULL,
        gender text NOT NULL
    );"""
    
    criar_tabelas(sql_create_books_table)

    #insert_book(1, "Confissões", "Santo Agostinho", 397, "Teologia")
    insert_book(2, "A Revolta de Atlas", "Ayn Rand", 1957, "Filosofia")
