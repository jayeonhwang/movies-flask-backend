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
       CREATE TABLE movies(
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT,
        director TEXT,
        genre TEXT,
        runtime INTEGER,
        rating INTEGER,
        image TEXT
      );
      """
    )

    conn.execute("DROP TABLE IF EXISTS users;")
    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT,
            email TEXT,
            password TEXT
        );
    """)
    



















    conn.execute(
        """
        DROP TABLE IF EXISTS reviews
        """
    )
    conn.execute(
        """
        CREATE TABLE reviews (
            id INTEGER PRIMARY KEY NOT NULL,
            user_id INTEGER,
            movie_id INTEGER, 
            review TEXT,
            FOREIGN KEY (movie_id) REFERENCES movies (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
    )

    conn.commit()
    print("Table created successfully")

    movies_seed_data = [
        ("Oppenheimer", "Christopher Nolan", "Historical Drama", 180, 9, "https://m.media-amazon.com/images/I/71lqDylcvGL._AC_UF894,1000_QL80_.jpg"),
        ("Barbie", "Greta Gerwing", "Adventure/Comedy", 154, 8, "https://i.ebayimg.com/images/g/lzMAAOSwDMRkxPxb/s-l1200.webp"),
        ("Past Lives", "Celine Song", "Romance/Drama", 106, 10, "https://www.movieposters.com/cdn/shop/products/scan003_70663bc2-b396-4858-84b9-eedbe2d4abfe_480x.progressive.jpg?v=1681920012"),
        ("Poor Things", "Yorgos Lanthimas", "Comedy/Fantasy", 141, 9, "https://m.media-amazon.com/images/I/71j0SXKUc-L._AC_UF894,1000_QL80_.jpg"),
        ("American Fiction", "Cord Jefferson", "Comedy/Drama", 117, 8, "https://www.movieposters.com/cdn/shop/files/american_fiction_510x.jpg?v=1699377938"),
        ("Zone of Interest", "Jonathan Glazer", "War/Crime", 106, 9, "https://m.media-amazon.com/images/M/MV5BYzRmOGQwZjktYjM2Ni00M2NmLWFlZDYtZGFhM2RkM2VhZDI1XkEyXkFqcGdeQXVyMTM1NjM2ODg1._V1_.jpg")

    ]
    conn.executemany(
        """
        INSERT INTO movies (title, director, genre, runtime, rating, image)
        VALUES (?,?,?,?,?,?)
        """,
        movies_seed_data,
    )


    users_seed_data = [
        ("user1", "user1@email.com", "password"),
        ("user2", "user2@email.com", "password"),
        ("user3", "user3@email.com", "password")
      ]
    
    conn.executemany(
        """
        INSERT INTO users (name, email, password)
        VALUES (?,?,?)
        """,
        users_seed_data,
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


def movies_create(title, director, genre , runtime, rating):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO movies (title, director, genre , runtime, rating, image)
        VALUES ( ?, ?, ?, ?, ?, ? )
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

def movies_update_by_id (id, title, director, genre , runtime, rating, image):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE movies SET title = ?, director = ?, genre = ? , runtime = ?,rating = ?, image = ?
        WHERE id = ?
        RETURNING *
        """,
        (title, director, genre , runtime, rating, id, image),
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

def users_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM users
        """
        ).fetchall()
    return [dict(row) for row in rows]

    
def users_create(name, email, password):
    conn = connect_to_db()
    row = conn.execute(
      """
      INSERT INTO users (name, email, password)
      VALUES (?, ?, ?)
      RETURNING *
      """,
      (name, email, password),
    ).fetchone()
    conn.commit()
    return dict(row)

def users_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM users
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)

def users_update_by_id(id, name,email,password):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE users SET name = ?, email = ?, password = ?
        WHERE id = ?
        RETURNING *
        """,
        (name, email, password, id),
    ).fetchone()
    conn.commit()
    return dict(row)


def users_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from users
        WHERE id = ?
        """,
        id,
    )
    conn.commit()
    return {"message": "user destroyed successfully"}

def reviews_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM reviews
        """
        ).fetchall()
    return [dict(row) for row in rows]

    
def reviews_create(user_id, movie_id, review):
    conn = connect_to_db()
    row = conn.execute(
      """
      INSERT INTO reviews (user_id, movie_id, review)
      VALUES (?, ?, ?)
      RETURNING *
      """,
      (user_id, movie_id, review),
    ).fetchone()
    conn.commit()
    return dict(row)

def reviews_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM reviews
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)

def reviews_update_by_id(id, user_id, movie_id, review):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE reviews SET user_id = ?, movie_id = ?, review = ?
        WHERE id = ?
        RETURNING *
        """,
        (user_id, movie_id, review, id),
    ).fetchone()
    conn.commit()
    return dict(row)


def reviews_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from reviews
        WHERE id = ?
        """,
        id,
    )
    conn.commit()
    return {"message": "review destroyed successfully"}

