from tkinter import *
from tkinter import messagebox
from PIL import Image

# ---------------------------- PYTHON SCRIPT ------------------------------- #
def forecast():
    inflation_rate = inflation_entry.get()
    revenue = rev_entry.get()
    bsp_policy = policy_entry.get()
    if inflation_rate == '' or revenue == '' or bsp_policy == '':
        return messagebox.showwarning('Warning', 'Some fields are empty.')
    else:
        try:
            inflation_rate = float(inflation_rate)
            revenue = float(revenue)
            bsp_policy = float(bsp_policy)
        except ValueError:
            return messagebox.showerror('Error', 'Input numbers only.')

        #Rule 1
        if inflation_rate <= 6.2 and revenue > 22.3:
            forecast = (0.0085 * inflation_rate) + (0.0993 * bsp_policy) + 0.9394

        #Rule 2
        elif inflation_rate > 4.05 and inflation_rate <= 5.75 and revenue > 22.3:
            forecast = (0.0221 * inflation_rate) + (0.0052 * revenue) + (0.0415 * bsp_policy) + 0.9252

        #Rule 3
        elif bsp_policy <= 2.375 and inflation_rate > 3.35 and inflation_rate <= 4.1:
            forecast = (0.0311 * inflation_rate) + (0.0005 * revenue) + (0.0636 * bsp_policy) + 0.9176

        #Rule 4
        elif bsp_policy > 4 and inflation_rate > 7.85:
            forecast = (0.1404 * inflation_rate) + (0.0001 * revenue) + (0.2782 * bsp_policy) + 1.5991

        #Rule 5
        elif bsp_policy <= 4 and inflation_rate <= 5.15:
            forecast = (0.1984 * inflation_rate) - (0.0078 * revenue) + (0.1219 * bsp_policy) + 0.1502

        #Rule 6
        elif bsp_policy > 2.875 and bsp_policy <= 4:
            forecast = (0.5685 * inflation_rate) - (0.0004 * revenue) + (0.1577 * bsp_policy) - 1.9833

        #Rule 7
        elif inflation_rate > 6.5 and revenue <= 51.3:
            forecast = (-0.4216 * inflation_rate) - (0.0027 * revenue) + (0.8186 * bsp_policy) + 3.1131

        #Rule 8
        else:
            forecast = (0.7427 * inflation_rate) + (0.3828 * bsp_policy) - 3.8654

        return messagebox.showinfo("Forecast", f"Market Rate: {round(forecast, 4)}")

def reset():
    inflation_entry.delete(0)
    rev_entry.delete(0)
    policy_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Mgt 286: DSS by Guena A. Nablo")
window.config(padx=30, pady=20, bg="#DAE3F4")

# title = Label(text="MARKET RATE FORECAST")
# title.config(font=('Calibri', 20, 'bold'), bg='#DAE3F4', fg='White', pady=5)
# title.grid(row=0, column=0, columnspan=3)

canvas = Canvas(width=350, height=60, bg='#DAE3F4', highlightthickness=0)
img = PhotoImage(file="title2.png")
canvas.create_image(180, 80, image=img)
canvas.grid(row=0, column=0, columnspan=2)

inflation_text = Label(text="Inflation Rate:     ", bg="#DAE3F4", fg="Black", anchor='w')
inflation_text.grid(column=0, row=1)
inflation_entry = Entry(width=20)
inflation_entry.grid(column=1, row=1, padx=5, pady=5)

rev_text = Label(text="Ph Revenue:        ", bg="#DAE3F4", fg="Black", anchor='w')
rev_text.grid(column=0, row=2)
rev_entry = Entry(width=20)
rev_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

policy_text = Label(text="BSP Policy Rate: ", bg='#DAE3F4', fg='Black', anchor='w')
policy_text.grid(column=0, row=3)
policy_entry = Entry(width=20)
policy_entry.grid(column=1, row=3, padx=5, pady=5)

forecast_button = Button(text="Forecast", width=20, border=3, command=forecast, bg='#2F5596', font=('Calibri', 9, 'bold'))
forecast_button.grid(column=0, row=4, padx=5, pady=5)

reset_button = Button(text="Reset", width=20, border=3, command=reset, bg='#D54135', font=('Calibri', 9, 'bold'))
reset_button.grid(column=1, row=4, padx=5, pady=5)

window.mainloop()