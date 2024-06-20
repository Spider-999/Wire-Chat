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
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class Chat(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Chat window

        # Widgets
        # Message frame
        self.message_frame = ctk.CTkFrame(self, height=400, width=100, corner_radius=16, bg_color='lightgray')
        self.message_frame.grid(row=0, column=0, padx=20)

        # Message list
        self.message_list = ctk.CTkTextbox(master=self.message_frame, height=400, width=400, bg_color='white',
                                           state='disabled', corner_radius=16, border_color='#000000', border_width=1)
        self.message_list.pack(side=tk.TOP)

        # Message variables
        self.entry_message = tk.StringVar()
        self.entry_message.set('')

        # Text entry widget
        self.text_entry = ctk.CTkEntry(master=self, textvariable=self.entry_message,
                                       placeholder_text='Type here...',
                                       width=200, corner_radius=32, border_color='#000000', border_width=1,
                                       font=('', 16))
        self.text_entry.grid(row=1, column=0, ipadx=80)

        # Send button
        self.send_button = ctk.CTkButton(master=self, text='Send message', corner_radius=32, fg_color='#7076fc',
                                         hover_color='#76adea', border_color='#000000', border_width=1, font=('', 16))
        self.send_button.grid(row=1, column=1, ipadx=30, padx=30)

        # Connections list
        self.connections_frame = ttk.Frame(master=self, height=200, width=200)
        self.connections_frame.grid(row=0, column=1)
        self.connections_list = ctk.CTkTextbox(master=self.connections_frame, height=200, width=200, state='disabled',
                                               corner_radius=16, border_color='#000000', border_width=1)
        self.connections_list.pack(side=tk.LEFT)

        self.pack(fill=tk.BOTH, expand=1)


class Login(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Login window

        # Username label
        self.user_label = ctk.CTkLabel(self, text='Enter your username:')
        self.user_label.place(relx=0.28, rely=0.5, anchor='center')

        # Username button
        self.entry_user = tk.StringVar()
        self.entry_user.set('')
        self.username = ctk.CTkEntry(self, width=200, height=50, corner_radius=16, textvariable=self.entry_user)
        self.username.place(relx=0.5, rely=0.5, anchor='center')

        # Connect button
        self.connect_button = ctk.CTkButton(self, text='Connect')
        self.connect_button.place(relx=0.75, rely=0.5, anchor='center')

        self.pack(fill = tk.BOTH, expand = 1)


class App:
    def __init__(self, master):
        # App window setup
        master.resizable(False, False)
        master.geometry('800x600')
        master.title('Wire')
        master.minsize(800, 600)
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        self.LOGIN_INDEX = 0
        self.CHAT_INDEX = 1

        # App frames
        self.app_frame = tk.Frame(master)
        self.app_frame.pack(padx = 10, pady = 10, fill='both', expand = 1)

        # Create the login and chat objects
        self.login = Login(self.app_frame)
        self.chat = Chat(self.app_frame)

        # Store the frames in a list
        self.frame_list = [self.login, self.chat]
        self.frame_list[self.CHAT_INDEX].forget()
        self.frame_list[self.LOGIN_INDEX].tkraise()


    def goto_chat(self):
        self.frame_list[self.LOGIN_INDEX].forget()
        self.frame_list[self.CHAT_INDEX].tkraise()
        self.frame_list[self.CHAT_INDEX].pack(fill='both', expand = 1)
