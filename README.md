# Python Socket Server for Method Execution

This project implements a Python socket server that listens for incoming connections and allows clients to execute predefined methods remotely. The server receives requests in JSON format, processes the request, executes the desired method, and returns the result.

## Features
The server supports the following methods:
- `floor(x, y)` - Performs floor division of `x` by `y`.
- `nroot(n, x)` - Returns the n-th root of `x`.
- `reverse(s)` - Reverses the input string `s`.
- `validAnagram(str1, str2)` - Checks if two strings are anagrams.
- `sort(arr)` - Sorts an array.

## How It Works
1. The server listens for incoming client connections on `localhost:12345`.
2. Clients send JSON requests containing the method name, parameters, and request ID.
3. The server processes the request, executes the corresponding method, and sends back the result.

### Request Format
A client should send a JSON object in the following format:
```json
{
  "method": "method_name",
  "params": [param1, param2, ...],
  "id": "unique_request_id"
}

### Example Request
{
  "method": "floor",
  "params": [10, 3],
  "id": "request_1"
}
### Example Response

{
  "result": 3,
  "result_type": "int",
  "id": "request_1"
}

### How to Run the Server
Clone this repository.

Run the following command to start the server:
python3 server.py

The server will start listening on localhost:12345.

Using the Node.js Client
You can use the provided client.js file to send requests to the server. The client can take command-line arguments to dynamically construct the request.

Running the Client
Ensure that the server is running.
Run the following command to send a request to the server using the client:
node client.js <method> <id> <param1> <param2> ...

For example, to calculate the floor division of 10 by 3 with the request ID req1, you would run:
node client.js floor req1 10 3

This sends a request to execute the floor method on the server with parameters 10 and 3, and the server responds with the result.

Client Explanation
<method>: The name of the method to call (e.g., floor, nroot, reverse, etc.).
<id>: A unique ID for the request (e.g., req1).
<param1> <param2> ...: The parameters to pass to the method. Numbers are automatically parsed, and strings are sent as-is.

The client will receive the server's response and display it in the terminal.