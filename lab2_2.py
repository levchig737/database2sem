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


class AggregationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Football Data Search App")

        self.key_label = Label(master, text="Ключ:")
        self.key_label.grid(row=0, column=0)

        self.comparison_label = Label(master, text="Сравнение:")
        self.comparison_label.grid(row=1, column=0)

        self.value_label = Label(master, text="Значение:")
        self.value_label.grid(row=2, column=0)

        self.key_entry = Entry(master)
        self.key_entry.grid(row=0, column=1)

        self.comparison_var = StringVar()
        self.comparison_entry = ttk.Combobox(master, textvariable=self.comparison_var, values=['>', '>=', '=', '<=', '<', '!='])
        self.comparison_entry.grid(row=1, column=1)

        self.value_entry = Entry(master)
        self.value_entry.grid(row=2, column=1)

        self.collection_var = StringVar()
        self.collection_entry = ttk.Combobox(master,textvariable=self.collection_var ,values=collections_names)
        self.collection_entry.grid(row=3, column=0, columnspan=1)
        self.collection_entry.bind("<<ComboboxSelected>>", lambda event: self.choose_current_collection())

        self.search_button = Button(master, text="Выполнить запрос", command=self.perform_search)
        self.search_button.grid(row=4, column=0, columnspan=2)

        self.current_collection_label = Label(master, text="Текущая коллекция:")
        self.current_collection_label.grid(row=5, column=0)
        
        self.current_collection_label2 = Label(master, text="Футбольные команды")
        self.current_collection_label2.grid(row=5, column=1)

        self.documents_text = Text(master, width=90, height=20, state="disabled")
        self.documents_text.grid(row=7, column=0, columnspan=2, padx=40, pady=10)

        self.current_collection = football_collection


    def choose_current_collection(self):
        cur_collection = self.collection_var.get()
        if (cur_collection == collections_names[1]):
            self.current_collection = game_collection
            self.current_collection_label2.config(text=collections_names[1])
        else:
            self.current_collection = football_collection
            self.current_collection_label2.config(text=collections_names[0])

        print(self.current_collection)


    def show_documents(self, query):
        self.documents_text.config(state=NORMAL)  # Включаем режим редактирования
        self.documents_text.delete(1.0, END)  # Очищаем Text перед выводом новых данных
        
        for document in self.current_collection.find(query):
            self.documents_text.insert(END, json.dumps({x: document[x] for x in document if x not in "_id"}, indent=4, ensure_ascii=False) +  '\n_______________________________________\n\n')
 
        self.documents_text.config(state="disabled")


    def perform_search(self):
        key = self.key_entry.get()
        comparison = self.comparison_var.get()
        value = self.value_entry.get()

        # Преобразование значения в соответствующий тип (int, float, str)
        try:
            if '.' in value:
                value = float(value)
            else:
                value = int(value)
        except ValueError:
            pass  # Если не удалось преобразовать в число, оставляем как строку
        
        # Определение оператора сравнения
        if comparison == '>':
            query = {key: {'$gt': value}}
        elif comparison == '>=':
            query = {key: {'$gte': value}}
        elif comparison == '=':
            query = {key: {'$eq': value}}
        elif comparison == '<=':
            query = {key: {'$lte': value}}
        elif comparison == '<':
            query = {key: {'$lt': value}}
        elif comparison == '!=':
            query = {key: {'$ne': value}}
        else:
            # Обработка некорректного сравнения
            print("Некорректное сравнение")
                
        # Выполнение запроса к коллекции
        self.show_documents(query)



# Оконное приложение для агрегации данных
class AggregationApp2:
    def __init__(self, master):
        self.master = master
        self.master.title("Aggregate Football Data")

        self.collection_var = StringVar()
        self.collection_entry = ttk.Combobox(master,textvariable=self.collection_var ,values=collections_names)
        self.collection_entry.grid(row=0, column=0, columnspan=2)
        self.collection_entry.bind("<<ComboboxSelected>>", lambda event: self.choose_current_collection(event))

        self.current_collection_label = Label(master, text="Текущая коллекция:")
        self.current_collection_label.grid(row=1, column=0)
        
        self.current_collection_label2 = Label(master, text="Футбольные команды")
        self.current_collection_label2.grid(row=1, column=1)

        self.command_label = Label(master, text="Команда для агрегации:")
        self.command_label.grid(row=2, column=0)

        self.command_entry =  Text(master, height=10, width=70)
        self.command_entry.grid(row=2, column=1)

        self.aggregate_button = Button(master, text="Выполнить агрегацию", command=self.perform_aggregation)
        self.aggregate_button.grid(row=3, column=0, columnspan=2)

        self.documents_text = Text(master, width=90, height=20, state="disabled")
        self.documents_text.grid(row=7, column=0, columnspan=2, padx=40, pady=10)

        self.current_collection = football_collection
    

    def choose_current_collection(self, event):
        cur_collection = self.collection_var.get()
        if (cur_collection == collections_names[1]):
            self.current_collection = game_collection
            self.current_collection_label2.config(text=collections_names[1])
        else:
            self.current_collection = football_collection
            self.current_collection_label2.config(text=collections_names[0])

        print(self.current_collection)



    def show_documents(self,result):
        self.documents_text.config(state=NORMAL)  # Включаем режим редактирования
        self.documents_text.delete(1.0, END)  # Очищаем Text перед выводом новых данных
        
        for document in result:
            self.documents_text.insert(END, json.dumps({x: document[x] for x in document if x not in "_id"}, indent=4, ensure_ascii=False) +  '\n_______________________________________\n\n')
 
        self.documents_text.config(state="disabled")
       

    def perform_aggregation(self):
        query_text = self.command_entry.get("1.0", END)

        try:
            # Попытка выполнить агрегацию
            pipeline = eval(query_text)
            results = self.current_collection.aggregate(pipeline)

            # Вывод результатов
            self.show_documents(results)

        except Exception as e:
            # Обработка ошибок
            self.documents_text.config(state=NORMAL)  # Включаем режим редактирования
            self.documents_text.delete(1.0, END)  # Очищаем Text перед выводом новых данных
            self.documents_text.insert(END, f"Ошибка выполнения запроса: {str(e)}")
            self.documents_text.config(state="disabled")

    ### Примеры запросов агрегации:
[{"$sort": {"_id": -1}}, {"$limit": 1}] # вывод последнего документа коллекции

# Вывод всех футболистов и их кол-во забитых голов во всех играх
[
    {"$unwind": {"path": "$goals", "preserveNullAndEmptyArrays": True}},
    {"$match": {"goals.author": {"$exists": True}}},
    {"$group": {"_id": "$goals.author", "total_goals": {"$sum": 1}}},
    {"$project": {"_id": 0, "player_name": "$_id", "total_goals": 1}}
]

# Вывод количества игроков, котоыре забыли  больше 2 голов во всех играх
[
    {"$unwind": {"path": "$goals", "preserveNullAndEmptyArrays": True}},
    {"$match": {"goals.author": {"$exists": True}}},
    {"$group": {"_id": "$goals.author", "total_goals": {"$sum": 1}}},
    {"$match": {"total_goals": {"$gt": 2}}},
    {"$group": {"_id": None, "total_players": {"$sum": 1}}},
    {"$project": {"_id": 0, "total_players": "$total_players"}}
]



# Запуск оконных приложений)

root3 = Tk()
aggregation_app = AggregationApp2(root3)
root3.geometry('800x600')

root3.mainloop()
