import tkinter as tk
from tkinter import Toplevel

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

# Центрируем окно на экране (опционально)
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# --- Переменные ---
current_player = "X"
buttons = []

# --- Функция для начала игры ---
def start_game(first_player):
    global current_player
    current_player = first_player
    update_status_label()

# --- Проверка на победителя ---
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

# --- Проверка на ничью ---
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# --- Сброс игры ---
def reset_game():
    global current_player
    current_player = starting_player_var.get()
    update_status_label()
    for row in buttons:
        for btn in row:
            btn.config(text="")

# --- Показываем сообщение с фиксированной шириной ---
def show_result(title, message):
    result_window = Toplevel(window)
    result_window.title(title)
    result_window.geometry("300x100")
    result_window.resizable(False, False)

    # Центрируем относительно основного окна
    window_x = window.winfo_x()
    window_y = window.winfo_y()
    pos_x = window_x + (window.winfo_width() // 2) - (250 // 2)
    pos_y = window_y + (window.winfo_height() // 2) - (100 // 2)
    result_window.geometry(f"+{pos_x}+{pos_y}")

    msg = tk.Label(result_window, text=message, font=("Arial", 14), justify="center")
    msg.pack(pady=20)

    btn = tk.Button(result_window, text="OK", command=lambda: [result_window.destroy(), reset_game()])
    btn.pack()

# --- Обработчик клика по кнопке ---
def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        show_result("Результат игры", f"Игрок {current_player} победил!")
        return

    if check_draw():
        show_result("Результат игры", "Ничья!")
        return

    # Смена игрока
    current_player = "0" if current_player == "X" else "X"
    update_status_label()

# --- Обновление метки статуса ---
def update_status_label():
    status_label.config(text=f"Ходит: {current_player}")

# --- Верхняя панель ---
top_frame = tk.Frame(window)
top_frame.grid(row=0, column=0, pady=10)

# --- Метка статуса ---
status_label = tk.Label(top_frame, text="", font=("Arial", 14))
status_label.pack()

# --- Радиокнопки для выбора первого игрока ---
starting_player_var = tk.StringVar(value="X")

def on_radio_change():
    global current_player
    current_player = starting_player_var.get()
    print("Выбранный первый игрок:", starting_player_var.get())
    update_status_label()
    pass  # просто обновляем значение, оно используется при сбросе

radio_frame = tk.Frame(top_frame)
radio_frame.pack()

tk.Radiobutton(radio_frame, text="Первый: X", variable=starting_player_var,
               value="X", command=on_radio_change).pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="Первый: O", variable=starting_player_var,
               value="0", command=on_radio_change).pack(side=tk.LEFT)

# --- Кнопка сброса ---
reset_button = tk.Button(top_frame, text="Сбросить игру", command=reset_game)
reset_button.pack(pady=5)

# --- Создаем фрейм для игрового поля и центрируем его ---
frame = tk.Frame(window)
frame.grid(row=1, column=0)

window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=0)
window.grid_columnconfigure(0, weight=1)

# Конфигурация строк и колонок внутри frame
for i in range(3):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

# --- Создание кнопок ---
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
        row.append(btn)
    buttons.append(row)

# --- Запуск игры с начальным игроком ---
# reset_game()
# update_status_label()  # гарантируем обновление метки сразу
# window.after(100, lambda: [reset_game(), update_status_label()])

# --- Отложенное выполнение reset_game(), чтобы убедиться, что всё загружено ---
def delayed_start():
    reset_game()
    update_status_label()

window.after(100, delayed_start)  # Выполняем через 100 мс

window.mainloop()