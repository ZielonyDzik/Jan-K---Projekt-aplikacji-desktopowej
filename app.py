import tkinter as tk
from tkinter import *   

root = tk.Tk()

root.geometry("715x1000")
root.title('Zielony Las')
root.configure(bg='#00802b')
root.iconbitmap('zielonydzik.ico')
root.resizable(False, False)  

#============INFORMACJE============#

class BetterButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master, **kw)
        self.defaultText = self["text"]
        self.bind("<Button-1>", self.on_click_left)
        self.bind("<Button-3>", self.on_click_right)

    def on_click_left(self, event):
        self["text"] = "Naciśnij prawym przyciskiem myszy aby schować.\n\n Najczęściej organizowane wydarzenia:\n - Wspólne słuchanie muzyki i rozmowy\n - Wspólne granie w gry komputerowe\n - Wspólne granie w gry planszowe\n - Event Karaoke\n - Konkursy plastyczne/graficzne\n - Zawody sportowe i esportowe"

    def on_click_right(self, event):
        self["text"] = "Opis społeczności - Naciśnij lewym przyciskiem myszy aby wyświetlić."

class Button:

    info1 = tk.Label(root, text="Zielony Las - Informacje", fg='white', bg='#00802b', font=('none', 16, 'bold'))
    info1.grid(column=0, row=0)
    info2 = tk.Label(root, text="Jest to społeczność, w której organizowane są różne wydarzenia zapewniające rozrywkę i dużo atrakcji.", fg='white', bg="#00802b", font=('none', 12, 'normal'))
    info2.grid(column=0, row=1)
    info2 = tk.Label(root, text=" ", fg='white', bg="#00802b", font=('none', 12, 'normal'))
    info2.grid(column=0, row=2)

    wyswietl = BetterButton(root, text="Opis społeczności - Naciśnij lewym przyciskiem myszy aby wyświetlić.", bg="#006622", fg="white", width=100, height=10)
    wyswietl.grid(column=0, row=3)
    

#============LOGOWANIE============#

a = {"Iterb": "Abecadło28", "ZielonyDzik": "Dzik123", "HyPer": "hypoero"}


class LogowanieRozszerzone(tk.Entry):
    def __init__(self, master=None, tekst_zastepczy="podaj liczbe", color="grey"):
        super().__init__(master, width=26)

        self.tekst_zastepczy = tekst_zastepczy
        self.tekst_zastepczy_color = color
        self.default_fg_color = self['fg']

        self.bind("<Key>", self.foc_in)

        self.bind("<Leave>", self.foc_out)

        self.put_tekst_zastepczy()

    def put_tekst_zastepczy(self):
        self.delete('0', 'end')
        self.insert(0, self.tekst_zastepczy)
        self['fg'] = self.tekst_zastepczy_color

    def foc_in(self, *args):
        if self['fg'] == self.tekst_zastepczy_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_tekst_zastepczy()

img = PhotoImage(file="las.ppm")

class Logowanie:
    def __init__(self, root):
        self.tekst1 = tk.StringVar()
        self.tekst2 = tk.StringVar()

        self.label002 = tk.Label(root, text="              ", width=705, height=600, bg="#00802b")
        self.label002.grid(row=4, column=0)

        self.label003 = tk.Label(self.label002, text="              ", width=605, height=500, bg="#00802b", image=img)
        self.label003.grid(row=4, column=0)

        self.label001 = tk.Label(root,text="Logowanie", bg="#00802b", font=('none', 20, 'bold'))
        self.label001.grid(row=5,column=0)

        self.label01 = tk.Label(root, text="Aby się zalogować wpisz nazwę użytkownika oraz hasło.", bg="#00802b")
        self.label01.grid(row=6, column=0)

        self.label01 = tk.Label(root, text="              ", bg="#00802b")
        self.label01.grid(row=8, column=0)

        self.label01 = tk.Label(root, text="              ", bg="#00802b")
        self.label01.grid(row=10, column=0)

        self.label01 = tk.Label(root, text="              ", bg="#00802b")
        self.label01.grid(row=12, column=0)

        self.entry01 = LogowanieRozszerzone(root, tekst_zastepczy="Podaj nazwę użytkownika")
        self.entry01.grid(row=7, column=0)

        self.entry02 = LogowanieRozszerzone(root, tekst_zastepczy="")
        self.entry02.config(show="*")
        self.entry02.grid(row=9,column=0)

        self.b1 = tk.Button(root, text="Zaloguj się", bg="#006622", command=lambda: self.zmien_tekst(self.label01, self.entry01.get(), self.entry02.get()))
        self.b1.grid(row=11, column=0)

        self.label01 = tk.Label(root, text="Czekam na zalogowanie", bg="#00802b")
        self.label01.grid(row=13, column=0)

    def zmien_tekst(self, label, user, passwd):
        if user in a:
            pass
            if passwd == a[user]:
                label.config(text="Użytkownik zalogowany")
            else:
                label.config(text="Złe hasło")
        else:
            label.config(text="Użytkownik nie istnieje")

login = Logowanie(root)
#==================================#


#================================#

root.mainloop()
