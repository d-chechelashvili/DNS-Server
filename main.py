import sys
from socket import *

import DNSParser
import DNSLogger


def run_dns_server(CONFIG, IP, PORT):
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind((IP, int(PORT)))
    while True:
        request, addr = server_socket.recvfrom(2048)
        id, info, qdCount, anCount, nsCount, arCount, \
        questions = DNSParser.parseRequest(request)
        DNSLogger.logRequest(id, info, qdCount, anCount, nsCount, arCount, questions)


# do not change!
if __name__ == '__main__':
    CONFIG = sys.argv[1]
    IP = sys.argv[2]
    PORT = sys.argv[3]
    run_dns_server(CONFIG, IP, PORT)
