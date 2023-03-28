import socket
import csv
import pickle

# Get srns from file
csv_file = open("Data.csv", "r")
csv_reader = csv.reader(csv_file)
data = next(csv_reader)
csv_file.close()
data = pickle.dumps(data)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port number
host = "127.0.0.1"
port = 9999

# Bind socket to host and port
server_socket.bind((host, port))

# Listen for incoming client connections
server_socket.listen(5)

while True:

    # Wait for a client to connect
    client_socket, addr = server_socket.accept()
    print("Connection from : " + str(addr))

    # Send srns of students
    client_socket.send(data)

    # Receive attendance data from the client
    attendance_data = client_socket.recv(1024)
    attendance_data = pickle.loads(attendance_data)

    # Write to csv file
    csv_file = open("Data.csv", "a")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(attendance_data)
    csv_file.close()

    # Send a success response back to the client
    client_socket.send(b"Attendance successfully recorded.")

    # Close the client connection
    client_socket.close()
