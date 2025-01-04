import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Canvas
from tkinter import font

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, 'end')
        folder_entry.insert(0, folder_path)

def change_extensions():
    folder = folder_entry.get()
    new_extension = format_entry.get().strip()

    if not folder:
        messagebox.showerror("Ошибка", "Выберите папку.")
        return

    if not new_extension:
        messagebox.showerror("Ошибка", "Укажите новый формат.")
        return

    if not new_extension.startswith("."):
        new_extension = "." + new_extension

    try:
        files = os.listdir(folder)
        for file in files:
            old_path = os.path.join(folder, file)
            if os.path.isfile(old_path):
                name, _ = os.path.splitext(file)
                new_path = os.path.join(folder, name + new_extension)
                os.rename(old_path, new_path)

        messagebox.showinfo("Успех", "Расширения файлов успешно изменены.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Создание окна
root = Tk()
root.title("Изменение формата файлов")
root.geometry("500x250")
root.configure(bg="#F7F7F7")

# Установка шрифта и цветов
custom_font = font.Font(family="Comic Sans MS", size=11)
label_bg_color = "#FFFFFF"
label_fg_color = "#4A4A4A"
button_bg_color = "#6FA3EF"
button_fg_color = "#FFFFFF"
entry_bg_color = "#E8E8E8"
entry_fg_color = "#333333"

# Расположение элементов в процентных координатах
Label(root, text="Выберите папку:", bg=label_bg_color, fg=label_fg_color, font=custom_font).place(relx=0.5, rely=0.2, anchor="center")
folder_entry = Entry(root, width=40, bg=entry_bg_color, fg=entry_fg_color, font=custom_font, relief="flat")
folder_entry.place(relx=0.5, rely=0.3, anchor="center")
Button(root, text="Обзор", command=browse_folder, bg=button_bg_color, fg=button_fg_color, font=custom_font, relief="flat", padx=10, pady=5).place(relx=0.85, rely=0.3, anchor="center")

Label(root, text="Новый формат (например, .txt):", bg=label_bg_color, fg=label_fg_color, font=custom_font).place(relx=0.5, rely=0.5, anchor="center")
format_entry = Entry(root, width=40, bg=entry_bg_color, fg=entry_fg_color, font=custom_font, relief="flat")
format_entry.place(relx=0.5, rely=0.6, anchor="center")

# Кнопка выполнения
Button(root, text="Изменить расширения", command=change_extensions, bg=button_bg_color, fg=button_fg_color, font=custom_font, relief="flat", padx=10, pady=5).place(relx=0.5, rely=0.8, anchor="center")

# Запуск окна
root.mainloop()
