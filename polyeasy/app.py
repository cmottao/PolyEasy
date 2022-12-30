from tkinter import *

from operations import *
from utils import *

root = Tk()
root.title('PolyEasy')
root.geometry('240x360')

#Display
display = Entry(root, font='Myriad 17', bg='gray17', fg='white') 
display.place(x=0, y=0, width=240, height=60)

#Calculator fuctions 
i = 0

def get_expression(n):
    global i
    display.insert(i, n)
    i += 1

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state) != 0:
        display_state = display_state[:-1]
        clear_display()
        display.insert(0, display_state)

def calculate():
    exp = display.get()
    p = encod(split_pol_p(exp))
    q = encod(split_pol_q(exp))
    operator = find_operator(exp)
    clear_display()
    if operator == '+':
        display.insert(0,decod(add_polinomyals(p,q)))
    elif operator == '-':
        display.insert(0,decod(substract_polinomyals(p,q)))
    elif operator == '×':
        display.insert(0,decod(multiply_polinomyals(p,q)))
    elif operator == '÷':
        display.insert(0,decod(divide_polinomyals(p,q)))
    else:
        display.insert(0,'Error')

#Numeric buttons
Button(root, text='1', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('1')).place(x=0, y=260, width=60, height=50)
Button(root, text='2', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('2')).place(x=60, y=260, width=60, height=50)
Button(root, text='3', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('3')).place(x=120, y=260, width=60, height=50)
Button(root, text='4', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('4')).place(x=0, y=210, width=60, height=50)
Button(root, text='5', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('5')).place(x=60, y=210, width=60, height=50)
Button(root, text='6', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('6')).place(x=120, y=210, width=60, height=50)
Button(root, text='7', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('7')).place(x=0, y=160, width=60, height=50)
Button(root, text='8', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('8')).place(x=60, y=160, width=60, height=50)
Button(root, text='9', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('9')).place(x=120, y=160, width=60, height=50)
Button(root, text='0', bg='gray45', fg='white', font='Myriad 15', command=lambda:get_expression('0')).place(x=60, y=310, width=60, height=50)

#Operator buttons
Button(root, text='÷', bg='orange', fg='white',font= 'Myriad 20', command=lambda:get_expression('÷')).place(x=180, y=110, width= 60, height=50)
Button(root, text='×', bg='orange', fg='white',font= 'Myriad 20', command=lambda:get_expression('×')).place(x=180, y=160, width= 60, height=50)
Button(root, text='-', bg='orange', fg='white',font= 'Myriad 20', command=lambda:get_expression('-')).place(x=180, y=210, width= 60, height=50)
Button(root, text='+', bg='orange', fg='white',font= 'Myriad 20', command=lambda:get_expression('+')).place(x=180, y=260, width= 60, height=50)
Button(root, text='^', bg='gray28', fg='white',font= 'Myriad 17', command=lambda:get_expression('^')).place(x=120, y=110, width= 60, height=50)

#Other buttons
Button(root, text='AC', bg='gray28', fg='white', font='Myriad 15', command=lambda:clear_display()).place(x=0, y=110, width=60, height=50)
Button(root, text='⌫', bg='gray28', fg='white', font='Myriad 15', command=lambda:undo()).place(x=60, y=110, width= 60, height=50)
Button(root, text='(', bg='gray28', fg='white', font='Myriad 17', command=lambda:get_expression('(')).place(x=0, y=60, width=60, height=50)
Button(root, text=')', bg='gray28', fg='white', font='Myriad 17', command=lambda:get_expression(')')).place(x=60, y=60, width=60, height=50)
Button(root, text='.', bg='gray45', fg='white', font='Myriad 20', command=lambda:get_expression('.')).place(x=0, y=310, width=60, height=50)
Button(root, text='=', bg='orange', fg='white', font='Myriad 20', command=lambda:calculate()).place(x=180, y=310, width=60, height=50)
Button(root, text=',', bg='gray45', fg='white', font='Myriad 20', command=lambda:get_expression(',')).place(x=120, y=310, width=60, height=50)
Button(root, text='x', bg='gray28', fg='white', font='Myriad 17', command=lambda:get_expression('x')).place(x=120, y=60, width=60, height=50)

#:) Button
Button(root, text=':)', bg='orange', fg='white', font='Myriad 17').place(x=180, y=60, width=60, height=50)

root.mainloop()