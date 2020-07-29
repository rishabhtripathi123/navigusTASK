from tkinter import *
import sqlite3 as sql
import re
from tkinter import messagebox

class Gui:
    def __init__(s):
        s.client=sql.connect('user.db')
        s.cu=s.client.cursor()
        try:
            s.cu.execute("create table user(id int auto_increment,name varchar(50),password varchar(20),email varchar(100))")
        except:
            pass
        s.loginpage()
    def register(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1200x600+0+0')#'widthxheight+x+y
        s.scr.config(bg='khaki1')
        l=Label(s.scr,bg='blue',font=('times',30,'bold'),text='Welcome to my task')
        l.pack(side=TOP,fill=X)
        l1=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Username')
        l1.place(x=300,y=100)
        l2=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Password')
        l2.place(x=300,y=200)
        l3=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Re password')
        l3.place(x=300,y=300)
        l4=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Email')
        l4.place(x=300,y=400)
        user=Entry(s.scr,bg='blue',fg='white',font=('times',30,'bold'))
        user.place(x=600,y=100)
        ps=Entry(s.scr,show='*',bg='blue',fg='white',font=('times',30,'bold'))
        ps.place(x=600,y=200)
        ps1=Entry(s.scr,show='*',bg='blue',fg='white',font=('times',30,'bold'))
        ps1.place(x=600,y=300)
        email=Entry(s.scr,bg='blue',fg='white',font=('times',30,'bold'))
        email.place(x=600,y=400)
        b=Button(s.scr,command=lambda :s.regi(user.get(),ps.get(),ps1.get(),email.get()),text='register',bg='blue',fg='white',font=('times',30,'bold'))
        b.place(x=600,y=500)
        b1=Button(s.scr,command=s.loginpage,text='back',bg='blue',fg='white',font=('times',30,'bold'))
        b1.place(x=300,y=500)
        s.scr.mainloop()
    def regi(s,u,p,p1,e):
        if not(re.search(r'^\S+$',u)):
               messagebox.showerror('register','user name must not contain spaces')
        elif not(re.search(r'^\S+$',p)) or not(re.search(r'^\S+$',p1)):
            messagebox.showerror('register','password must not contain spaces')
        elif not(re.search(r'^\S+@\w+[.][a-z]{2,3}$',e)):
            messagebox.showerror('register','invalid email')
        else:
            if p!=p1:
                messagebox.showerror('register','both passwords didnot match')
            else:
                s.cu.execute('insert into user (name,password,email) values (%r,%r,%r)'%(u,p,e))
                s.client.commit()
                s.loginpage()
    def login(s,u,p):
        if not(re.search(r'^\S+$',u)):
               messagebox.showerror('login','user name must not contain spaces')
        elif not(re.search(r'^\S+$',p)):
            messagebox.showerror('login','password must not contain spaces')
        else:
            s.cu.execute('select count(*) from user where name=%r and password=%r'%(u,p))
            if s.cu.fetchone()[0]!=0:
                print("login sucess")
            else:
                messagebox.showerror('login','invalid credentials')
            
    def loginpage(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1200x600+0+0')#'widthxheight+x+y
        s.scr.config(bg='khaki1')
        l=Label(s.scr,bg='blue',font=('times',30,'bold'),text='My Task')
        l.pack(side=TOP,fill=X)
        l1=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Username')
        l1.place(x=300,y=200)
        l2=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Password')
        l2.place(x=300,y=300)
        user=Entry(s.scr,bg='blue',fg='white',font=('times',30,'bold'))
        user.place(x=600,y=200)
        ps=Entry(s.scr,show='*',bg='blue',fg='white',font=('times',30,'bold'))
        ps.place(x=600,y=300)
        b=Button(s.scr,command=lambda :s.login(user.get(),ps.get()),text='Login',bg='blue',fg='white',font=('times',30,'bold'))
        b.place(x=300,y=400)
        b1=Button(s.scr,command=s.register,text='New user',bg='blue',fg='white',font=('times',30,'bold'))
        b1.place(x=600,y=400)
        s.scr.mainloop()
Gui()
