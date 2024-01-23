from tkinter  import *
from tkinter import messagebox
import base64
import os
from tkinter import PhotoImage
#for main decryption and password also here:----------------------
def decrypt():
    password=code.get()
    if password=="1234":       
         screen2=Toplevel(screen)
         screen2.title("decryption")
         screen2.geometry("400x200")
         screen2.configure(bg='#00bd56')
         message=text1.get(1.0,END)
         decode_message=message.encode("ascii")
         base64_bytes=base64.b64decode(decode_message)
         decrypt=base64_bytes.decode("ascii")
         
         Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
         text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
         text2.place(x=10,y=40,width=380,height=150)
         
         text2.insert(END,decrypt)
         
    elif password=="":
        messagebox.showerror("encryption","Input Password")
    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password") 
#for main encryption and password also here:----------------------
def encrypt():
     password=code.get()
     
     if password=="1234":
         screen1=Toplevel(screen)
         screen1.title("encryption")
         screen1.geometry("400x200")
         screen1.configure(bg='#D2B48C')
         message=text1.get(1.0,END)
         encode_message=message.encode("ascii")
         base64_bytes=base64.b64encode(encode_message)
         encrypt=base64_bytes.decode("ascii")
         
         Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#D2B48C").place(x=10,y=0)
         text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
         text2.place(x=10,y=40,width=380,height=150)
         
         text2.insert(END,encrypt)
         
     elif password=="":
         messagebox.showerror("encryption","Input Password")
     elif password!="1234":
         messagebox.showerror("encryption","Invalid Password")    



#for main structure to design the main box--------------
def main_screen():
    
    global screen
    global code
    global text1
    
    screen=Tk()
    screen.geometry("375x398")
    # screen.configure(bg='skyblue')
    
    
#for adding the logo of the app----------    
    image_icon=PhotoImage(file="e_d.png")
    screen.iconphoto(False,image_icon)
    screen.title("E-DApp")
    
    #for reset function code--------------
    def reset():
        code.set("")
        text1.delete(1.0,END)
        
#for the label and text box and buttons-----------------------    
    Label(text="Enter text for encryption and decryption",fg="black",font=("calbri",13),bg="grey").place(x=10,y=10)
    
    text1 =Text(font="Robote 20",bg="White",relief=GROOVE,wrap=WORD,bd=0)
    
    text1.place(x=10,y=50,width=355,height=100)
    
    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calbri",13),bg="grey").place(x=10,y=170)
    
    code=StringVar()
    
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
    
    Button(text="Encrypt",height="2",width=23,bg="#D2B48C",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    
    Button(text="Decrypt",height="2",width=23,bg="#00bd56",fg="white",bd=0,highlightbackground="black",highlightthickness=2,command=decrypt).place(x=200,y=250)
      
    Button(text="Reset",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
    
    screen.mainloop()
main_screen()    