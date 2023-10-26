import tkinter as tk
import redis

# подключение к Redis
connection = redis.Redis(host='localhost')


def decode(settings, key):
    return settings[key].decode()

def save_settings():
    selected_user = user.get(user.curselection())
    font = text1.get()
    font_size = text2.get()
    font_color = text3.get()
    font_style = text4.get()
    
    settings = {
        'font': font,
        'font_size': font_size,
        'font_color': font_color,
        'font_style': font_style,
    }

    # хэшируем
    connection.hmset(selected_user, settings)

def update_label_text():
    # Обновляем надпись с учетом текущих настроек
    selected_user = user.get(user.curselection())
    settings = connection.hgetall(selected_user)
    print(settings) #отладочный вывод

    # Применяем настройки к тексту в надписи
    formatted_text = 'This is a sample text.'
    if settings:
        custom_font = (decode(settings, b'font'), decode(settings, b'font_size'), decode(settings, b'font_style'))
        font_color = decode(settings, b'font_color')
        
        label.config(text=formatted_text, font=custom_font, foreground=font_color)
    else:
        label.config(text=formatted_text, font='', foreground='black')

root = tk.Tk()
root.title('Настройки текстового сообщения')
root.geometry('600x400')

label2 = tk.Label(root, text='Размер шрифта')
label2.grid(row=1, column=1)
text2 = tk.Entry(root)
text2.grid(row=1, column=2)
label1 = tk.Label(root, text='Название шрифта')
label1.grid(row=2, column=1)
text1 = tk.Entry(root)
text1.grid(row=2, column=2)
label3 = tk.Label(root, text='Цвет шрифта')
label3.grid(row=3, column=1)
text3 = tk.Entry(root)
text3.grid(row=3, column=2)
label4 = tk.Label(root, text='Начертание шрифта')
label4.grid(row=4, column=1)
text4 = tk.Entry(root)
text4.grid(row=4, column=2)

user = tk.Listbox(root, width=30, height=3)
user.insert(0, 'Пользователь №1')
user.insert(1, 'Пользователь №2')
user.insert(2, 'Пользователь №3')
user.grid(row=2, column=3)


do_it = tk.Button(root, text='Сохранить настройки', command=save_settings)
do_it.grid(row=4, column=3)

label = tk.Label(root, text='This is a sample text.')
label.grid(row=6, column=1, columnspan=3)

user.bind('<<ListboxSelect>>', lambda event: update_label_text())

root.mainloop()
