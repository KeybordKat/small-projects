# Notes: this method of user input is very unsafe as it can be used to inject malicious code
# into a system, safe in a basic calculator, but not when dealing with user data


# imports module required to make the window
import tkinter as tk

# sets the calculation variable as blank
calculation = ""


def add_to_calculation(symbol):
    global calculation
    # adds any symbol to the calculation regardless of if its a string
    calculation += str(symbol)
    # parameters for deleting and inserting into our calculator
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# creates main window, sets size, sets colour, sets font and font size
root = tk.Tk()
root.geometry("300x315")
root.configure(bg='#FFB0B0')
text_result = tk.Text(root, height=2, width=15, font=("Century Gothic", 24))

# creating the buttons for the digits, including their position in the grid and design
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Century Gothic", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Century Gothic", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Century Gothic", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Century Gothic", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Century Gothic", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Century Gothic", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Century Gothic", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Century Gothic", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Century Gothic", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Century Gothic", 14))
btn_0.grid(row=5, column=1)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Century Gothic", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Century Gothic", 14))
btn_minus.grid(row=3, column=4)

btn_multiply = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Century Gothic", 14))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Century Gothic", 14))
btn_divide.grid(row=5, column=4)

btn_open_bracket = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Century Gothic", 14))
btn_open_bracket.grid(row=5, column=2)

btn_close_bracket = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Century Gothic", 14))
btn_close_bracket.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=10, font=("Century Gothic", 14))
btn_equals.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

btn_clear = tk.Button(root, text="clear", command=clear_field, width=10, font=("Century Gothic", 14))
btn_clear.grid(row=6, column=3, columnspan=2, padx=10, pady=10)

# creates a grid for typing
text_result.grid(row=1, columnspan=5, padx=10, pady=10)
root.mainloop()
