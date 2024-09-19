#!/usr/bin/env python3
# Simple server test client
#
# This simple client application can be used to test a server that is under development.
# The application opens a connection to the server, then goes into a loop where it prompts
# the user to provide a string message to be sent over to the server for processing. Then
# the client waits for a reply and prints it. To exit and disconnect, the user can enter 'quit'
# at the prompt.

import socket

HOST = "127.0.0.1"  # This is the loopback address
PORT = 65432        # The port used by the server

def run_client():
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connection established")
        while True:
            # loop until the user asks to quit
            if not talk_to_server(s):
                break
#talking to server 
def talk_to_server(sock):
    msg = input("Type 1 to recieve unsolicited advice from my Italian mom. Type 2 to get your poorly chosen celebrity look-alike. Type 'quit' to quit the program.")
    if msg == 'quit':
        print("client quitting at operator request")
        return False
    elif msg == '1': 
        type = input("what kind of advice do you want, (1) romantic or (2) general ")
        if type == "1":
            msg = "11"
        elif type == "2": 
            msg = "12"
        else: 
            "Sorry, I don't understand. quitting program..."
            return False
    elif msg == "2":
        type = input("What is your hair color? (1 for redhead, 2 for blonde, 3 for brunette): ")
        eyebrows = input("would you say you have particularly pronounced eyebrows? (yes or no): ")
        if(type == "1" or type == "2" or type =="3"):
            print("your hair is " + type)
            if (eyebrows == "yes"):
                msg = "2"+type+"1"
            elif (eyebrows == "no"):
                msg = "2"+type + "0"
            else: 
                print("Sorry, I don't understand. quitting program...")
                return False
        else:
            print("Sorry, I don't understand. quitting program...")
            return False
    else: 
        print("Sorry, I don't understand. quitting program...")
        return False
    print(f"sending message '{msg}' to server")
    sock.sendall(msg.encode('utf-8'))
    print("message sent, waiting for reply")
    reply = sock.recv(1024).decode('utf-8')
    if not reply:
        return False
    else:
        print(f"received reply '{reply}' from server")
        return reply

if __name__ == "__main__":
    run_client()
    print("test client is done, exiting...")
