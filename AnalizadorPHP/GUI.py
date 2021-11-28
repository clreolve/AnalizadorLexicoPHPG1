#
import tkinter as tk
from sintaxis import parser

project_name = 'Analizador PHP'
sw = 100
r = tk.Tk()
r.title(project_name)

response = tk.StringVar()
button_stop = tk.Button(r, text='Cerrar', width=sw, command=r.destroy)
text_code  = tk.Text(r)
label_response = tk.Label(r, width=sw, textvariable = response)
# the magic
def validar():
    inputValue = text_code.get("1.0", "end-1c")
    print(inputValue)

    result = parser.parse(inputValue)
    print(result)

    response.set("valido")
button_valid = tk.Button(r, text='Validar', width=sw, command=validar)
# button.pack()

text_code.pack()
label_response.pack()
button_stop.pack()
button_valid.pack()

r.mainloop()