import socket
from tkinter import *
def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',"client:"+message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message = s.recv(50)
    listbox.insert('end',"server:"+message.decode('utf-8'))

root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()
button = Button(root,text = "send",command = lambda :send(listbox,entry))
button.pack(side=BOTTOM)
rbutton = Button(root,text = "Receive",command = lambda :receive(listbox))
rbutton.pack(side=BOTTOM)

root.title("client")


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME,PORT))




