import socket
from setting import *
from time import*
def up():
    s = socket.socket()
    s.connect((address,port))
    print(s.recv(1024).decode("utf-8"))
    print("输入你的账号")
    ID = input()

    print("输入你的密码")
    PASSWORD = input()

    s.send(ID.encode())
    s.send(PASSWORD.encode())
    ui = s.recv(1024).decode('utf-8')
    s.close()
    return int(ui)
