from tkinter import*
root=Tk()
def send():
    send="you=>"+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot=>hi")
    elif (e.get()=="hi"):
        txt.insert(END,"\n"+"bot=>hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"bot=>fine and you")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"bot=>okay")
    elif(e.get()=="what are you doing"):
        txt.insert(END,"\n"+"bot=>i am studing")
    elif(e.get()=="how is your studies"):
        txt.insert(END,"\n"+"bot=>good and you")
    else:
        txt.insert(END,"\n"+"bot=>nice to hear")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOX")
root.mainloop()


