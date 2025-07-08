import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

moon=tk.Tk()
moon.configure(bg="darkBlue")
moon.geometry('1500x700')
moon.title('Diploma Percentage MIC COLLEGE OF TECHNOLOGY')
#BACKEND

def Back():
	M=messagebox.askyesno(message="Are you sure to Exit? Your data will loss completely ",icon="warning",title="Exit",type=("yesno"))
	if M==1:
		moon.destroy()
	else:
		pass

for i in range(100000):

    def Enabel():
        E1.config(state=NORMAL)
        E2.config(state=NORMAL)
        E3.config(state=NORMAL)
        E4.config(state=NORMAL)
        E5.config(state=NORMAL)
        Button(F1,text="  DISABEL EDIT  ",font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",width=12,command=Disabel).place(x=280,y=230)

    def Disabel():
        E1.config(state=DISABLED)
        E2.config(state=DISABLED)
        E3.config(state=DISABLED)
        E4.config(state=DISABLED)
        E5.config(state=DISABLED)
        Button(F1,text="  ENABEL EDIT  ",font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",width=12,command=Enabel).place(x=280,y=230)


def Clear_2():		
	E1_1.delete(0,'end')
	E2_2.delete(0,'end')
	E3_3.delete(0,'end')
	E4_4.delete(0, 'end')
	E5_5.delete(0,'end')

for i in range(100000):
        def Clear_1():
                E1.delete(0,'end')
                E2.delete(0,'end')
                E3.delete(0,'end')
                E4.delete(0, 'end')
                E5.delete(0, 'end')
                Button(F1,text="  Get Back  ",width=12,font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",command=getback).place(x=50,y=230)
        def getback():
                E1.insert(0,1000)
                E2.insert(0,1000)
                E3.insert(0,1000)
                E4.insert(0,1000)
                E5.insert(0,300)
                Button(F1,text="  Clear  ",width=12,font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",command=Clear_1).place(x=50,y=230)

        
                
                
	
	
	
	
	

def Calculate():
    A=int(E1.get())
    B=int(E2.get())
    C=int(E3.get())
    D=int(E4.get())
    E=int(E5.get())

    F=int(E1_1.get())
    G=int(E2_2.get())
    H=int(E3_3.get())
    I=int(E4_4.get())
    J=int(E5_5.get())

    OM=A/4+B+C+D+E
    YM=F/4+G+H+I+J

    Per=round((YM/OM)*100,2)
    n=str(Per)
    Label(moon,text="--Yours Diploms Percentage--",bg="darkblue",fg="white",font=("",10,"bold")).place(x=570,y=450)
    Label(moon,text="OVERALL SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=420,y=480)
    Label(moon,text=" YOUR SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=450,y=520)
    Label(moon,text="YOUR PERCENTAGE :",font=("",14,""),bg="darkblue",fg="white").place(x=435,y=560)

    Label(moon,text=OM,bg="darkblue",fg="white",font=("",10,"bold")).place(x=650,y=485)
    Label(moon,text=YM,bg="darkblue",fg="white",font=("",10,"bold")).place(x=650,y=525)
    Label(moon,text=n+"%",bg="darkblue",fg="red",font=("",10,"bold")).place(x=650,y=565)




    

    
    
#FRONTEND
Label(moon,text="WELCOME TO MOONSTAR PYHTON WORLD",bg="darkblue",fg="white",font=("",20,"bold")).place(x=400,y=20)

#FRISTFRAME

Label(moon,text="--Overall Diploms Marks--",bg="darkblue",fg="white",font=("",10,"bold")).place(x=230,y=80)

F1=Frame(moon,width=500,highlightbackground="white",highlightthickness=1.50,bg="darkblue",bd=10,cursor="dotbox",height=30,highlightcolor="blue")
F1.grid(row=0,column=0,padx=40,pady=120,ipadx=15,ipady=130)

Label(F1,text="ENTER FIRST SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=30,y=20)
E1=Entry(F1,width=10,font=("",10,"bold"),bd=3)
E1.place(x=300,y=23)
E1.insert(0,1000)
E1.config(state=DISABLED)
Label(F1,text="*1/4th Marks Taken",font=("",10,""),bg="darkblue",fg="red").place(x=380,y=20)

Label(F1,text="ENTER THIRD SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=28,y=60)
E2=Entry(F1,width=10,font=("",10,"bold"),bd=3)
E2.insert(0,1000)
E2.place(x=300,y=63)
E2.config(state=DISABLED)

Label(F1,text="ENTER FOURTH SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=8,y=100)
E3=Entry(F1,width=10,font=("",10,"bold"),bd=3)
E3.insert(0,1000)
E3.place(x=300,y=103)
E3.config(state=DISABLED)

Label(F1,text="ENTER FIFTH SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=30,y=140)
E4=Entry(F1,width=10,font=("",10,"bold"),bd=3)
E4.insert(0,1000)
E4.place(x=300,y=143)
E4.config(state=DISABLED)

Label(F1,text="ENTER SIXTH SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=30,y=180)
E5=Entry(F1,width=10,font=("",10,"bold"),bd=3)
E5.insert(0,300)
E5.place(x=300,y=183)
E5.config(state=DISABLED)

Button(F1,text="  CLEAR  ",width=12,font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",command=Clear_1).place(x=50,y=230)
Button(F1,text="  ENABEL EDIT  ",font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",width=12,command=Enabel).place(x=280,y=230)


#SECONDFRAME

Label(moon,text="--Yours Diploms Marks--",bg="darkblue",fg="white",font=("",10,"bold")).place(x=930,y=80)

F2=Frame(moon,width=500,highlightbackground="white",highlightthickness=1.50,bg="darkblue",bd=10,cursor="dotbox",height=30,highlightcolor="blue")
F2.grid(row=0,column=1,padx=140,pady=120,ipadx=15,ipady=130)

Label(F2,text="ENTER FIRST SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=30,y=20)
E1_1=Entry(F2,width=10,font=("",10,"bold"),bd=3)
E1_1.place(x=300,y=23)
'''for i in range(100):
        E1_1.get()
        if E1_1== int("a"):
                messagebox.showinfo(message="numbers are onl allowed",type=("ok"))'''

#E1_1.insert(0,1000)
Label(F2,text="*ENTER ALL ",font=("",10,""),bg="darkblue",fg="red").place(x=380,y=20)



Label(F2,text="ENTER THIRD SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=28,y=60)
E2_2=Entry(F2,width=10,font=("",10,"bold"),bd=3)
#E2_2.insert(0,1000)
E2_2.place(x=300,y=63)

Label(F2,text="ENTER FOURTH SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=8,y=100)
E3_3=Entry(F2,width=10,font=("",10,"bold"),bd=3)
#E3_3.insert(0,1000)
E3_3.place(x=300,y=103)

Label(F2,text="ENTER FIFTH SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=30,y=140)
E4_4=Entry(F2,width=10,font=("",10,"bold"),bd=3)
#E4_4.insert(0,1000)
E4_4.place(x=300,y=143)

Label(F2,text="ENTER SIXTH SEM MARKS :",font=("",14,""),bg="darkblue",fg="white").place(x=30,y=180)
E5_5=Entry(F2,width=10,font=("",10,"bold"),bd=3)
#E5_5.insert(0,300)
E5_5.place(x=300,y=183)

Button(F2,text="  CLEAR  ",width=12,font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",command=Clear_2).place(x=50,y=230)
Button(F2,text="  CALCULATE  ",font=("",10,"bold"),fg="white",bg="blue",bd=5,cursor="hand2",width=12,command=Calculate).place(x=280,y=230)






Label(moon,text='You can contact "@moonstar_mr_official_ on instgram" for help',font=("",14,""),bg="darkblue",fg="white",cursor="hand1").place(x=400,y=640)
b1=Button(moon,text="  EXIT  ",font=("",10,"bold"),fg="RED",bg="blue",bd=5,cursor="hand2",width=12,command=Back).place(x=600,y=600)


moon.mainloop()
