import socket
import piController

HOST = "192.168.86.103" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

car_control = piController.piController()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":               # Instruct the car to move in the direction as the input string
                print(data)     
                cmdHandle = car_control.directionHandle(data)
                if(data == b"INFO"):      # Retrieve the info and send the info to the client
                    print("cmdHandle: " + cmdHandle)
                    client.sendall(cmdHandle.encode())

    except: 
        print("Closing socket")
        client.close()
        s.close()    