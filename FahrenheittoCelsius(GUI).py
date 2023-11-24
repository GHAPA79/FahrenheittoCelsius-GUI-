import tkinter as tk
from tkinter import ttk
# ttk -> sefareshi kardane dore rabete gerafiki.

window = tk.Tk()

lbl_fahrenheit = tk.Label(
    window,
    text='FAHRENHEIT : ',
    bg='pink',
    )
lbl_fahrenheit.grid(row=0,column=0,padx=(10,10),pady=15,)


ent_fahrenheit = ttk.Entry(
    window,
    width=50,
    )
ent_fahrenheit.grid(row=0,column=1,padx=(1,10),pady=15,)


lbl_celsius = tk.Label(
    window,
    text='CELSIUS  ---> ',
    bg='pink',
    )
lbl_celsius.grid(row=1,column=0,padx=(20,10),pady=(10,25),)


lbl_risult = tk.Label(
    window,
    text='You will see the risult here...',
    bg='pink',
    )
lbl_risult.grid(row=1,column=1,padx=10,pady=(10,25),)


def convert_fahrenheit_to_celsius(*args):
    # *args -> rabete beyne (window.bind()) va in taabe baraye ejade dokme Enter.
    fahrenheit_input = ent_fahrenheit.get()
    try:
        fahrenheit_value = float(fahrenheit_input) # agr float nashavad belafasele varede except mishavad.
        lbl_risult['text'] = (fahrenheit_value - 32) / 1.8
    except ValueError:
        if fahrenheit_input != '':
            # if -> agar inputi dashtim ke be float tabdil nemishavad. 
            lbl_risult['text'] = 'You should enter a number.'
        else:
            # else -> agar input khali bood.
            lbl_risult['text'] = 'Risult is empty. Please enter a number.'


btn_button = ttk.Button(
    window,
    text='CALC',
    command=convert_fahrenheit_to_celsius,
    width=10,
    )
btn_button.grid(row=0,column=2,padx=(10,30),pady=15,)


window.bind('<Return>',convert_fahrenheit_to_celsius,)
# window.bind() -> ejad dokmeh Enter.


window.configure(bg='pink')

window.title('< Convert Fahrenheit to Celsius >')

window.mainloop()