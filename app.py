import tkinter as tk # GUI library
from tkinter.filedialog import askopenfilename, asksaveasfilename # File management
from tkinter import ttk

def open_file(window, text_editor):
    file_path = askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    if not file_path:
        return False
    text_editor.delete(1.0, tk.END) # Clear all text
    with open(file_path, "r") as f:
        content = f.read()
        text_editor.insert(tk.END, content) # Replaces text

    window.title(f"Arquivo em: {file_path}")

def save_file(window, text_editor):
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")]) # defaultextension = always saves as .txt

    if not file_path:
        return False
    with open(file_path, "w") as f:
        content = text_editor.get(1.0, tk.END) # Gets all text from the file
        f.write(content) # Saves file

def main():
    # =========== #
    # Window settings

    window = tk.Tk()
    window.title("Notepad--")
    window.resizable(False, False)
    window.geometry("640x480")

    # =========== #
    # Widgets

    text_editor = tk.Text(window, font=("Arial", 14), padx = 3)
    text_editor.grid(row = 1, column = 0)
    
    # =========== #
    # Buttons

    btn_frame = tk.Frame(window, bd = 1)
    open_btn = tk.Button(btn_frame, text="Abrir", relief=tk.FLAT, command = lambda: open_file(window, text_editor))
    save_btn = tk.Button(btn_frame, text="Salvar", relief=tk.FLAT, command = lambda: save_file(window, text_editor))
    font_btn = tk.Button(btn_frame, text="Fonte", relief=tk.FLAT, command = lambda: font_selector(text_editor))

    open_btn.grid(row = 0, column = 0)
    save_btn.grid(row = 0, column = 1)
    font_btn.grid(row = 0, column = 2)
    btn_frame.grid(row = 0, column= 0, sticky="W")

    def font_selector(text_editor):
        new_window = tk.Tk()
        new_window.geometry("320x240")
        new_window.title("Fonte")

        ttk.Label(new_window, text = "Selecione a fonte: ").grid(row = 2, column = 1, padx=20, pady=10)

        def change_font():
            font = font_box.get()
            text_editor.configure(font=(f"{font}", 14))

        font_box = ttk.Combobox(new_window)
        font_box['values'] = (
        'Arial',
        'Courier New',
        'Tahoma',
        'Times New Roman',
        'Comic Sans MS'
                )
        font_box.grid(row = 2, column = 2)
        font_box.current(0)
        
        send = tk.Button(new_window, text = "Ok", relief=tk.GROOVE, command= lambda: change_font())
        send.grid(row = 6, column=2)

    # =========== #
    # Main loop

    window.bind("<Control-o>", lambda x: open_file(window, text_editor)) # KEY SHORTCUTS
    window.bind("<Control-s>", lambda x: save_file(window, text_editor))
    window.mainloop()

if __name__ == '__main__':
    main()