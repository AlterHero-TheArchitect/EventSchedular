from socket import *
import hashlib
import sqlite3
import threading

#serverIP = "127.0.0.1"
#serverIP = "localhost"
serverIP = "127.0.0.1"
serverPort = 65535
global login
login=False
thread_local = threading.local()
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen()
print('The server is ready to receive')


def handle_connection(c,login):

  while login==False:
        c.send("Username: ".encode())
        username = c.recv(1024).decode()
        print(username)
        c.send("Password: ".encode())
        password = c.recv(1024)
        password = hashlib.sha256(password).hexdigest()
        print(password)

        conn =sqlite3.connect("users.db")
        cur =conn.cursor()

        cur.execute("SELECT * FROM userdata WHERE username=? AND password=?",(username,password)) 

        if cur.fetchall():
                c.send("Login successful".encode())
                login=True
                break
 
        else:
                c.send("Login Failed".encode())
       

def booking(c,login):
    
    #if (login==False):
        c.send("NoOfSlots: ".encode())
        slots = c.recv(1024).decode()
        c.send("NoOfTickets: ".encode())
        tickets = c.recv(1024)
        c.send("Date: ".encode())
        date = c.recv(1024)


        conn =sqlite3.connect("BookingData.db")
        cur =conn.cursor()

        cur.execute("INSERT INTO UserBookingData (NoOfSlots, NoOfTickets, Date) VALUES (?, ?, ?)",
                (slots, tickets, date))
        conn.commit()
        cur.execute("SELECT * FROM UserBookingData WHERE NoOfSlots=? AND NoOfTickets=? AND Date=?",
                (slots, tickets, date))

        if cur.fetchone():
                c.send("Data has been stored".encode())
        else:
                c.send("Failed to store data".encode())
    






while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Client Address = {connectionSocket}")
    t1=threading.Thread(target=handle_connection, args=(connectionSocket,login))
    t1.start()
    t1.join()
    t2=threading.Thread(target=booking, args=(connectionSocket,login))
    t2.start()
    #threading.Thread(target=handle_connection, args=(connectionSocket,)).start()
    #sentence = connectionSocket.recv(2048)
    #print(("Login successful2".encode()))
    
    
    #connectionSocket.close()
