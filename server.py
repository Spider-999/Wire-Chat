'''
Copyright (C) 19/06/2024 Hary Patrascu
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
Last updated: 19/06/2024
Contact: email: harypatrascu.1@gmail.com
'''
import socket
import threading


class Server:
    def __init__(self):
        # Setup variables
        self.HOST = '127.0.0.1'
        self.PORT = 50000
        self.BYTES = 512
        self.FORMAT = 'utf-8'
        self.MAX_CONNECTIONS = 5

        # Setting the socket options to allow for reconnection and creating the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))

        # Variables to store new clients
        self.clients = []
        self.usernames = []

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(self.BYTES).decode('utf-8')
                print(f'{self.usernames[self.clients.index(client)]}:{message}')
                self.broadcast(message, client)
            except socket.error as error:
                print(error)
                # Remove username and client from the arrays
                user_index = self.clients.index(client)
                self.clients.remove(client)

                username = self.usernames[user_index]
                self.usernames.remove(username)

                print(f'[SERVER] {username} disconnected.')
                self.broadcast(f'[SERVER] {username} disconnected.', client)
                break
        client.close()

    def broadcast(self, message, this_client):
        for client in self.clients:
            if client != this_client:
                client.send(f'{self.usernames[self.clients.index(this_client)]}:{message}'.encode(self.FORMAT))

    def receive(self):
        # Listen for maximum 10 new connections
        self.server_socket.listen(self.MAX_CONNECTIONS)
        while True:
            # Accept a new connection
            client, address = self.server_socket.accept()
            print(f'[SERVER] New connection from {address}')

            # Get the username of the new client
            client.send('USERNAME'.encode(self.FORMAT))
            username = client.recv(self.BYTES).decode(self.FORMAT)
            print(username)
            # Append the new variables to the storage lists
            self.usernames.append(username)
            self.clients.append(client)

            # Let everyone know someone joined and show the new client that the connection was successful
            print(f'[SERVER] {username} joined the chat.')
            self.broadcast(f'joined the chat.', client)
            client.send('[SERVER] Connected.'.encode(self.FORMAT))

            # Start a server thread
            server_thread = threading.Thread(target=self.handle_client, args=(client,))
            server_thread.start()


if __name__ == '__main__':
    server = Server()
    server.receive()
    server.server_socket.close()
