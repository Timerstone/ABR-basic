import socket
import errno

HEADER_LENGTH = 10

host = input("Enter IP: ")
port = int(input("Enter Port Number: "))
clientname = input("Client Name: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.setblocking(False)

username = clientname.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
s.send(username_header + username)

def receiveMessage():
    try:
        message_header = s.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': s.recv(message_length)}

    except:
        return False

def sendMessage(message):
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        s.send(message_header + message)

    try:
        while True:
            username_header = s.recv(HEADER_LENGTH)

            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = s.recv(username_length).decode('utf-8')

            message_header = s.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = s.recv(message_length).decode('utf-8')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()

def commands(args):
    if args == 1:
        captureData()
    elif args == 2:
        terminate()

def waitAction():
    print("Awaiting command...")
    commands(int(receiveMessage()))

def captureData():
    print("Capturing data...")

def terminate():
    print("Terminating connection...")
    sendMessage("Terminating")
    s.close()

def Main():
    while True:
        waitAction()

if __name__ == '__main__':
    Main()