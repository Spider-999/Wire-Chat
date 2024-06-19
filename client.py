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
from gui import App, tk, ctk


class Client(App):
    def __init__(self, window):
        super().__init__(window)
        # Create the graphical user interface object
        # The client class inherits from the app class
        self.chat.send_button.configure(command = self.send_message)
        self.login.connect_button.configure(command=self.get_username)

        # Sockets setup
        self.HOST = '127.0.0.1'
        self.PORT = 50000
        self.BYTES = 4096
        self.FORMAT = 'utf-8'
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))


    def send_message(self):
        # Send message to the server to be broadcast to every client
        try:
            # Get the message from the Entry widget
            message = self.chat.entry_message.get()

            if message != '':
                self.insert_text(f'you:{message}')
                self.chat.entry_message.set('')

                # Encode it and send it to the server
                encoded_message = message.encode('utf-8')
                self.client_socket.send(encoded_message)
        except socket.error as error:
            print(f'[SEND_MESSAGE] {error}')


    def receive_message(self):
        # Receive messages from the server
        while True:
            try:
                message = self.client_socket.recv(self.BYTES).decode(self.FORMAT)
                if message != 'USERNAME':
                    self.insert_text(message)
                    print(message)
            except socket.error as error:
                # If an error occurred print it
                print(f'[RECEIVE_MESSAGE] {error}')
                break
        self.insert_text('[SERVER] - Connection lost.')
        self.client_socket.close()


    def insert_text(self, message):
        # Insert text in the chat
        self.chat.message_list.configure(state = 'normal')
        self.chat.message_list.insert(tk.END, message + '\n')
        self.chat.message_list.configure(state = 'disabled')


    def get_username(self):
        # Get the username and change the frame to the chat frame
        username = self.login.entry_user.get()
        self.client_socket.send(username.encode(self.FORMAT))
        self.goto_chat()


    def start_client(self):
        # Start the client thread
        receive_thread = threading.Thread(target=self.receive_message)
        receive_thread.start()

window = ctk.CTk()
client = Client(window)
client.start_client()
window.mainloop()