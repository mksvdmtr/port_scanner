import socket
import sys
import validators
from colored import fg, attr, stylize

usage = """
Usage:
      test.py 127.0.0.1 2222
      """

def check_port(port):
    return 1 <= int(port) <= 65535      

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = sys.argv[2]

    if validators.ipv4(ip) and check_port(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        res = s.connect_ex((ip,int(port)))
        if res == 0:
            #print(f"Port {port} is open")
            print(stylize(f"Port {port} is open", fg("green") + attr("bold")))
        else:
            print(stylize(f"Port {port} is closed", fg("red") + attr("bold")))
else:
    print(usage)







