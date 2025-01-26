import socket

host = socket.gethostbyname(socket.gethostname()) # it's the local ip address of the computer and make sure not to use it if you're using virtual meachine
HOST = str(host)
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

client, address = server.accept()
print(f"Connected to {address}")

done = False

while not done:
  message = client.recv(1024).decode('utf-8')
  if message == 'quit':
    done == True
    client.close()
  else:
    print(f'Client: {message}')

  client.send(input("Server: ").encode('utf-8'))

  
