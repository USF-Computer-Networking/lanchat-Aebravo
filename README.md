To run the chat application, you must open at least three terminal windows. In one, you must run chatserver.py (start the server brefore initializing clients),
on the other two, open chat.server.py. I used a youtube tutorial as source code, I improved on the code by removing threading locks between receiving messages and typing messages in order
to receive messages real time (On the previous version, you have to press enter or send a message to be prompted new messages in order to bypass a thread
lock which prevented the thread from continuing to receive messages before sending one out). I also modified the server in order to not re-send a clients
own message to themselves. I modified the client app so that you become a client as soon as you type in your name by sending a message to the server that
you have joined the chat, by doing so, you are added to the client list before sending your first message, that way you can receive a message from someone
else before sending a message out. I also added a help prompt.

When running the chatclient.py, run as "python chatclient.py -name *YOUR_NAME*".

# lanchat-Aebravo
