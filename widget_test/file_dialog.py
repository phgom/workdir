import tkinter as tk
import tkinter.ttk as ttk  # for notebook
import tkinter.scrolledtext as scr
import tkinter.filedialog as fd

class FileDiag:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("File Dialog Example")
        self.win.geometry("1024x768+100+100")
        self.win.resizable(False,False)
        self.create_widgets()
        self.file_opend=0
        self.win.bind_all('<Control-o>',self.open)
        self.win.bind_all('<Control-s>', self.save)
        self.win.bind_all('<Control-S>', self.saveas)
        self.win.bind_all('<Control-q>', self.close)


    def close(self, *args):
        self.win.quit()
        self.win.destroy()

    def open(self, *args):
        self.filename = fd.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text Files", "*.txt"),("All Files", "*.*")))
        if not self.filename:
            return
        f = open(self.filename,'r')
        self.file_opend = 1
        self.scr.delete("1.0", tk.END)
        while True:
            line=f.readline()
            if not line:
                break
            self.scr.insert(tk.INSERT, line)
        f.close()

    def save(self, *args):
        if(self.file_opend == 0) :
            self.saveas()
            return
        f = open(self.filename, 'w')
        f.write(self.scr.get("1.0", tk.END))
        f.close()

    def saveas(self, *args):
        self.ftypes=[("Text Files", "*.txt"),("All Files", "*.*")]
        self.filename = fd.asksaveasfilename(initialdir="/", title="Save As File", filetypes=self.ftypes)
        if not self.filename:
            return
        f = open(self.filename,'w')
        f.write(self.scr.get("1.0",tk.END))
        f.close()



    def create_widgets(self):
        # Menubar
        self.menubar = tk.Menu(self.win)

        self.menu_1 = tk.Menu(self.menubar, tearoff=0, selectcolor="red")
        self.menu_1.add_command(label="Open", command=self.open, accelerator="Ctrl+o")
        self.menu_1.add_command(label="Save", command=self.save, accelerator="Ctrl+s")
        self.menu_1.add_separator()
        self.menu_1.add_command(label="Save As", command=self.saveas, accelerator="Ctrl+S")
        self.menu_1.add_separator()
        self.menu_1.add_command(label="Exit", command=self.close, accelerator="Ctrl+q")
        self.menubar.add_cascade(label="File", menu=self.menu_1)

        self.menu_2 = tk.Menu(self.menubar, tearoff=0, selectcolor="red")
        self.menu_2.add_command(label="About")
        self.menu_2.add_command(label="ContactUs")
        self.menubar.add_cascade(label="Help", menu=self.menu_2)

        self.win.config(menu=self.menubar)


        # self.menu_3 = tk.Menu(self.menubar, tearoff=0)
        # self.menu_3.add_checkbutton(label="하위 메뉴 3-1")
        # self.menu_3.add_checkbutton(label="하위 메뉴 3-2")
        # self.menubar.add_cascade(label="상위 메뉴 3", menu=self.menu_3)

        # Notebook

        self.notebook = ttk.Notebook(self.win)
        self.notebook.grid(sticky="nwes")

        # Frame
        self.frame1 = tk.Frame(self.win)
        self.notebook.add(self.frame1,text="FileDialog")

        # Scrolled Text
        self.scr = scr.ScrolledText(self.frame1, wrap=tk.WORD, width=122, height=43)
        self.scr.grid(column=0,  row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="news")








fdiag = FileDiag()
fdiag.win.mainloop()

