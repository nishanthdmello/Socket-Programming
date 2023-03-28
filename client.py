import socket
import pickle

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port number
host = "127.0.0.1"
port = 9999

# Connect to the server
client_socket.connect((host, port))

# Receive the srns
data = client_socket.recv(1024)
data = pickle.loads(data)

# Prompt the user for attendance data
attendance_status = []
for i in data:
    print("Is",i, end=" ")
    attendance = input("(P or A) : ")
    attendance_status.append(attendance)

# Send the attendance data to the server
data = pickle.dumps(attendance_status)
client_socket.send(data)

# Receive the server's response
response = client_socket.recv(1024)

# Print the response
print(response.decode())

# Close the socket
client_socket.close()
