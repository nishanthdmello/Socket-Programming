import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port number
host = socket.gethostname()
port = 9999

# Bind socket to host and port
server_socket.bind((host, port))

# Listen for incoming client connections
server_socket.listen(5)

# Create an empty dictionary to store attendance data
attendance_data = {}

while True:
    # Wait for a client to connect
    client_socket, addr = server_socket.accept()
    print("Connection from : " + str(addr))

    # Receive attendance data from the client
    data = client_socket.recv(1024)

    # Check if the data is valid
    if data:
        # Parse the attendance data and store it in the dictionary
        student_id, attendance_status = data.decode().split(",")
        attendance_data[student_id] = attendance_status

        # Send a success response back to the client
        client_socket.send(b"Attendance successfully recorded.")
    else:
        # Send an error response back to the client
        client_socket.send(b"Invalid attendance data.")

    # Close the client connection
    client_socket.close()
