import socket

HOST = '192.168.10.183'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

done = False

while not done:
  client.send(input('Client: ').encode('utf-8'))
  message = client.recv(1024).decode('utf-8')
  if message == "quit":
    done = True
    break
  print(f'Server: {message}')
  
