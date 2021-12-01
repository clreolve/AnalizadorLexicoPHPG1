#
import tkinter as tk
from tkinter import ttk, tix
from sintaxis import sintaxis_test
from lexico import lexical_test

bg = '#2b2b2b'
foreground = '#d1dce8'
# This is a scrollable text widget
class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, bg= bg, foreground= foreground,
                            insertbackground='white',
                            selectbackground="blue", width=100, height=40)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=30, bg=bg)
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
            #self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            self.create_text(2, y, anchor="nw", text=linenum, fill="white")
            i = self.textwidget.index("%s+1line" % i)

class Results(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, bg=bg, foreground=foreground,
                            insertbackground='white',
                            selectbackground="blue", width=40, height=35,state = tk.DISABLED)

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

# main window
main = tk.Tk()
main.title(project_name)
main.resizable(False, False)
# main.geometry(window_size)

# group frames
button_frames = tk.Frame(main)
text_frames = tk.Frame(main)

text_code = ScrollText(text_frames)
text_response = Results(text_frames)

# the magic
def get_text():
    txt = text_code.get("1.0", "end")
    return txt

def validar_sintactico():
    inputValue = get_text()
    result = sintaxis_test(inputValue)
    res = "Errores:\n"
    keys = list(result.keys())
    for e in keys:
        res = res + f'Error line {e}: \n\t{result.pop(e)}\n'

    if(len(keys) == 0):
        text_response.rewrite("No hay Errores Sintacticos")
    else:
        text_response.rewrite(res)

    print(result)


def validar_lexico():
    inputValue = get_text()
    result = lexical_test(inputValue)
    res = ""
    for i in range(0,len(result)-1):
        res = res + f'{result.pop(0)}\n'
    text_response.rewrite(res)


button_sintax_valid = tk.Button(button_frames, text='Validacion Sintactica',
                                command=validar_sintactico, width=40)

button_lexical_valid = tk.Button(button_frames, text='Validacion Léxica',
                                 command=validar_lexico,width=40)
button_stop = tk.Button(button_frames, text='Cerrar', command=main.destroy,
                        bg= "Red",width=40)


text_code.pack(side ='left')
text_response.pack(side='right')

text_frames.pack(side='top')

button_sintax_valid.pack(fill="x")
button_lexical_valid.pack(fill="x")
button_stop.pack(fill ="x")

button_frames.pack()

main.mainloop()