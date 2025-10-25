import socket
from customtkinter import *

def new_win():
    win2 = CTk()
    win2.title("мавпа2")
    win2.geometry("500x400")
    win2.configure(fg_color="green")

    text_area = CTkTextbox(win2,  width=450, height=400)
    text_area.place(x=30, y=-70)


    your_text=CTkEntry(win2,placeholder_text="Тут писати",width=200,height=70,font=("Arial", 26, "bold"))
    your_text.place(x=65,y=340)
    send=CTkButton(win2,text="✈",width=80,height=55)
    send.place(x=300,y=350)




    win2.mainloop()


win = CTk()
win.title("мавпа")
win.geometry("500x400")
win.configure(fg_color="green")

name_label = CTkLabel(win, text="Name", font=("Arial", 26, "bold"))
name_label.pack(pady=10)

name_entry = CTkEntry(win)
name_entry.pack(pady=10)

host_label = CTkLabel(win, text="Host", font=("Arial", 26, "bold"))
host_label.pack(pady=15)

host_entry = CTkEntry(win)
host_entry.pack(pady=15)

port_label = CTkLabel(win, text="Port", font=("Arial", 26, "bold"))
port_label.pack(pady=15)

port_entry = CTkEntry(win)
port_entry.pack(pady=16)

btn = CTkButton(win, text="Увійти", command=new_win)
btn.pack(pady=20)


win.mainloop()