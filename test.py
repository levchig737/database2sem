import tkinter as tk
from tkinter import ttk
import redis

# Создание соединения с Redis
connection = redis.Redis(host='localhost')

# Функция для добавления баллов
def add_score():
    sportsperson = sportsperson_var.get()
    judge = judge_var.get()
    score = int(score_entry.get())

    # Создаем ключ в виде "sportsperson:judge" и сохраняем оценку
    key = f"sportsperson:{sportsperson}:{judge}"
    connection.hincrby(key, "score", score)
    update_rankings()

# Функция для обновления рейтинга
def update_rankings():
    rankings = get_rankings()
    rankings_listbox.delete(0, tk.END)
    for sportsperson, score in rankings:
        rankings_listbox.insert(tk.END, f'{sportsperson}: {score}')

# Функция для получения рейтинга
def get_rankings():
    # Получите всех спортсменов из базы данных
    sportspersons = set()
    for key in connection.keys('sportsperson:*'):
        sportsperson = key.decode().split(':')[1]
        sportspersons.add(sportsperson)

    # Вычислите сумму баллов для каждого спортсмена
    rankings = {}
    for sportsperson in sportspersons:
        total_score = sum([int(connection.hget(key, "score")) for key in connection.keys(f"sportsperson:{sportsperson}:*")])
        rankings[sportsperson] = total_score

    # Отсортируйте рейтинг по убыванию
    sorted_rankings = sorted(rankings.items(), key=lambda x: x[1], reverse=True)
    return sorted_rankings

# Создание окна
root = tk.Tk()
root.title("Спортивный монитор")
root.geometry('300x400')

# Создание и настройка виджетов
sportsperson_label = tk.Label(root, text="Спортсмен:")
sportsperson_var = tk.StringVar()
sportsperson_combobox = ttk.Combobox(root, textvariable=sportsperson_var, values=["Спортсмен 1", "Спортсмен 2"])
judge_label = tk.Label(root, text="Судья:")
judge_var = tk.StringVar()
judge_combobox = ttk.Combobox(root, textvariable=judge_var, values=["Судья 1", "Судья 2"])
score_label = tk.Label(root, text="Баллы:")
score_entry = tk.Entry(root)
save_button = tk.Button(root, text="Сохранить баллы", command=add_score)
rankings_label = tk.Label(root, text="Рейтинг спортсменов:")
rankings_listbox = tk.Listbox(root)

# Размещение виджетов на форме
sportsperson_label.grid(row=0, column=0)
sportsperson_combobox.grid(row=0, column=1)
judge_label.grid(row=1, column=0)
judge_combobox.grid(row=1, column=1)
score_label.grid(row=2, column=0)
score_entry.grid(row=2, column=1)
save_button.grid(row=3, column=0, columnspan=2)
rankings_label.grid(row=4, column=0, columnspan=2)
rankings_listbox.grid(row=5, column=0, columnspan=2)

# Запуск приложения
root.mainloop()
