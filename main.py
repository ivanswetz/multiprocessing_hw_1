import os
import shutil
from multiprocessing import Process
from threading import Thread
from tkinter import Tk, messagebox, filedialog
from tkinter.ttk import Frame, Label, Entry, Button, Style
import tkinter as tk
import tkinter.font as tkfont
def choose_dir(text_widget):
 file_path = filedialog.askdirectory(title="Виберіть файл")
 text_widget.delete(0, tk.END)
 text_widget.insert(0, file_path)

def archive_dir(opened_dir_path: str):
    processes = []
    for included_element_name in os.listdir(opened_dir_path):
        included_element_path = os.path.join(opened_dir_path, included_element_name)
        if os.path.isdir(included_element_path):
            p = Process(target=shutil.make_archive, kwargs={"base_name": included_element_path, "format": "zip", "root_dir": opened_dir_path, "base_dir": included_element_name})
            p.start()
            processes.append(p)
    for p in processes:
        p.join()
    messagebox.showinfo("Архівовано !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
def create_winodw():
    # --------------------------------------------------------------------
    # Вікно
    root = Tk()
    root.title("Архівування папок")
    root.resizable(True, True)
    # Рамка всередині вікна
    frame = Frame(root, padding=12)
    frame.pack(fill="both", expand=True)
    # --------------------------------------------------------------------
    # Шрифт
    FONT = tkfont.Font(family="Segoe UI", size=12)
    style = Style()
    style.configure("TButton", font=FONT)
    style.configure("TLabel", font=FONT)
    # --------------------------------------------------------------------
    # Підпис
    label1 = Label(frame, text="Шлях до існуючої папки:")
    label1.grid(row=0, column=0, sticky="w", pady=(0, 6))
    # Текстове поле 1
    entry1 = Entry(frame, width=60, font=FONT)
    entry1.grid(row=1, column=0, sticky="w", padx=(0, 6))
    # Кнопка 1
    btn1 = Button(frame, text="Вибрати Папку ", command=lambda: choose_dir(entry1))
    btn1.grid(row=1, column=2, sticky="e")
    # --------------------------------------------------------------------
    # Кнопка 3
    btn3 = Button(frame, text="Архівувати", command=lambda: Thread(target=archive_dir, args=(entry1.get(),)).start())
    btn3.grid(row=4, column=0, sticky="w", pady=(24, 0))
    # --------------------------------------------------------------------
    root.mainloop()

if __name__ == "__main__":
    print("Start")
    create_winodw()