import socket
import json
import math

# Define available methods
def floor(x, y):
    return x // y

def nroot(n, x):
    return x ** (1 / n)

def reverse(s):
    return s[::-1]

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sort(arr):
    return sorted(arr)

# Start the server and listen for client connections
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print(f"Server is listening on {server_address}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established!")
        handle_client(client_socket)

# Handle client communication (receiving, processing and responding)
def handle_client(client_socket):
    try:
        data = receive_data(client_socket)
        if data:
            request = parse_request(data)
            response = process_request(request)
            send_response(client_socket, response)
    finally:
        # Close the connection
        client_socket.close()


# Receiving data from the client
def receive_data(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")
    return data

# Parse the received JSON request
def parse_request(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return None

# Process the request and execute the corresponding method
def process_request(request):
    # Get method name, parameters, and ID
    method_name = request.get("method")
    params = request.get("params")
    request_id = request.get("id")

    # Find and execute the method
    if method_name in globals():
        method = globals()[method_name]
        try:
            result = method(*params)
            result_type = type(result).__name__
            return {
                "result": result,
                "result_type": result_type,
                "id": request_id
            }
        except Exception as e:
            return {
              "error": str(e),
              "id": request_id
            }
    else:
        response = {
            "error": "Method not found",
            "id": request_id
        }

# Send the response back to the client
def send_response(client_socket, response):
    client_socket.sendall(json.dumps(response).encode('utf-8'))

if __name__ == "__main__":
    start_server()
