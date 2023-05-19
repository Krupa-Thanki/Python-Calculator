from tkinter import *

root = Tk()
root.geometry("310x450")
root.title("Calculator")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
        label_result.config(text=result)

label_result = Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="gray",command=lambda :show("/")).place(x=85,y=100)
Button(root,text="%",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="gray",command=lambda :show("%")).place(x=160,y=100)
Button(root,text="*",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="gray",command=lambda :show("*")).place(x=238,y=100)

Button(root,text="7",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("7")).place(x=10,y=170)
Button(root,text="8",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("8")).place(x=85,y=170)
Button(root,text="9",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("9")).place(x=160,y=170)
Button(root,text="-",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="gray",command=lambda :show("-")).place(x=238,y=168)

Button(root,text="4",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("4")).place(x=10,y=240)
Button(root,text="5",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("5")).place(x=85,y=240)
Button(root,text="6",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("6")).place(x=160,y=240)
Button(root,text="+",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="gray",command=lambda :show("+")).place(x=238,y=237)

Button(root,text="1",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("1")).place(x=10,y=310)
Button(root,text="2",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("2")).place(x=85,y=310)
Button(root,text="3",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("3")).place(x=160,y=310)
Button(root,text="0",width=7,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show("0")).place(x=10,y=380)

Button(root,text=".",width=3,height=1,font=("arial",25),bd=1,fg="#fff",bg="#2a2d36",command=lambda :show(".")).place(x=162,y=380)
Button(root,text="=",width=3,height=3,font=("arial",25),bd=1,fg="#fff",bg="orange",command=lambda :calculate()).place(x=238,y=305)

root.mainloop()