import pymongo
from tkinter import *
from tkinter import ttk
import json

# Подключение
client = pymongo.MongoClient('localhost')
database = client['22307']

# Создание коллекции
football_collection = database["chekarev-football_data"]
game_collection = database["chekarev-game_data"]
collections_names = ['Футбольные команды', 'Игры']


# Оконное приложение для ввода и отображения информации
class FootballApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Football Database App")

        self.key_label = Label(master, text="Ключ:")
        self.key_label.grid(row=0, column=0)

        self.value_label = Label(master, text="Значение:")
        self.value_label.grid(row=1, column=0)

        self.key_entry = Entry(master)
        self.key_entry.grid(row=0, column=1)

        self.value_entry = Entry(master)
        self.value_entry.grid(row=1, column=1)

        self.collection_var = StringVar()
        self.collection_entry = ttk.Combobox(master,textvariable=self.collection_var ,values=collections_names)
        self.collection_entry.grid(row=2, column=0, columnspan=2)
        self.collection_entry.bind("<<ComboboxSelected>>", lambda event: self.choose_current_collection())

        self.add_button = Button(master, text="Добавить ключ-значение", command=self.add_key_value)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.save_button = Button(master, text="Сохранить документ", command=self.save_document)
        self.save_button.grid(row=4, column=0, columnspan=2)

        self.show_button = Button(master, text="Показать документы", command=self.show_documents)
        self.show_button.grid(row=5, column=0, columnspan=2)

        self.current_collection_label = Label(master, text="Текущая коллекция:")
        self.current_collection_label.grid(row=6, column=0)
        
        self.current_collection_label2 = Label(master, text="Футбольные команды")
        self.current_collection_label2.grid(row=6, column=1)

        self.documents_text = Text(master, width=90, height=20, state="disabled")
        self.documents_text.grid(row=7, column=0, columnspan=2, padx=40, pady=10)




        self.current_document = {}
        self.current_collection = football_collection


    def view_current_document(self):
        self.documents_text.config(state=NORMAL)  # Включаем режим редактирования
        
        self.documents_text.delete(1.0, END)  # Очищаем Text перед выводом новых данных
        self.documents_text.insert(END, json.dumps({x: self.current_document[x] for x in self.current_document if x not in "_id"}, indent=4, ensure_ascii=False))
        
        self.documents_text.config(state="disabled")


    def choose_current_collection(self):
        cur_collection = self.collection_var.get()
        if (cur_collection == collections_names[1]):
            self.current_collection = game_collection
            self.current_collection_label2.config(text=collections_names[1])
        else:
            self.current_collection = football_collection
            self.current_collection_label2.config(text=collections_names[0])

        print(self.current_collection)


    def add_key_value(self):
        key = self.key_entry.get()
        
        value = self.value_entry.get()
        value_new = value
        try:
            value_new = int(value)
        except:
            pass

        value = value_new
        key = key.split('.')

        if (len(key) == 1):
            self.current_document[key[0]] = value
            self.view_current_document()
            return

        doc_dict = {key[1]:value}

        # Если значение по ключу нет, то создаем список
        if (key[0] not in self.current_document):
           arr = [doc_dict]
           self.current_document[key[0]] = arr
        else:
            # Пробегаемся по всему списку
            for i in range(len(self.current_document[key[0]])):
                # Ищем, где нет ключа
                if key[1] not in self.current_document[key[0]][i]:
                    self.current_document[key[0]][i][key[1]] = value
                    self.view_current_document()
                    return
                
            # Если все-таки везде есть ключ, то создаем новый элемент
            self.current_document[key[0]].append(doc_dict)
            self.view_current_document()

        self.view_current_document()
        

    def save_document(self):
        if self.current_document:
            self.current_collection.insert_one(self.current_document)
            self.current_document = {}

    def show_documents(self):
        self.documents_text.config(state=NORMAL)  # Включаем режим редактирования
        self.documents_text.delete(1.0, END)  # Очищаем Text перед выводом новых данных
        
        for document in self.current_collection.find():
            self.documents_text.insert(END, json.dumps({x: document[x] for x in document if x not in "_id"}, indent=4, ensure_ascii=False) +  '\n_______________________________________\n\n')
 
        self.documents_text.config(state="disabled")


# Запуск оконных приложений
root1 = Tk()
root1.geometry('800x600')
football_app = FootballApp(root1)

root1.mainloop()
