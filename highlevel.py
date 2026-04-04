from tkinter import Tk, Button, Label
from tkinter import ttk

# function that creates a window with tabs and a Start button

def start_tab_button():
    root = Tk()
    root.title("Start Tab Button")
    root.geometry("400x280")

    notebook = ttk.Notebook(root)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    notebook.add(tab1, text="Start")
    notebook.add(tab2, text="Info")
    notebook.pack(expand=True, fill="both", padx=10, pady=10)

    title_label = Label(tab1, text="Press Start to go to Tab 2", font=("Arial", 12))
    title_label.pack(pady=18)

    def on_start():
        status_label.config(text="Started! Showing Tab 2.")
        notebook.select(tab2)

    start_button = Button(tab1, text="Start", command=on_start, width=12)
    start_button.pack(pady=10)

    status_label = Label(tab1, text="", font=("Arial", 10))
    status_label.pack(pady=6)

    Label(tab2, text="This is Tab 2 content.", font=("Arial", 12)).pack(pady=20)
    Button(tab2, text="Back to Start", command=lambda: notebook.select(tab1), width=14).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    start_tab_button()

 