import sqlite3


conn=sqlite3.connect("BookingData.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS UserBookingData(
    id INTEGER PRIMARY KEY,
    NoOfSlots INT  NOT NULL,
    NoOfTickets INT  NOT NULL,
    Date VARCHAR(255)  NOT NULL
)""")




conn.commit()
