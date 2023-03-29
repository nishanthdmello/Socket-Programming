import socket
import pickle
from tkinter import *


def send(list_of_absentees):

    # Sending the attendance data to the server
    data = pickle.dumps(list_of_absentees)
    client_socket.send(data)

    # Receiving the server's response
    response = client_socket.recv(1024)

    # Printing the response
    print(response.decode())

    # Closing the socket
    client_socket.close()


def submit():

    list_of_absentees = ["p", "p", "p"]
    for i in range(3):
        if checkbox_variables[i].get() == 1:
            list_of_absentees[i] = "a"
    send(list_of_absentees)
    root.destroy()


# Creating the socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Getting local machine name and port number
host = "127.0.0.1"
port = 9999

# Connecting to the server
client_socket.connect((host, port))

# Receiving the srn's and unpickling it
data = client_socket.recv(1024)
data = pickle.loads(data)


root = Tk()
root.title("Attendance")
root.geometry("200x200")

l1 = Label(root, text="SRN")
l2 = Label(root, text="Absentees")
l1.grid(row=0, column=0)
l2.grid(row=0, column=1)

dn = IntVar()
na = IntVar()
nd = IntVar()

checkbox_variables = [dn, na, nd]

cb1 = Checkbutton(root, variable=checkbox_variables[0], onvalue=1, offvalue=0)
cb2 = Checkbutton(root, variable=checkbox_variables[1], onvalue=1, offvalue=0)
cb3 = Checkbutton(root, variable=checkbox_variables[2], onvalue=1, offvalue=0)
cb1.grid(row=1, column=1)
cb2.grid(row=2, column=1)
cb3.grid(row=3, column=1)

srn1 = Label(root, text=data[0])
srn2 = Label(root, text=data[1])
srn3 = Label(root, text=data[2])
srn1.grid(row=1, column=0)
srn2.grid(row=2, column=0)
srn3.grid(row=3, column=0)

but = Button(root, text="Submit", command=submit, font=("Helvetica", 12))
but.grid(row=4, rowspan=3, column=0, columnspan=2,pady=20)

mainloop()
