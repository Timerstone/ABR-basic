import socket
import netifaces as ni


def getHostName():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)

        print(host_name)
        print(host_ip)

        print("hi")
        ni.ifaddresses('eth0')
        print("something")
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        print(ip)
    except:
        print("cant get")


getHostName()
