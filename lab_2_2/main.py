import pymongo
import tkinter as tk
from tkinter import ttk
import json

# Подключение
client = pymongo.MongoClient('localhost')
database = client['22307']
# Создание коллекции
collection = database["chekarev-shop_data"]

def save_document():
    shop_data = \
    [
    {
        "product_name": "Ноутбук SuperBook",
        "category": "Ноутбук",
        "manufacturer": "SuperTech",
        "price": 899.99,
        "characteristics": {
            "screen_size": "14 дюймов",
            "processor": "Intel Core i5",
            "memory": "8 ГБ RAM",
            "storage": "256 ГБ SSD",
            "color": "серый"
        },
        "customer_info": [
            {
                "customer_name": "Анна Кирьянен",
                "purchase_date": "2023-01-10",
                "review": "Отличный выбор для работы и развлечений",
                "delivery_service": "ExpressTech"
            },
            {
                "customer_name": "Павел Смирнов",
                "purchase_date": "2023-02-05",
                "review": "Быстрая доставка, надежный ноутбук",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Ноутбук ProBook X1",
        "category": "Ноутбук",
        "manufacturer": "ProTech",
        "price": 1099.99,
        "characteristics": {
            "screen_size": "15.6 дюймов",
            "processor": "AMD Ryzen 7",
            "memory": "16 ГБ RAM",
            "storage": "512 ГБ SSD",
            "color": "серебристый"
        },
        "customer_info": [
            {
                "customer_name": "Евгений Козлов",
                "purchase_date": "2023-03-15",
                "review": "Мощный процессор, стильный дизайн",
                "delivery_service": "ExpressTech"
            },
            {
                "customer_name": "Марина Семенова",
                "purchase_date": "2023-04-02",
                "review": "Большой объем памяти, удобный в использовании",
                "delivery_service": "TechExpress"
            }
        ]
    },
    {
        "product_name": "Ноутбук EliteBook Z2",
        "category": "Ноутбук",
        "manufacturer": "EliteTech",
        "price": 1299.99,
        "characteristics": {
            "screen_size": "13.3 дюйма",
            "processor": "Intel Core i7",
            "memory": "32 ГБ RAM",
            "storage": "1 ТБ SSD",
            "color": "черный"
        },
        "customer_info": [
            {
                "customer_name": "Анна Кирьянен",
                "purchase_date": "2023-03-20",
                "review": "Идеальный для профессионального использования",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Дмитрий Игнатьев",
                "purchase_date": "2023-04-18",
                "review": "Быстрый и надежный, высокая производительность",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Ноутбук UltraBook S3",
        "category": "Ноутбук",
        "manufacturer": "UltraTech",
        "price": 899.99,
        "characteristics": {
            "screen_size": "14 дюймов",
            "processor": "Intel Core i5",
            "memory": "8 ГБ RAM",
            "storage": "256 ГБ SSD",
            "color": "серый"
        },
        "customer_info": [
            {
                "customer_name": "Анна Кирьянен",
                "purchase_date": "2023-01-25",
                "review": "Легкий и компактный, отлично подходит для путешествий",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Артем Миронов",
                "purchase_date": "2023-02-10",
                "review": "Удобный и стильный, хорошая цена",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Ноутбук PowerBook G6",
        "category": "Ноутбук",
        "manufacturer": "PowerTech",
        "price": 999.99,
        "characteristics": {
            "screen_size": "15.6 дюйма",
            "processor": "AMD Ryzen 5",
            "memory": "16 ГБ RAM",
            "storage": "512 ГБ SSD",
            "color": "золотистый"
        },
        "customer_info": [
            {
                "customer_name": "Владимир Иванов",
                "purchase_date": "2023-03-05",
                "review": "Отличное соотношение цена-качество",
                "delivery_service": "ExpressTech"
            },
            {
                "customer_name": "Екатерина Кузнецова",
                "purchase_date": "2023-04-15",
                "review": "Высокая производительность, стильный дизайн",
                "delivery_service": "TechExpress"
            }
        ]
    },

    {
        "product_name": "Смартфон iPhone 13",
        "manufacturer": "Apple",
        "category": "Смартфон",
        "price": 899.99,
        "characteristics": {
            "display": "6.1 дюйма, Super Retina XDR",
            "camera": "12 МП + 12 МП",
            "battery": "3095 мАч",
            "storage": "256 ГБ",
            "color": "голубой"
        },
        "customer_info": [
            {
                "customer_name": "Михаил Петров",
                "purchase_date": "2023-03-15",
                "review": "iOS на высоте, отличная производительность",
                "delivery_service": "ExpressTech"
            },
            {
                "customer_name": "Анна Ковалева",
                "purchase_date": "2023-04-20",
                "review": "Прекрасная камера, стильный дизайн",
                "delivery_service": "TechExpress"
            }
        ]
    },
    {
        "product_name": "Смартфон Pixel 6",
        "manufacturer": "Google",
        "category": "Смартфон",
        "price": 699.99,
        "characteristics": {
            "display": "6.4 дюйма, OLED",
            "camera": "50 МП + 12 МП",
            "battery": "4600 мАч",
            "storage": "128 ГБ",
            "color": "черный"
        },
        "customer_info": [
            {
                "customer_name": "Татьяна Новикова",
                "purchase_date": "2023-03-20",
                "review": "Чистый Android, отличная камера",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Сергей Игнатов",
                "purchase_date": "2023-04-25",
                "review": "Долгая автономия, удобный дисплей",
                "delivery_service": "GoogleDelivery"
            }
        ]
    },
    {
        "product_name": "Смартфон OnePlus 9",
        "manufacturer": "OnePlus",
        "category": "Смартфон",
        "price": 749.99,
        "characteristics": {
            "display": "6.55 дюйма, Fluid AMOLED",
            "camera": "48 МП + 50 МП + 2 МП",
            "battery": "4500 мАч",
            "storage": "256 ГБ",
            "color": "серый"
        },
        "customer_info": [
            {
                "customer_name": "Наталья Соколова",
                "purchase_date": "2023-03-25",
                "review": "Быстрая зарядка, отличная производительность",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Артем Миронов",
                "purchase_date": "2023-04-02",
                "review": "Операционная система OxygenOS на высшем уровне",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Смартфон Mi 11",
        "manufacturer": "Xiaomi",
        "category": "Смартфон",
        "price": 649.99,
        "characteristics": {
            "display": "6.81 дюйма, AMOLED",
            "camera": "108 МП + 13 МП + 5 МП",
            "battery": "4600 мАч",
            "storage": "128 ГБ",
            "color": "зеленый"
        },
        "customer_info": [
            {
                "customer_name": "Анна Кирьянен",
                "purchase_date": "2023-04-05",
                "review": "Большой и красочный экран, отличная камера",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Владимир Попов",
                "purchase_date": "2023-04-18",
                "review": "Доступная цена, высокая производительность",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Смартфон Xperia 5 III",
        "manufacturer": "Sony",
        "category": "Смартфон",
        "price": 899.99,
        "characteristics": {
            "display": "6.1 дюйма, HDR OLED",
            "camera": "12 МП + 12 МП + 12 МП",
            "battery": "4500 мАч",
            "storage": "256 ГБ",
            "color": "синий"
        },
        "customer_info": [
            {
                "customer_name": "Денис Лебедев",
                "purchase_date": "2023-04-10",
                "review": "Превосходный экран, мощная камера",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Анастасия Семенова",
                "purchase_date": "2023-04-15",
                "review": "Удобный и стильный, отличное качество сборки",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Смартфон Redmi Note 10",
        "manufacturer": "Xiaomi",
        "category": "Смартфон",
        "price": 329.99,
        "characteristics": {
            "display": "6.43 дюйма, AMOLED",
            "camera": "48 МП + 8 МП + 2 МП",
            "battery": "5000 мАч",
            "storage": "64 ГБ",
            "color": "белый"
        },
        "customer_info": [
            {
                "customer_name": "Александра Кузнецова",
                "purchase_date": "2023-03-08",
                "review": "Отличный баланс цены и качества",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Василий Иванов",
                "purchase_date": "2023-03-12",
                "review": "Долгая автономия, быстрая доставка",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Наушники SoundWave",
        "category": "Наушники",
        "manufacturer": "AudioTech",
        "price": 79.99,
        "characteristics": {
            "type": "беспроводные",
            "features": ["шумоподавление", "басы высокого качества"],
            "color": "белый"
        },
        "customer_info": [
            {
                "customer_name": "Елена Васнецова",
                "purchase_date": "2023-01-18",
                "review": "Отличное звучание, удобные наушники",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Сергей Игнатов",
                "purchase_date": "2023-02-08",
                "review": "Хороший выбор за свою цену",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Наушники BassMaster 5000",
        "category": "Наушники",
        "manufacturer": "SoundTech",
        "price": 99.99,
        "characteristics": {
            "type": "беспроводные",
            "features": ["потрясающий бас", "активное шумоподавление"],
            "color": "черный"
        },
        "customer_info": [
            {
                "customer_name": "Александр Петров",
                "purchase_date": "2023-03-15",
                "review": "Басы просто огонь, отличные наушники для музыки",
                "delivery_service": "ExpressTech"
            },
            {
                "customer_name": "Ольга Козлова",
                "purchase_date": "2023-04-02",
                "review": "Отличное шумоподавление, удобные в ношении",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Наушники SonicWave X3",
        "category": "Наушники",
        "manufacturer": "AudioTech",
        "price": 129.99,
        "characteristics": {
            "type": "беспроводные",
            "features": ["высокое разрешение звука", "комфортная посадка"],
            "color": "синий"
        },
        "customer_info": [
            {
                "customer_name": "Ирина Новикова",
                "purchase_date": "2023-03-20",
                "review": "Отличный звук, долгое время работы батареи",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Андрей Семенов",
                "purchase_date": "2023-04-18",
                "review": "Комфортные наушники, отличное качество звука",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Наушники UltraSound Pro",
        "category": "Наушники",
        "manufacturer": "UltraTech",
        "price": 79.99,
        "characteristics": {
            "type": "проводные",
            "features": ["чистый звук", "легкий вес"],
            "color": "черный"
        },
        "customer_info": [
            {
                "customer_name": "Николай Соколов",
                "purchase_date": "2023-01-25",
                "review": "Прекрасное качество звука, удобные наушники",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Марина Миронова",
                "purchase_date": "2023-02-10",
                "review": "Легкие и удобные, отличное соотношение цена-качество",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Наушники HarmonySound E5",
        "category": "Наушники",
        "manufacturer": "HarmonyTech",
        "price": 89.99,
        "characteristics": {
            "type": "беспроводные",
            "features": ["высокая чувствительность микрофона", "стильный дизайн"],
            "color": "розовый"
        },
        "customer_info": [
            {
                "customer_name": "Екатерина Павлова",
                "purchase_date": "2023-03-05",
                "review": "Отличные для звонков, красивый дизайн",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Денис Семенов",
                "purchase_date": "2023-04-15",
                "review": "Хорошее сочетание цвета и качества звука",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Смарт-телевизор UltraVision",
        "category": "Телевизор",
        "manufacturer": "TechInnovations",
        "price": 799.99,
        "characteristics": {
            "screen_size": "55 дюймов, OLED",
            "resolution": "4K",
            "smart_features": ["Smart TV", "голосовое управление"],
            "color": "черный"
        },
        "customer_info": [
            {
                "customer_name": "Артем Михайлов",
                "purchase_date": "2023-03-05",
                "review": "Отличный телевизор, яркое изображение",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Людмила Козлова",
                "purchase_date": "2023-04-02",
                "review": "Умные функции работают на ура",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Смарт-телевизор ProVision X1",
        "category": "Телевизор",
        "manufacturer": "TechInnovations",
        "price": 999.99,
        "characteristics": {
            "screen_size": "65 дюймов, QLED",
            "resolution": "8K",
            "smart_features": ["Smart TV", "голосовое управление", "встроенный искусственный интеллект"],
            "color": "серебристый"
        },
        "customer_info": [
            {
                "customer_name": "Анна Петрова",
                "purchase_date": "2023-03-20",
                "review": "Великолепное изображение, множество умных функций",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Дмитрий Игнатьев",
                "purchase_date": "2023-04-18",
                "review": "Идеальный выбор для киноманов",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Смарт-телевизор Visionary Plus",
        "category": "Телевизор",
        "manufacturer": "InnovateTech",
        "price": 1199.99,
        "characteristics": {
            "screen_size": "75 дюймов, OLED",
            "resolution": "6K",
            "smart_features": ["Smart TV", "голосовое управление", "встроенный стример"],
            "color": "черный"
        },
        "customer_info": [
            {
                "customer_name": "Максим Соколов",
                "purchase_date": "2023-01-25",
                "review": "Большой экран, отличные цвета",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Алиса Новикова",
                "purchase_date": "2023-02-10",
                "review": "Умные функции удобны в использовании",
                "delivery_service": "ExpressTech"
            }
        ]
    },
    {
        "product_name": "Смарт-телевизор SmartView E2",
        "category": "Телевизор",
        "manufacturer": "ViewTech",
        "price": 899.99,
        "characteristics": {
            "screen_size": "55 дюймов, LED",
            "resolution": "4K",
            "smart_features": ["Smart TV", "голосовое управление"],
            "color": "черный"
        },
        "customer_info": [
            {
                "customer_name": "Екатерина Миронова",
                "purchase_date": "2023-03-05",
                "review": "Хорошее сочетание цена-качество",
                "delivery_service": "TechExpress"
            },
            {
                "customer_name": "Иван Семенов",
                "purchase_date": "2023-04-15",
                "review": "Прост в использовании, красочное изображение",
                "delivery_service": "ExpressTech"
            }
        ]
    }
    ]

    collection.delete_many({})

    for document in shop_data:
        collection.insert_one(document)
    print(len(shop_data))
    
# save_document()



class ProductQueryApp:
    listCategory = sorted(list(collection.distinct("category")))
    listCustomer = sorted(list(collection.distinct("customer_info.customer_name")))
    listColors = sorted(list(collection.distinct("characteristics.color")))
    listProducts = sorted(list(collection.distinct("product_name")))
    listDeliveries = sorted(list(collection.distinct("customer_info.delivery_service")))




    def __init__(self, master, collection):
        self.master = master
        self.master.title("Product Query App")

        self.collection = collection

        # Первый запрос
        self.category_label1 = tk.Label(self.master, text="Категория:")
        self.category_label1.grid(row=0, column=0, padx=10, pady=10)

        self.collection_var1 = tk.StringVar()
        self.collection_entry1 = ttk.Combobox(master,textvariable=self.collection_var1, values=self.listCategory)
        self.collection_entry1.grid(row=1, column=0)

        self.query_button_1 = tk.Button(self.master, text="1. Названия товаров по категории", command=self.get_product_names_by_catregory)
        self.query_button_1.grid(row=2, column=0, padx=10, pady=10)

        # Второй запрос
        self.category_label2 = tk.Label(self.master, text="Категория:")
        self.category_label2.grid(row=0, column=1, padx=10, pady=10)

        self.collection_var2 = tk.StringVar()
        self.collection_entry2 = ttk.Combobox(master,textvariable=self.collection_var2, values=self.listCategory)
        self.collection_entry2.grid(row=1, column=1)

        self.query_button_2 = tk.Button(self.master, text="2. Характеристики товаров по категории", command=self.get_product_characteristics_by_category)
        self.query_button_2.grid(row=2, column=1, padx=10, pady=10)

        # Третий запрос
        self.category_label2 = tk.Label(self.master, text="Покупатели:")
        self.category_label2.grid(row=0, column=2, padx=10, pady=10)

        self.collection_var3 = tk.StringVar()
        self.collection_entry3 = ttk.Combobox(master,textvariable=self.collection_var3, values=self.listCustomer)
        self.collection_entry3.grid(row=1, column=2)

        self.query_button_3 = tk.Button(self.master, text="3. Товары, купленные заданным покупателем", command=self.get_products_by_customer)
        self.query_button_3.grid(row=2, column=2, padx=10, pady=10)

        # Четвертый запрос
        self.category_label4 = tk.Label(self.master, text="Цвета:")
        self.category_label4.grid(row=0, column=3, padx=10, pady=10)

        self.collection_var4 = tk.StringVar()
        self.collection_entry4 = ttk.Combobox(master,textvariable=self.collection_var4, values=self.listColors)
        self.collection_entry4.grid(row=1, column=3)

        self.query_button_4 = tk.Button(self.master, text="4. Товары с заданным цветом", command=self.get_products_by_color)
        self.query_button_4.grid(row=2, column=3, padx=10, pady=10)

        # Пятый запрос
        self.category_label5 = tk.Label(self.master, text="Общая сумма:")
        self.category_label5.grid(row=3, column=0, padx=10, pady=10)

        self.query_button_5 = tk.Button(self.master, text="5. Общая сумма проданных товаров", command=self.get_total_sold_amount)
        self.query_button_5.grid(row=5, column=0, padx=10, pady=10)

        # Шестой запрос
        self.category_label6 = tk.Label(self.master, text="Товары в категориях:")
        self.category_label6.grid(row=3, column=1, padx=10, pady=10)

        self.query_button_6 = tk.Button(self.master, text="6. Количество товаров в каждой категории", command=self.get_products_count_by_category)
        self.query_button_6.grid(row=5, column=1, padx=10, pady=10)

        # Седьмой запрос
        self.category_label7 = tk.Label(self.master, text="Товары:")
        self.category_label7.grid(row=3, column=2, padx=10, pady=10)

        self.collection_var7 = tk.StringVar()
        self.collection_entry7 = ttk.Combobox(master,textvariable=self.collection_var7, values=self.listProducts)
        self.collection_entry7.grid(row=4, column=2)

        self.query_button_7 = tk.Button(self.master, text="7. Имена покупателей заданного товара", command=self.get_customer_names_by_product)
        self.query_button_7.grid(row=5, column=2, padx=10, pady=10)

        # Восьмой запрос
        self.category_label8 = tk.Label(self.master, text="Товары:")
        self.category_label8.grid(row=3, column=3, padx=10, pady=10)

        self.collection_var8 = tk.StringVar()
        self.collection_entry8 = ttk.Combobox(master,textvariable=self.collection_var8, values=self.listProducts)
        self.collection_entry8.grid(row=4, column=3)

        self.category_label8_1 = tk.Label(self.master, text="Службы доставки")
        self.category_label8_1.grid(row=5, column=3, padx=10, pady=10)

        self.collection_var8_1 = tk.StringVar()
        self.collection_entry8 = ttk.Combobox(master,textvariable=self.collection_var8_1, values=self.listDeliveries)
        self.collection_entry8.grid(row=6, column=3)

        self.query_button_8 = tk.Button(self.master, text="8. Имена покупателей с доставкой от заданной фирмы", command=self.get_customer_names_by_product_and_delivery)
        self.query_button_8.grid(row=7, column=3, padx=10, pady=10)

        # Блок с результатом
        self.result_label = tk.Label(self.master, text="Результат:")
        self.result_label.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

        self.result_text = tk.Text(self.master, height=10, width=50, state="disabled")
        self.result_text.grid(row=9, column=1, columnspan=2, padx=10, pady=10)


    #####################################################
    # 1 запрос
    def get_product_names_by_catregory(self):
        category = self.collection_var1.get()
        result_text = f"1. Названия товаров по категории '{category}':\n"

        pipeline = [
            {
                "$match": {"category": category}
            },
            {
            "$project": {
                "_id": 0,
                "product_name": 1
                }
            }
        ]

        a = self.collection.aggregate(
            pipeline
        )

        for name in a:
            result_text += name['product_name'] + '\n'

        self.update_result_text(result_text)


    # 2 запрос
    def get_product_characteristics_by_category(self):
        category = self.collection_var2.get()
        result_text = f"2. Характеристики товаров по категории '{category}':\n"

        pipeline = [
            {
                "$match": {"category": category}
            },
            {
            "$project": {
                "_id": 0,
                "product_name": 1,
                "characteristics": 1
                }
            }
        ]

        a = self.collection.aggregate(
            pipeline
        )
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        
        for doc in a:
            json_str = json.dumps(doc, indent=2, ensure_ascii=False) +  '\n_______________________________________\n\n'
            self.result_text.insert(tk.END, json_str)

        
        self.result_text.config(state="disabled")


     # 3 запрос
    def get_products_by_customer(self):
        customer = self.collection_var3.get()

        result_text = f"3. Товары, купленные покупателем '{customer}':\n"


        pipeline = [
            {
                "$match": {"customer_info.customer_name": customer}
            },
            {
                "$project": {
                    "_id": 0,
                    "product_name": "$product_name",
                    "price": "$price"
                }
            }
        ]

        a = self.collection.aggregate(
            pipeline
        )
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        
        for doc in a:
            json_str = json.dumps(doc, indent=2, ensure_ascii=False) +  '\n_______________________________________\n\n'
            self.result_text.insert(tk.END, json_str)

        
        self.result_text.config(state="disabled")


     # 4 запрос
    def get_products_by_color(self):
        color = self.collection_var4.get()
        result_text = f"4. Товары с цветом '{color}':\n"

        pipeline = [
            {
                "$match": {"characteristics.color": color}
            },
            {
                "$project": {
                    "_id": 0,
                    "product_name": "$product_name",
                    "manufacturer":"$manufacturer",
                    "price": "$price"
                }
            }
        ]

        a = self.collection.aggregate(
            pipeline
        )
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        
        for doc in a:
            json_str = json.dumps(doc, indent=2, ensure_ascii=False) +  '\n_______________________________________\n\n'
            self.result_text.insert(tk.END, json_str)

        
        self.result_text.config(state="disabled")

    def get_total_sold_amount(self):
        result_text = f"5. Общая сумма проданных товаров: "

        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "total_sales": {"$sum": "$price"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "total_sales": 1
                }
            }
        ]

        a = self.collection.aggregate(
            pipeline
        )
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        
        for doc in a:
            json_str = doc["total_sales"]
            self.result_text.insert(tk.END, json_str)
        
        
        self.result_text.config(state="disabled")


    def get_products_count_by_category(self):
        result_text = f"6. Количество товаров в каждой категории:\n"

        pipeline = [
        {
            "$group": {
                "_id": "$category",
                "total_products": {"$sum": 1}
            }
        },
        {
            "$project": {
                "_id": 0,
                "category": "$_id",
                "total_products": 1
            }
        }
    ]

        a = self.collection.aggregate(
            pipeline
        )
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        
        for doc in a:
            json_str = json.dumps(doc, indent=2, ensure_ascii=False) +  '\n_______________________________________\n\n'
            self.result_text.insert(tk.END, json_str)

        
        self.result_text.config(state="disabled")

    def get_customer_names_by_product(self):
        product_name = self.collection_var7.get()
        result_text = f"7. Имена покупателей товара '{product_name}':\n"

        pipeline = [
            {
                "$match": {"product_name": product_name}
            },
            {
                "$group": {
                    "_id": "$customer_info.customer_name"
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "customer_name": "$_id"
                }
            }
        ]

        a = self.collection.aggregate(
            pipeline
        )
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        
        for doc in a:
            json_str = json.dumps(doc, indent=2, ensure_ascii=False) +  '\n_______________________________________\n\n'
            self.result_text.insert(tk.END, json_str)

        self.result_text.config(state="disabled")


    def get_customer_names_by_product_and_delivery(self):
        product_name = self.collection_var8.get()
        delivery_service = self.collection_var8_1.get()

        result_text = f"8. Имена покупателей товара '{product_name}' с доставкой от '{delivery_service}':\n"


        pipeline = [
            {
                "$match": {"product_name": product_name, "customer_info.delivery_service": delivery_service}
            },
            {
                "$unwind": "$customer_info"
            },
            {
                "$match": {"customer_info.delivery_service": delivery_service}
            },
            {
                "$group": {
                    "_id": "$customer_info.customer_name"
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "customer_name": "$_id"
                }
            }
        ]
        a = self.collection.aggregate(
            pipeline
        )
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        
        for doc in a:
            json_str = doc["customer_name"]
            self.result_text.insert(tk.END, "-" +json_str+",\n")

        self.result_text.config(state="disabled")
    

    def update_result_text(self, text):
        self.result_text.config(state=tk.NORMAL)  # Включаем режим редактирования
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state="disabled")



root = tk.Tk()
app = ProductQueryApp(root, collection)
root.mainloop()

