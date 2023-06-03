import sqlite3
import hashlib

conn=sqlite3.connect("users.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)""")

username1,password1 ="hero" ,hashlib.sha256("alterhero".encode()).hexdigest()
username2,password2 ="Max" ,hashlib.sha256("Payne".encode()).hexdigest()
username3,password3 ="Jack" ,hashlib.sha256("Slate".encode()).hexdigest()

cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username1,password1))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username2,password2))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username3,password3))

conn.commit()
