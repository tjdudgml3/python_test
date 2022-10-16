import socket

in_addr = socket.gethostbyname(socket.gethostname())  #gehostname 서버의 이름을 hostname이라고 하지만 pc이름을 hostname이라고도 한다. 
                                                        #gethostbyname 이름을 가지고 뽑아내기

print(in_addr)
