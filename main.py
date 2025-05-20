import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x300")

# Центрируем окно на экране (опционально)
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

current_player = "X"
buttons = []

# Создаем фрейм для игрового поля и размещаем его по центру
frame = tk.Frame(window)
frame.grid(row=1, column=1)

# Делаем так, чтобы фрейм был по центру окна
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Конфигурируем строки и колонки внутри frame для равномерного распределения
for i in range(3):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

def check_winner():
   for i in range(3):
       if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
           return True
       if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
           return True

   if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
       return True
   if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
       return True

   return False


def on_click(row, col):
   global current_player

   if buttons[row][col]['text'] != "":
       return

   buttons[row][col]['text'] = current_player

   if check_winner():
       messagebox.showinfo("Игра окончена",f"Игрок {current_player} победил!")

   current_player = "0" if current_player == "X" else "X"


for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
       btn.grid(row=i, column=j)
       row.append(btn)
   buttons.append(row)


window.mainloop()