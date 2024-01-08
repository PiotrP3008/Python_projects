from tkinter import *
import math

def button_press(num):
    
    global equation_text
    global new_equation_text
    global old_num

    if(old_num == "="):
    
        old_num = num

        if(num == "+" or num == "-" or num == "/" or num == "*"):
            equation_text = equation_text +str(num)
            new_equation_text = ""
            equation_label.set("")
        
        elif(num == "="):
            equals()

        else:
            old_num = num
            equation_text = ""
            new_equation_text = ""
            new_equation_text = new_equation_text +str(num)
            equation_text = equation_text +str(num)
            equation_label.set(new_equation_text)

    else:
        old_num = num

        if(num == "+" or num == "-" or num == "/" or num == "*"):
            equation_text = equation_text +str(num)
            new_equation_text = ""
            equation_label.set("")
        
        elif(num == "="):
            equals()

        else:
            new_equation_text = new_equation_text +str(num)
            equation_text = equation_text +str(num)
            equation_label.set(new_equation_text)

def equals():
    
    global equation_text
    global new_equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
        new_equation_text = total


        
    
    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")
        equation_text = ""

def percent():
    
    global equation_text

    try:

        parts = str(eval(equation_text)/100)

        equation_label.set(parts)

        equation_text = parts

    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""

def power(a):
    
    global equation_text

    try:

        result = str(eval(equation_text)**a)

        equation_label.set(result)

        equation_text = result

    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""

def root(num):
    
    global equation_text

    try:

        result = str(eval(equation_text)**(1/num))

        equation_label.set(result)

        equation_text = result
        
    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""


def negativ():
    
    global equation_text

    try:

        parts = str((-1)*eval(equation_text))

        equation_label.set(parts)

        equation_text = parts

    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""

def denominator():
    
    global equation_text

    try:
        equation_label.set(str(1/eval(equation_text)))

        equation_text = str(1/eval(equation_text))

    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""



def clear():
    
    
    global equation_text
    global new_equation_text

    equation_label.set("")

    equation_text = ""
    new_equation_text = ""

def clearE():
    
    
    global equation_text
    global new_equation_text

    equation_label.set("")

    equation_text = equation_text[slice(0 ,-len(new_equation_text))]
    new_equation_text = ""


def reset():
    
    
    global equation_text
    global new_equation_text

    label.delete(len(label.get())-1, END)

    equation_text = equation_text[slice(0, -1)]
    new_equation_text = new_equation_text[slice(0, -1)]

window = Tk()

reset_photo = PhotoImage(file="C:\\Users\\_piotr_paterewicz\\Desktop\\python\\calculator\\reset.png")

window.title("Calculator")
window.geometry("380x500")
window.config(bg="#f3f3f3")

numButtonColor = "#ffffff"
numActivebackgroundColor = "#f9f9f9"

opeButtonColor = "#f9f9f9"
opeActivebackgroundColor = "#f4f4f4"

equButtonColor = "#005A9E"
equActivebackgroundColor = "#3179AF"


equation_text = ""
new_equation_text = ""
old_num = ""

equation_label = StringVar()
equation_label.set("0")

label = Entry(window, textvariable=equation_label, font=("Arial", 45), bg="#f3f3f3", justify="right")
label.pack(side=TOP)

frame = Frame(window)
frame.pack()

dmt = Button(frame, text="1/x",height=2, width=7, font=35, command=denominator, 
                 bg=opeButtonColor, activebackground=opeActivebackgroundColor, relief="flat")
dmt.grid(row=1, column=0, pady=2, padx=2)

