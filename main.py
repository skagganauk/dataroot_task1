import socket
import sys
import os

HOST,PORT = '', 8000 
addr = (HOST, PORT) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')


try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print ('Socket bind complete')

s.listen(10)
print ('Socket now listening')

conn, addr = s.accept()
conn.recv(1024)

def handler():

    curr_dir = os.getcwd()
    index = 'index.html'
    file_list = os.listdir(path=".")

    if index in file_list:
        with open('index.html') as main_html:
            mainpage=main_html.read().replace('\n', '')
            conn.send(bytes(
                            "HTTP/1.1 200 OK\n"
                            +"Content-Type: text/html\n"
                            +"\n"
                            +mainpage, encoding='utf-8'))
            conn.close()

    else:
        #for dirName, subdirList, fileList in os.walk(rootDir):
        #conn.send(bytes(
                        #"HTTP/1.1 200 OK\n"
                        #+"Content-Type: text/html\n"
                        #+"\n"
                        #+

        curr_dir = os.getcwd()
        for dirName, subdirList, fileList in os.walk(curr_dir):



            print('Found directory: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)



while 1:
    handler()



s.close()
#s.serveforever()