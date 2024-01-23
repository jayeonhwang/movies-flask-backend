import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    with connect_to_db() as conn:
      conn = connect_to_db()
      conn.execute(
          """
          DROP TABLE IF EXISTS movies;
          """
      )
      conn.execute(
          """
          CREATE TABLE movies (
            id INTEGER PRIMARY KEY NOT NULL,
            title TEXT,
            director TEXT,
            genre TEXT,
            runtime INTEGER,
            rating INTEGER
          );
          """
    )
    conn.commit()
    print("Table created successfully")

    movies_seed_data = [
        ("Oppenheimer", "Christopher Nolan", "historical drama", 180, 9),
        ("Barbie", "Greta Gerwing", "adventure/comedy", 154, 8),
    ]
    conn.executemany(
        """
        INSERT INTO movies (title, director, genre, runtime, rating)
        VALUES (?,?,?,?,?)
        """,
        movies_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()

def initialize_database():
    initial_setup()

if __name__ == "__main__":
    initialize_database()

def movies_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM movies
        """
    ).fetchall()
    return [dict(row) for row in rows]


def movies_create(title, director, genre , runtime, rating):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO movies (title, director, genre , runtime, rating)
        VALUES ( ?, ?, ?, ?, ? )
        RETURNING *
        """,
        (title, director, genre , runtime, rating),
    ).fetchone()
    conn.commit()
    return dict(row)

def movies_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM movies
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)

def movies_update_by_id (id, title, director, genre , runtime, rating):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE movies SET title = ?, director = ?, genre = ? , runtime = ?,rating = ?
        WHERE id = ?
        RETURNING *
        """,
        (title, director, genre , runtime, rating, id),
    ).fetchone()
    conn.commit()
    return dict(row)

def movies_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from movies
        WHERE id = ?
        """,
        id,
    )
    conn.commit()
    return {"message": "Movies destroyed successfully"}