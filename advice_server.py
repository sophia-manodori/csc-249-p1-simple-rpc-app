import random
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

radvice = ["don't share a man, let several men share you", "the fancier the car, the smaller the penis", "stop talking about women that way", "*sigh* if I were to divorce my wife, I would date several younger men all at the same time. You aren't married! You still can... if you want..."]
gadvice = ["go outside. It's weird to be inside this much. not normal *italian hand movements*", "you should talk to your therapist about that", "I'd say that mole looks normal, actually. Don't worry about it.", "it's okay to speed on the freeway. Just don't get a ticket."]
random.seed(version=2)
unhinged = ["Emilia Clark", "Dwayne 'The Rock' Johnson", "Emma Stone", "Merida (the princess from Brave)", "Ross Lynch", "Troye Sivan"]


print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            response = data.decode('utf-8')
            print(f"Received client message: '{response}' [{len(data)} bytes]")
            if (response[0] == "1"):
               num = random.randint(0, 3)
               if (response[1]== "1"):
                    data = radvice[num]
               if (response[1]== "2"):
                   data = gadvice[num]
            elif (response[0]=="2"):
                print("generating look alike")
                if(response[1]=="1"):
                    if(response[2]=="0"):
                        data = "You are Emma Stone"
                    if (response[2]=="1"):
                        data = "You are Merida (the princess from Brave)"
                    else:
                        break
                elif(response[1]=="2"):
                    print("they have blonde hair", response[2])
                    if(response[2]=="0"):
                        data = "You are Troye Sivan"
                        print(data)
                    if (response[2]=="1"):
                        data = "You are Ross Lynch"
                    else:
                        break
                elif(response[1]=="3"):
                    if(response[2]=="0"):
                        data = "Pitbull"
                    elif (response[2]=="1"):
                        data = "The Rock"
                    else:
                        break
                else:
                    print("error")
                    break
            print(f"sending'{data} back to client")
            conn.sendall(data.encode('utf-8'))

print("server is done!")