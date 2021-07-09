import socket
from setting import *
from time import *
import threading
import sign_up
s = socket.socket()
s.bind((address,port))
s.listen(5)
while True:
    a,addr = s.accept()
    t = threading.Thread(target = sign_up.sign_up,args=(a,addr))
    t.start()
s.close()



    
