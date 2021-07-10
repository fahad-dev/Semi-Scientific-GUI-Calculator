import tkinter
import math

window = tkinter.Tk()
window.geometry('500x650')
window.title("Scientific Calculator")
window.resizable(0,0)

# Functions

def button_click(item):
    global expression
    expression = expression + str(item)
    inputted_text.set(expression)

def button_click_clear():
    global expression
    expression = ""
    inputted_text.set(expression)

def button_click_equal():
    global expression
    expression = str(eval(expression))
    inputted_text.set(expression)

def cos_function():
    global expression
    expression = str(math.cos(eval(expression)))
    inputted_text.set(expression)

def sin_function():
    global expression
    expression = str(math.sin(eval(expression)))
    inputted_text.set(expression)

def tan_function():
    global expression
    expression = str(math.tan(eval(expression)))
    inputted_text.set(expression)

def square_root_function():
    global expression
    expression = str(math.sqrt(eval(expression)))
    inputted_text.set(expression)

def square_function():
    global expression
    expression = str((eval(expression))**2)
    inputted_text.set(expression)

def cube_function():
    global expression
    expression = str((eval(expression))**3)
    inputted_text.set(expression)

def log_function():
    global expression
    expression = str(math.log(eval(expression),10))
    inputted_text.set(expression)

def natural_log_function():
    global expression
    expression = str(math.log(eval(expression),math.e))
    inputted_text.set(expression)

expression = ""
inputted_text = tkinter.StringVar() # Used to edit a widget's text

# Frame creation for input field and entire calculator
input_frame = tkinter.Frame(window,width=500,height=400,bd=0,highlightbackground="black",highlightcolor="black")
input_frame.pack()
input_field = tkinter.Entry(input_frame, font=('radioland',30), textvariable=inputted_text,width=50,bg="#969970", bd=0)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

lower_frame = tkinter.Frame(window,width=500,height=300,bg="red")
lower_frame.pack(side="bottom")
scientific_buttons_frame = tkinter.Frame(window,width=500,height=200,bg="orange")
scientific_buttons_frame.pack()
number_buttons_frame = tkinter.Frame(lower_frame,width=400,height=200,bg="green")
number_buttons_frame.pack(side="left")
operation_buttons_frame = tkinter.Frame(lower_frame,width=100,height=199,bg="grey")
operation_buttons_frame.pack(side="right")

# Button creation for each row
#1) Scientific buttons creation
sin = tkinter.Button(scientific_buttons_frame,text="sin",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: sin_function()).grid(row=0,column=0,padx=1,pady=1)
cos = tkinter.Button(scientific_buttons_frame,text="cos",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: cos_function()).grid(row=0,column=1,padx=1,pady=1)
tan = tkinter.Button(scientific_buttons_frame,text="tan",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: tan_function()).grid(row=0,column=2,padx=1,pady=1)
square_root = tkinter.Button(scientific_buttons_frame,text="√",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: square_root_function()).grid(row=1,column=0,padx=1,pady=1)
square = tkinter.Button(scientific_buttons_frame,text="x²",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: square_function()).grid(row=1,column=1,padx=1,pady=1)
cube = tkinter.Button(scientific_buttons_frame,text="x³",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: cube_function()).grid(row=1,column=2,padx=1,pady=1)
#exponent = tkinter.Button(scientific_buttons_frame,text="yˣ",width=23,height=4,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: exponent_function()).grid(row=1,column=3,padx=1,pady=1)
log = tkinter.Button(scientific_buttons_frame,text="log₁₀",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: log_function()).grid(row=2,column=0,padx=1,pady=1)
natural_log = tkinter.Button(scientific_buttons_frame,text="ln",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: natural_log_function()).grid(row=2,column=1,padx=1,pady=1)
pi = tkinter.Button(scientific_buttons_frame,text="π",width=23,height=3,fg="black",bg="#fff",bd=0,cursor="hand2",command= lambda: button_click("math.pi")).grid(row=2,column=2,padx=1,pady=1)
#2) Operations buttons creation
# First row:
left_parentheses = tkinter.Button(operation_buttons_frame,text="(",width=11,height=4,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("(")).grid(row=0,column=0,padx=1,pady=1)
right_parentheses = tkinter.Button(operation_buttons_frame,text=")",width=11,height=4,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click(")")).grid(row=0,column=1,padx=1,pady=1)
clear = tkinter.Button(operation_buttons_frame,text="CLEAR",width=23,height=5,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click_clear()).grid(row=1,column=0,padx=1,pady=1,columnspan=5)
divide = tkinter.Button(operation_buttons_frame,text="÷",width=11,height=5,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("/")).grid(row=2,column=0,padx=1,pady=1)
multiply = tkinter.Button(operation_buttons_frame,text="×",width=11,height=5,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("*")).grid(row=2,column=1,padx=1,pady=1)
add = tkinter.Button(operation_buttons_frame,text="+",width=11,height=5,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("+")).grid(row=3,column=0,padx=1,pady=1)
subtract = tkinter.Button(operation_buttons_frame,text="-",width=11,height=5,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("-")).grid(row=3,column=1,padx=1,pady=1)
equal = tkinter.Button(operation_buttons_frame,text="=",width=23,height=4,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click_equal()).grid(row=4,column=0,padx=1,pady=1,columnspan=5)

#3) Number buttons creation
nine = tkinter.Button(number_buttons_frame,text="9",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("9")).grid(row=0,column=0,padx=1,pady=1)
eight = tkinter.Button(number_buttons_frame,text="8",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("8")).grid(row=0,column=1,padx=1,pady=1)
seven = tkinter.Button(number_buttons_frame,text="7",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("7")).grid(row=0,column=2,padx=1,pady=1)
six = tkinter.Button(number_buttons_frame,text="6",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("6")).grid(row=1,column=0,padx=1,pady=1)
five = tkinter.Button(number_buttons_frame,text="5",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("5")).grid(row=1,column=1,padx=1,pady=1)
four = tkinter.Button(number_buttons_frame,text="4",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("4")).grid(row=1,column=2,padx=1,pady=1)
three = tkinter.Button(number_buttons_frame,text="3",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("3")).grid(row=2,column=0,padx=1,pady=1)
two = tkinter.Button(number_buttons_frame,text="2",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("2")).grid(row=2,column=1,padx=1,pady=1)
one = tkinter.Button(number_buttons_frame,text="1",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("1")).grid(row=2,column=2,padx=1,pady=1)
zero = tkinter.Button(number_buttons_frame,text="0",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("0")).grid(row=3,column=0,padx=1,pady=1)
decimal = tkinter.Button(number_buttons_frame,text=".",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click(".")).grid(row=3,column=1,padx=1,pady=1)
make_negative = tkinter.Button(number_buttons_frame,text="+/-",width=15,height=6,fg="black",bg="#fff",bd=0,cursor="hand2",command=lambda: button_click("*(-1)")).grid(row=3,column=2,padx=1,pady=1)

window.mainloop()