button1 = Button(frame, text=1,height=2, width=7, font=35, command=lambda:button_press(1), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat", overrelief="flat")
button1.grid(row=4, column=0, pady=2, padx=2)

button2 = Button(frame, text=2,height=2, width=7, font=35, command=lambda:button_press(2),
                  bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button2.grid(row=4, column=1, padx=2)

button3 = Button(frame, text=3,height=2, width=7, font=35, command=lambda:button_press(3), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button3.grid(row=4, column=2, padx=2)

button4 = Button(frame, text=4,height=2, width=7, font=35, command=lambda:button_press(4), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button4.grid(row=3, column=0, pady=2)

button5 = Button(frame, text=5,height=2, width=7, font=35, command=lambda:button_press(5), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button5.grid(row=3, column=1)

button6 = Button(frame, text=6,height=2, width=7, font=35, command=lambda:button_press(6), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button6.grid(row=3, column=2)

button7 = Button(frame, text=7,height=2, width=7, font=35, command=lambda:button_press(7), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button7.grid(row=2, column=0, pady=2)

button8 = Button(frame, text=8,height=2, width=7, font=35, command=lambda:button_press(8), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button8.grid(row=2, column=1)

button9 = Button(frame, text=9,height=2, width=7, font=35, command=lambda:button_press(9), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button9.grid(row=2, column=2)

button0 = Button(frame, text=0,height=2, width=7, font=35, command=lambda:button_press(0), 
                 bg=numButtonColor, activebackground=numActivebackgroundColor, relief="flat")
button0.grid(row=5, column=1, pady=2)

plus = Button(frame, text="+",height=2, width=7, font=35, command=lambda:button_press("+"), 
              bg=opeButtonColor, activebackground=numActivebackgroundColor, relief="flat")
plus.grid(row=4, column=3)

minus = Button(frame, text="-",height=2, width=7, font=35, command=lambda:button_press("-"), 
               bg=opeButtonColor, activebackground=numActivebackgroundColor, relief="flat")
minus.grid(row=3, column=3)

multiply = Button(frame, text=chr(215),height=2, width=7, font=35, command=lambda:button_press("*"), 
                  bg=opeButtonColor, activebackground=opeActivebackgroundColor, relief="flat")
multiply.grid(row=2, column=3)

divide = Button(frame, text=chr(247),height=2, width=7, font=35, command=lambda:button_press("/"), 
                bg=opeButtonColor, activebackground=opeActivebackgroundColor, relief="flat")
divide.grid(row=1, column=3)

equal = Button(frame, text="=",height=2, width=7, font=35, command=lambda:button_press("="), bg=equButtonColor, 
               activebackground=equActivebackgroundColor, relief="flat")
equal.grid(row=5, column=3)

decimal = Button(frame, text=".",height=2, width=7, font=35, command=lambda:button_press("."), 
                 bg=opeButtonColor, activebackground=opeActivebackgroundColor, relief="flat")
decimal.grid(row=5, column=2)

perc = Button(frame, text="%",height=2, width=7, font=35, command=percent, bg=opeButtonColor, 
              activebackground=opeActivebackgroundColor, relief="flat")
perc.grid(row=0, column=0)

neg = Button(frame, text="+/-",height=2, width=7, font=35, command=negativ, bg=opeButtonColor, 
             activebackground=opeActivebackgroundColor, relief="flat")
neg.grid(row=5, column=0)

cube = Button(frame, text=("x"+chr(178)),height=2, width=7, font=35, command=lambda:power(2), bg=opeButtonColor, 
             activebackground=opeActivebackgroundColor, relief="flat")
cube.grid(row=1, column=1)

sqrt = Button(frame, text=(chr(8730)),height=2, width=7, font=35, command=lambda:root(2), bg=opeButtonColor, 
             activebackground=opeActivebackgroundColor, relief="flat")
sqrt.grid(row=1, column=2)


clear = Button(frame, text="C",height=2, width=7, font=35, command=clear, bg=opeButtonColor, 
               activebackground=opeActivebackgroundColor, relief="flat")
clear.grid(row=0, column=2)

ce = Button(frame, text="CE",height=2, width=7, font=35, command=clearE, bg=opeButtonColor, 
               activebackground=opeActivebackgroundColor, relief="flat")
ce.grid(row=0, column=1)

reset = Button(frame,height=58, width=81, font=50, bg=opeButtonColor, 
               activebackground=opeActivebackgroundColor, relief="flat", image=reset_photo, command=reset)
reset.grid(row=0, column=3)


window.mainloop()
