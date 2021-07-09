import random
from setting import*
with open('userID') as f:
    userID = f.readlines()
with open('userPASSWORD') as f:
    userPASSWORD = f.readlines()
def sign_up(c,addr):
    while True:
        print(f"{addr}")
        c.send(b"hello")
        
        a = c.recv(1024)
        b = c.recv(1024)
        for line in userID:
            index = userID.index(line)
            temp = userPASSWORD[index]
            print(temp)

            if a == line.encode() :
                if b == temp.encode():

                    ui = random.choice(range(10000,99999))
                    ui =str(ui)
                    c.send(ui.encode())
                    with open(f'convensionID\{ui}','w') as f:
                        f.write(f"{ui}\n{line}")
                else:
                    c.send(b'402')
            else:
                c.send(b"401")