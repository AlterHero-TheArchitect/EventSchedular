from socket import *
from tkinter import *

loginpass = False
serverIP = "127.0.0.1"
serverPort = 65535
client = socket(AF_INET, SOCK_STREAM)
client.connect((serverIP, serverPort))

root = Tk()
root.title("Client GUI")

def send_login():
    global loginpass
    message = client.recv(1024).decode()
    client.send(entry.get().encode())
    message2 = client.recv(1024).decode()
    client.send(entry2.get().encode())
    ans = client.recv(1024).decode()
    output_text.insert(END, ans + "\n")
    if "Login successful" in ans:
        loginpass = True

def send_booking():
    if loginpass:
        message3 = client.recv(1024).decode()
        client.send(entry3.get().encode())
        message4 = client.recv(1024).decode()
        client.send(entry4.get().encode())
        message5 = client.recv(1024).decode()
        client.send(entry5.get().encode())
        ans = client.recv(1024).decode()
        output_text.insert(END, ans + "\n")


# Create GUI components
label = Label(root, text="Enter Username:")
label.pack()

entry = Entry(root)
entry.pack()

label2 = Label(root, text="Enter Password:")
label2.pack()

entry2 = Entry(root)
entry2.pack()

button = Button(root, text="Login", command=send_login)
button.pack()

output_text = Text(root, width=50, height=10)
output_text.pack()

# Additional GUI components for booking
label3 = Label(root, text="No. of Slots:")
label3.pack()

entry3 = Entry(root)
entry3.pack()

label4 = Label(root, text="No. of Tickets:")
label4.pack()

entry4 = Entry(root)
entry4.pack()

label5 = Label(root, text="Date:")
label5.pack()

entry5 = Entry(root)
entry5.pack()

button2 = Button(root, text="Book", command=send_booking)
button2.pack()

root.mainloop()
