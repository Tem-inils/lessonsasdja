import tkinter as tk
from tkinter import PhotoImage


def show_heart():
    heart_label = tk.Label(root, image=heart_image)
    heart_label.pack()


# Создаем основное окно
root = tk.Tk()
root.title("Сердечко GUI")

# Загружаем изображение сердечка (замените путь к файлу на свой)
heart_image = PhotoImage(file="ac5476233b74f30001f41756e2319c14.png")

# Создаем кнопку
button = tk.Button(root, text="Покажи сердечко", command=show_heart)
button.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
