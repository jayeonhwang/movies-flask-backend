import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
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


if __name__ == "__main__":
    initial_setup()

def movies_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM movies
        """
    ).fetchall()
    return [dict(row) for row in rows]


def movies_create(title,director, genre , runtime, rating):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO movies (title,director, genre , runtime, rating)
        VALUES ( ?, ?, ?, ?, ? )
        RETURNING *
        """,
        (id. title, director, genre , runtime, rating),
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