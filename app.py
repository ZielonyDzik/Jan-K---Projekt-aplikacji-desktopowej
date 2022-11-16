import tkinter as tk

root = tk.Tk()

root.geometry("1000x1000")
root.title('Zielony Las')
root.configure(bg='#395814')
root.iconbitmap('zielonydzik.ico')

#==================================#

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

    info1 = tk.Label(root, text="Zielony Las - Informacje", fg='white', bg='#395814', font=('none', 16, 'bold'))
    info1.grid(column=0, row=0)
    info2 = tk.Label(root, text="Jest to społeczność, w której organizowane są różne wydarzenia zapewniające rozrywkę i dużo atrakcji.", fg='white', bg="#395814", font=('none', 12, 'normal'))
    info2.grid(column=0, row=1)
    info2 = tk.Label(root, text=" ", fg='white', bg="#345210", font=('none', 12, 'normal'))
    info2.grid(column=0, row=2)

    wyswietl = BetterButton(root, text="Opis społeczności - Naciśnij lewym przyciskiem myszy aby wyświetlić.", bg="#395814", fg="white", width=100, height=10)
    wyswietl.grid(column=0, row=3)
    

#==================================#



root.mainloop()
