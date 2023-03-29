import socket
import csv
import pickle

# Getting srn's from file and pickling it
csv_file = open("Data.csv", "r")
csv_reader = csv.reader(csv_file)
data = next(csv_reader)
csv_file.close()
data = pickle.dumps(data)

# Creating a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Getting local machine name and port number
host = "127.0.0.1"
port = 9999

# Binding socket to host and port
server_socket.bind((host, port))

# Listening for incoming client connections
server_socket.listen(5)

while True:

    # Waiting for a client to connect
    client_socket, addr = server_socket.accept()
    print("Connection from : " + str(addr))

    # Sending srn's of students
    client_socket.send(data)

    # Receiving attendance data from the client
    attendance_data = client_socket.recv(1024)
    attendance_data = pickle.loads(attendance_data)

    # Writing to csv file
    csv_file = open("Data.csv", "a")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(attendance_data)
    csv_file.close()

    # Sending a success response back to the client
    client_socket.send(b"Attendance successfully recorded.")

    # Closing the client connection
    client_socket.close()
