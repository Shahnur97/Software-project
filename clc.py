import tkinter as tk


def add_number(value):
    current_exp = output.get("1.0","end-1c")
    new_exp = current_exp + value
    output.delete("1.0", "end")
    output.insert("1.0", new_exp)

def add_operator(op):
    current_exp = output.get("1.0","end-1c")
    new_exp = current_exp + op
    output.delete("1.0", "end")
    output.insert("1.0", new_exp)

def equal():
    expression = output.get("1.0","end-1c")
    try:
        result = eval(expression)
        output.delete("1.0", "end")
        output.insert("1.0", str(result))
    except:
        output.delete("1.0", "end")
        output.insert("1.0", "Error")

def clear():
    new_exp = output.get("1.0","end-2c")
    output.delete("1.0", "end")
    output.insert("1.0", new_exp)


root = tk.Tk()

root.geometry("390x440")

output = tk.Text(root, width=20, height=1, font=("Arial", 24))
output.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


c= tk.Button(root, font=("Arial", 16), text="C", width=4, height=1, command=lambda: clear())
c.grid(row=1, column=0, padx=10, pady=10)
dot= tk.Button(root, font=("Arial", 16), text=".", width=4, height=1, command=lambda: add_number("."))
dot.grid(row=1, column=1, padx=10, pady=10)
mod= tk.Button(root, font=("Arial", 16), text="%", width=4, height=1, command=lambda: add_operator("%"))
mod.grid(row=1, column=2, padx=10, pady=10)
div= tk.Button(root, font=("Arial", 16), text="/", width=4, height=1, command=lambda: add_operator("/"))
div.grid(row=1, column=3, padx=10, pady=10)

n7= tk.Button(root, font=("Arial", 16), text="7", width=4, height=1, command=lambda: add_number("7"))
n7.grid(row=2, column=0, padx=10, pady=10)
n8= tk.Button(root, font=("Arial", 16), text="8", width=4, height=1, command=lambda: add_number("8"))
n8.grid(row=2, column=1, padx=10, pady=10)
n9= tk.Button(root, font=("Arial", 16), text="9", width=4, height=1, command=lambda: add_number("9"))
n9.grid(row=2, column=2, padx=10, pady=10)
mult= tk.Button(root, font=("Arial", 16), text="*", width=4, height=1, command=lambda: add_operator("*"))
mult.grid(row=2, column=3, padx=10, pady=10)

n4= tk.Button(root, font=("Arial", 16), text="4", width=4, height=1, command=lambda: add_number("4"))
n4.grid(row=3, column=0, padx=10, pady=10)
n5= tk.Button(root, font=("Arial", 16), text="5", width=4, height=1, command=lambda: add_number("5"))
n5.grid(row=3, column=1, padx=10, pady=10)
n6= tk.Button(root, font=("Arial", 16), text="6", width=4, height=1, command=lambda: add_number("6"))
n6.grid(row=3, column=2, padx=10, pady=10)
minus= tk.Button(root, font=("Arial", 16), text="-", width=4, height=1, command=lambda: add_operator("-"))
minus.grid(row=3, column=3, padx=10, pady=10)

n1= tk.Button(root, font=("Arial", 16), text="1", width=4, height=1, command=lambda: add_number("1"))
n1.grid(row=4, column=0, padx=10, pady=10)
n2= tk.Button(root, font=("Arial", 16), text="2", width=4, height=1, command=lambda: add_number("2"))
n2.grid(row=4, column=1, padx=10, pady=10)
n3= tk.Button(root, font=("Arial", 16), text="3", width=4, height=1, command=lambda: add_number("3"))
n3.grid(row=4, column=2, padx=10, pady=10)
plus= tk.Button(root, font=("Arial", 16), text="+", width=4, height=1, command=lambda: add_operator("+"))
plus.grid(row=4, column=3, padx=10, pady=10)

brc_strt= tk.Button(root, font=("Arial", 16), text="(", width=4, height=1, command=lambda: add_operator("("))
brc_strt.grid(row=5, column=0, padx=10, pady=10)
n0= tk.Button(root, font=("Arial", 16), text="0", width=4, height=1, command=lambda: add_number("0"))
n0.grid(row=5, column=1, padx=10, pady=10)
brc_end= tk.Button(root, font=("Arial", 16), text=")", width=4, height=1, command=lambda: add_operator(")"))
brc_end.grid(row=5, column=2, padx=10, pady=10)
eq= tk.Button(root, font=("Arial", 16), text="=", width=4, height=1, command=lambda: equal())
eq.grid(row=5, column=3, padx=10, pady=10)


root.mainloop()