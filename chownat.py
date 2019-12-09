import subprocess
from threading import Thread
import os
import sys

def server(local_port,dest,name=None,path=os.path.join('resources','chownat')):
    t = Thread(target=subprocess.Popen,name=name,args=[[path,'-d','-s',str(local_port),dest]],kwargs={'stdout':sys.stdout})
    t.start()
    return t

def client(local_port,dest,name=None,path=os.path.join('resources','chownat')):
    t = Thread(target=subprocess.Popen,name=name,args=[[path,'-d','-c',str(local_port),dest]],kwargs={'stdout':sys.stdout})
    t.start()
    return t