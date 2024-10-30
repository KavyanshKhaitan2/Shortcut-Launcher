import pathlib

# ConfigStart
SHORTCUTS_DIR = pathlib.Path(__file__).parent / "links/"
GUI_TITLE_TEXT = "Select server to start"
GUI_TITLE_FONT_SIZE = 15
# ConfigEnd

import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
import os
from functools import partial
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(GUI_TITLE_TEXT)
        ttk.Label(self.root, text=GUI_TITLE_TEXT, font=font.Font(size=GUI_TITLE_FONT_SIZE)).grid(row=0, column=0, columnspan=999, sticky='n')
        dirlist = os.listdir(SHORTCUTS_DIR)
        full_path_dirlist = [SHORTCUTS_DIR/file for file in dirlist]
        print(full_path_dirlist)
        
        for i, (filename, path) in enumerate(zip(dirlist, full_path_dirlist)):
            ttk.Button(self.root, text='.'.join(filename.split('.')[0:-1]), command=partial(self.start_file, path), width=50).grid(row=i+5)
        ttk.Button(self.root, text='=== EXIT ===', command=self.root.destroy, width=50).grid(row=i+99, pady=10, padx=5)
    
    def start_file(self, path):
        try:
            os.startfile(path)
            self.root.quit()
        except Exception as e:
            messagebox.showerror("Exception at os.startfile(path)", f"{e}\n\nThe program hit an unhandlable exeption.\nThe program will now restart.")
            self.root.destroy()
            App().run()
        
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    App().run()