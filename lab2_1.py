import pymongo
from tkinter import Tk, Label, Entry, Button, Listbox

# Подключение к MongoDB
client = pymongo.MongoClient('localhost')
database = client['22307']
collection_name = database["Chekarev-football_data"]

# Оконное приложение
class FootballApp:
    def __init__(self, master):
        self.master = master
        master.title("Football Database")

        self.label_key = Label(master, text="Key:")
        self.label_key.grid(row=0, column=0)

        self.entry_key = Entry(master)
        self.entry_key.grid(row=0, column=1)

        self.label_value = Label(master, text="Value:")
        self.label_value.grid(row=1, column=0)

        self.entry_value = Entry(master)
        self.entry_value.grid(row=1, column=1)

        self.add_button = Button(master, text="Add Key-Value", command=self.add_key_value)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.save_button = Button(master, text="Save Document", command=self.save_document)
        self.save_button.grid(row=3, column=0, columnspan=2)

        self.show_button = Button(master, text="Show Documents", command=self.show_documents)
        self.show_button.grid(row=4, column=0, columnspan=2)

        self.listbox = Listbox(master)
        self.listbox.grid(row=5, column=0, columnspan=2)

    def add_key_value(self):
        # Добавление ключ-значение в текущий документ
        key = self.entry_key.get()
        value = self.entry_value.get()
        # Добавьте код для добавления ключ-значение в текущий документ

    def save_document(self):
        # Сохранение текущего документа в базе данных
        # Добавьте код для создания нового документа в базе данных
        None
    def show_documents(self):
        # Показать все документы в списке
        # Добавьте код для запроса всех документов и отображения их в списке
        None
# Создание объекта приложения
root = Tk()
app = FootballApp(root)

# Запуск оконного приложения
root.mainloop()
