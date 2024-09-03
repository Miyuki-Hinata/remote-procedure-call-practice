const net = require('net');

// Get command-line arguments
const args = process.argv.slice(2);

if(args.length < 2) {
  console.error('Usage: node client.js <method> <id> <param1> <param2> ...');
  process.exit(1);
} 

const method = args[0];
const id = args[1];
const params = args.slice(2).map(arg => {
  if(!isNaN(arg)) {
    return parseFloat(arg);
  } else {
    return arg;
  }
})

const param_types = params.map(param => typeof param)

const client = new net.Socket();
const request = {
    method: method, 
    params: params, 
    param_types: param_types,
    id: id
};

client.connect(12345, 'localhost', function() {
    console.log('Connected to server');
    client.write(JSON.stringify(request));
});

client.on('data', function(data) {
    console.log('Received: ' + data);
    client.destroy(); // kill client after server's response
});

client.on('close', function() {
    console.log('Connection closed');
});
