import os,sys,re,time
import json
import socket
import subprocess
import struct
import socketserver
import hashlib
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

IP_PORT=("127.0.0.1",8080)
buffer =  1024
