#
import tkinter as tk
from tkinter import ttk, tix
from sintaxis import lexical_test
bg = '#2b2b2b'
foreground = '#d1dce8'
# This is a scrollable text widget
class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, bg= bg, foreground= foreground,
                            insertbackground='white',
                            selectbackground="blue", width=100, height=30)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=40, bg='white')
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()



class TextLineNumbers(tk.Canvas):
    '''THIS CODE IS CREDIT OF Bryan Oakley:
    https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget'''
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            i = self.textwidget.index("%s+1line" % i)

class Results(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, bg=bg, foreground=foreground,
                            insertbackground='white',
                            selectbackground="blue", width=30, height=30,state = tk.DISABLED)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def rewrite(self, text, *args):
        self.text.config(state = tk.NORMAL)
        self.text.delete("1.0", "end")
        self.text.insert(tk.END, text)
        self.text.config(state=tk.DISABLED)


project_name = 'Analizador PHP'
sw = 100
window_size = "1200x600"

# main window
main = tk.Tk()
main.title(project_name)
main.geometry(window_size)

response = tk.StringVar()
button_stop = tk.Button(main, text='Cerrar', command=main.destroy, bg= "Red")
text_code  = ScrollText(main)
text_res  = tk.Text(main)
label_response = Results(main)
response.set("Resultado")
# the magic
def validar_lexico():
    inputValue = text_code.get("1.0", "end-1c")
    print(inputValue)
    result = lexical_test(inputValue)
    res = ""
    for key in result:
        if(result[key]['error'] == True):
            res = res + f'Error line{key}: \n\t{result[key]["text"]}\n'
    label_response.rewrite(res)
button_lexical_valid = tk.Button(main, text='Validacion Léxica', command=validar_lexico)

text_code.grid(row = 0, column = 0)
label_response.grid(row = 0, column = 2)
button_lexical_valid.grid(row = 2, column = 0)
button_stop.grid(row = 2, column = 1)


main.mainloop()