# Wire-Chat
A python desktop chatting application made with sockets and customtkinter.

TODO:
- improve GUI looks.
- Add connected users to a separate panel
- Add FTP
- Maybe VOIP
- Add emojis

  The purpose of this software was to learn more stuff about sockets programming, GUI programming, OOP and client-server architecture.

  
  username frame:
![image1](https://github.com/Spider-999/Wire-Chat/assets/67486366/895b1028-4190-4421-96e6-c2763f3f62c9)

  chat application frame:
![image2](https://github.com/Spider-999/Wire-Chat/assets/67486366/5ab6d56a-93d8-4a6d-a31f-984f5329954b)


Usage:
Run the server file which in its current state hosts the app on localhost(127.0.0.1) and then run how many client files you want.

The app can connect to different computers if you change the host variable in the server.py file and in the client.py file
to your private ip and then you could talk between clients using different computers connected to the same WIFI.
You could host the server yourself using ngrok, linode or any other services. If you decide to host the app using your public
ip address(I don't recommend this) you might run into some trouble with firewalls and many other things.
