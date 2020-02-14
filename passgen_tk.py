"""Password generator."""
import random
import string
import tkinter as tk


def get_number():
    """Get values function."""
    pass_wd = ''
    pass_char = string.ascii_letters + string.digits + string.punctuation
    for _ in range(1, 32):
        pass_wd += random.choice(pass_char)
    return pass_wd


class Window(tk.Frame):
    """Draw TK window and widgets."""

    def __init__(self, master=None):
        """Init window."""
        tk.Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=tk.BOTH, expand=1)

        # create widgets
        textBox = tk.Text(self, height=1, width=32)
        passButton = tk.Button(self, text="Run",
                               width=5,
                               command=lambda: [textBox.delete("1.0", tk.END),
                                                textBox.insert(tk.END,
                                                               get_number())])
        exitButton = tk.Button(self, text="Exit",
                               width=5,
                               command=self.clickExitButton)
        clearButton = tk.Button(self, text="Clear", width=5,
                                command=lambda: textBox.delete("1.0", tk.END))

        # place widgets
        textBox.place(x=10, y=10)
        passButton.place(x=10, y=45)
        clearButton.place(x=66, y=45)
        exitButton.place(x=121, y=45)

    def clickExitButton(self):
        """Exit program."""
        exit()

#    def clickRunButton(self):
#        """Run program."""
#        get_number()


root = tk.Tk()
app = Window(root)
root.wm_title("Passgen")
root.geometry("350x320")
root.mainloop()
