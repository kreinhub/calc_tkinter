from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calc again')


# calc logic
def calc(val):
    if val == 'C':
        screen.delete(0, END)
    elif val == '+/-':
        raw_string = str(screen.get())
        signs = "+-*/"

        if raw_string.isdigit():
            result = '-' + raw_string
            screen.delete(0, END)
            screen.insert(0, result)
        else:
            for idx, val in enumerate(raw_string):
                if val in signs:
                    if val == '-' and idx == 0:
                        result = raw_string[idx + 1:]
                        screen.delete(0, END)
                        screen.insert(0, result)
                    elif val == '-' and raw_string[idx - 1] not in signs[2:]:
                        result = raw_string[:idx] + '+' + raw_string[idx + 1:]
                        screen.delete(0, END)
                        screen.insert(0, result)
                    elif val == '+':
                        result = raw_string[:idx] + '-' + raw_string[idx + 1:]
                        screen.delete(0, END)
                        screen.insert(0, result)
                    elif val in signs[2:] and raw_string[idx + 1].isdigit():
                        result = raw_string[:idx + 1] + '-' + raw_string[idx + 1:]
                        screen.delete(0, END)
                        screen.insert(0, result)
                    elif val in signs[2:] and not raw_string[idx + 1].isdigit():
                        result = raw_string[:idx + 1] + raw_string[idx + 2:]
                        screen.delete(0, END)
                        screen.insert(0, result)

    elif val == '=':
        screen.insert(END, '=' + str(eval(screen.get())))
    else:
        screen.insert(END, val)


# draw buttons
button_list = [
    "7", "8", "9", "+/-", "*",
    "4", "5", "6", "/", "+",
    "1", "2", "3", "-", "=",
    "0", ".", "C", "", ""
]
r = 1
c = 0

for i in button_list:
    cmd = lambda temp=i: calc(temp)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1
screen = Entry(root, width=33)
screen.bind("<Button-1>", "pass")

screen.grid(row=0, column=0, columnspan=5)

root.mainloop()