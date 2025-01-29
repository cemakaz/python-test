import tkinter as tk

def say_hello():
    window = tk.Tk()
    window.title("hello")

    label = tk.Label(window, text="Hello")
    label.pack(pady=20)

    window.mainloop()

if __name__ == '__main__':
    say_hello()
