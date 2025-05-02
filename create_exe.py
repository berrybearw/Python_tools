import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filepath:
        file_path_var.set(filepath)

def build_exe():
    filepath = file_path_var.get()
    if not filepath or not filepath.endswith(".py"):
        messagebox.showwarning("Warning", "Please select a valid .py file.")
        return

    try:
        # 切換到 .py 所在資料夾再執行 pyinstaller
        workdir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)

        subprocess.run(
            ["pyinstaller", "--onefile", filename],
            cwd=workdir,
            check=True
        )

        messagebox.showinfo("Success", f"EXE built in:\n{os.path.join(workdir, 'dist')}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Build failed:\n{e}")

# 建立 UI
root = tk.Tk()
root.title("Python to EXE Builder")
root.geometry("500x200")

file_path_var = tk.StringVar()

tk.Label(root, text="Python File:").pack(pady=10)
tk.Entry(root, textvariable=file_path_var, width=60).pack()
tk.Button(root, text="Browse", command=select_file).pack(pady=5)
tk.Button(root, text="Build EXE", command=build_exe, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
