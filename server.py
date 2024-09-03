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

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print(f"Server is listening on {server_address}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established!")

    # Receive data
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")

    # Parse JSON data
    request = json.loads(data)

    # Get method name, parameters, and ID
    method_name = request.get("method")
    params = request.get("params")
    param_types = request.get("param_types")
    request_id = request.get("id")

    # Find and execute the method
    if method_name in globals():
        method = globals()[method_name]
        result = method(*params)
        result_type = type(result).__name__

        # Prepare the response
        response = {
            "result": result,
            "result_type": result_type,
            "id": request_id
        }
    else:
        response = {
            "error": "Method not found",
            "id": request_id
        }

    # Send response
    client_socket.sendall(json.dumps(response).encode('utf-8'))

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_server()
