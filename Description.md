# Overview of Application
When running the client, you will be prompted to either recieve advice or a badly selected, perhaps slighly offensive, self confidence lowering celebrity look alike. 
# Client->Server Message Format
    For advice: 
        The first character in the outgoing message should be "1" for advice. If the advice is romantic, the second character should be "1", and if the advice is just general, the second character should be "2". 
        All possible message sending options are: 11, 12
    For a bad celebrity look alike: 
        The first character should be 2. The second character should be 1, 2 or 3 for whether the person in question is a redhead, blonde or brunette, respectively. 
        The third character should be 0 if the person does not have notable eyebrows and 1 if they do. 
        You will end with a 3 digit number which is one of the following: 
            210, 211, 220, 221, 230, 231
# Server->Client Message Format 
    For advice: 
        If the first digit of the message is 1, the server will send back advice. if the second digit is 1, the advice is romantic, if it is 2 the advice is general. The server should then send back advice in bytes. 
    For celebrity look alike: 
        if the first digit of the message is 2, the server will send back a celebrity look alike. The second digit signifies the hair color (1, 2 or 3 for redhead, blonde and brunette) and the third digit signifies the presence of eyebrows (0 for not really, 1 for definitely bushy eyebrows.) The server should then chose a celebrity with the descriptions and send it back in byte formating. 
# Example Output
Client:
    sophia@Sophias-MacBook-Air-3 csc-249-p1-simple-rpc-app % python3 AdviceClient.py
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established
Type 1 to recieve unsolicited advice from my Italian mom. Type 2 to get your poorly chosen celebrity look-alike. Type 'quit' to quit the program.1
what kind of advice do you want, (1) romantic or (2) general 1
sending message '11' to server
message sent, waiting for reply
received reply 'the fancier the car, the smaller the penis' from server
Type 1 to recieve unsolicited advice from my Italian mom. Type 2 to get your poorly chosen celebrity look-alike. Type 'quit' to quit the program.quit
client quitting at operator request
test client is done, exiting...

Server:
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 62650)
Received client message: '11' [2 bytes]
sending'the fancier the car, the smaller the penis back to client
server is done!

Another Example: 
Client: 
sophia@Sophias-MacBook-Air-3 csc-249-p1-simple-rpc-app % python3 AdviceClient.py
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established
Type 1 to recieve unsolicited advice from my Italian mom. Type 2 to get your poorly chosen celebrity look-alike. Type 'quit' to quit the program.2
What is your hair color? (1 for redhead, 2 for blonde, 3 for brunette): 3
would you say you have particularly pronounced eyebrows? (yes or no): yes
your hair is 3
sending message '231' to server
message sent, waiting for reply
received reply 'The Rock' from server
Type 1 to recieve unsolicited advice from my Italian mom. Type 2 to get your poorly chosen celebrity look-alike. Type 'quit' to quit the program.

Server: 
sophia@Sophias-MacBook-Air-3 csc-249-p1-simple-rpc-app % python3 testserver.py
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 62662)
Received client message: '231' [3 bytes]
sending'The Rock back to client

# Acknowledgments
my mom (Chiara Manodori)

