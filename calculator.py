from tkinter import*

def show(x):
    s = len(entry.get())
    entry.insert(s , str(x))

hesap = 5
s1 = 0
def calc(x):
    
    global hesap
    hesap = x
    global s1
    
    s1 = float(entry.get())
    entry.delete(0 , END)

s2 = 0
def son():
    global s2
    s2 = float(entry.get())
    global hesap
    a = 0
    if hesap == 0 :
        a = s1 + s2
    elif hesap == 1:
        a = s1 - s2
    elif hesap == 2 :
        a = s1 * s2
    elif hesap == 3 :
        a = s1 / s2
    
    entry.delete( 0 ,END)
    entry.insert( 0 , str(a))
    




def delet(x):
    entry.delete(0 , END)




window = Tk()
window.geometry("250x300+850+95")
window.title("calculator")
window.config(bg="#A3EBB1")


entry = Entry(window , font=("verdana"  ,14) , width=15 , justify=RIGHT)
entry.place(x=20 ,  y=20)

b = []
for i in range(1,10):
    b.append(Button(window , text=str(i) , font=("verdana" , 14) , bg="#3cb371" ,
                    activebackground="#3cb371" , command=lambda x = i:show(x)))

num = 0
for i in range(0,3):
    for j in range(0,3):
        b[num].place(x=20+j*50 , y= 50+i*50)
        num +=1


sumeval = []
for i in range(0,4):
    sumeval.append(Button(window ,font=("verdana" , 14) , bg="#3cb371" ,width=2,command=lambda x = i:calc(x),
                    activebackground="#3cb371")   )
for i in range(0,4):
    sumeval[i].place(x=170 , y = 50+50*i)

sumeval[0]["text"]  = "+"
sumeval[1]["text"]  = "-"
sumeval[2]["text"]  = "*"
sumeval[3]["text"]  = "/"


zb = Button(window , text="0" , font=("verdana" , 14) , bg="#3cb371" ,
                    activebackground="#3cb371",width=2 , command=lambda x = 0 :show(x) ).place(x=70 , y=200)
nb = Button(window , text="." , font=("verdana" , 14) , bg="#3cb371" ,
                    activebackground="#3cb371",width=2 , command=lambda x = ".":show(x) ).place(x= 20 , y=200 )
mb = Button(window , text="=" , font=("verdana" , 14) , bg="#3cb371" ,
                    activebackground="#3cb371" , fg="#6d0000" ,command=son).place(x=120 , y=200)
db = Button(window , text="C" , font=("verdana" , 14) , bg="#3cb371" ,
                    activebackground="#3cb371" , command= lambda x = i:delet(x) ).place(x=20 , y=250)










window.mainloop()