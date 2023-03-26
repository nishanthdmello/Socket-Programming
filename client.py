import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port number
host = socket.gethostname()
port = 9999

# Connect to the server
client_socket.connect((host, port))

# Prompt the user for attendance data
student_id = input("Enter student ID : ")
attendance_status = input("Enter attendance status (P or A) : ")

# Send the attendance data to the server
data = student_id + "," + attendance_status
client_socket.sendall(data.encode())

# Receive the server's response
response = client_socket.recv(1024)

# Print the response
print(response.decode())

# Close the socket
client_socket.close()
