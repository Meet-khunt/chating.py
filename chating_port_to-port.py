import socket


s=socket.socket()

while True:
    try:
        s.bind(("192.168.___.__",8888))
        break
    except ConnectionRefusedError:
     pass
     print("connect")




s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.listen(1)

client,addr=s.accept()

print('connected')




while True:
  

  cmd=input(" ")

  client.send (cmd .encode())

  if cmd=="q":
    break
  recv=client.recv((1024)).decode()

  print(recv)

  client.close
  s.close
