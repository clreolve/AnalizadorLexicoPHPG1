#
import sys
import tkinter as tk
from sintaxis import parser, out

project_name = 'Analizador PHP'
sw = 100
r = tk.Tk()
r.title(project_name)
response = tk.StringVar()

button_stop = tk.Button(r, text='Cerrar', width=sw, command=r.destroy)
text_code  = tk.Text(r)
text_res  = tk.Text(r, height = 50)
label_response = tk.Label(r, width=sw, textvariable = response)
# the magic
def validar():
    inputValue = text_code.get("1.0", "end-1c")
    print(inputValue)
    result = parser.parse(inputValue)
    response.set(result)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

button_valid = tk.Button(r, text='Validar', width=sw, command=validar)
# button.pack()

text_code.pack()
label_response.pack()
button_stop.pack()
button_valid.pack()
#text_res.pack()


r.mainloop()