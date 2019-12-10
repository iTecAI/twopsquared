import socket
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import time
import secrets

def ip():
    return socket.gethostbyname(socket.gethostname())

def generate_salt():
    t = time.time()
    token = secrets.SystemRandom(t)


class Crypt:
    def __init__(self,password,peer):
        self.peer = peer

    def gen_key(self,password,salt):
        password = bytes(password,'utf-8')
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

class NodeServer:
    def __init__(self,peer,addr):
        self.addr = addr
        self.peer = peer
    def send_data(self,addr,data):
        conn = socket.create_connection(addr)
        conn.sendall()

class Peer:
    def __init__(self,localport,identifier,method_class,connection_methods=[]):
        self.cmethods = connection_methods
        self.mclass = method_class
        self.id = identifier
        self.port = localport
        self.node_servers = []
    def bootstrap(self,addr):
        pass