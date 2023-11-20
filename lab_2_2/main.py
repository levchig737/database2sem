import pymongo
import tkinter as tk
from tkinter import ttk

# Подключение
client = pymongo.MongoClient('localhost')
database = client['22307']

# Создание коллекции
shop_collection = database["chekarev-shop_data"]


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
                "customer_name": "Анна Иванова",
                "purchase_date": "2023-01-10",
                "review": "Отличный выбор для работы и развлечений",
                "delivery_service": "TechExpress"
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
                "delivery_service": "ProExpress"
            },
            {
                "customer_name": "Марина Семенова",
                "purchase_date": "2023-04-02",
                "review": "Большой объем памяти, удобный в использовании",
                "delivery_service": "ExpressProTech"
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
                "customer_name": "Ольга Петрова",
                "purchase_date": "2023-03-20",
                "review": "Идеальный для профессионального использования",
                "delivery_service": "EliteExpress"
            },
            {
                "customer_name": "Дмитрий Игнатьев",
                "purchase_date": "2023-04-18",
                "review": "Быстрый и надежный, высокая производительность",
                "delivery_service": "ExpressEliteTech"
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
                "customer_name": "Наталья Соколова",
                "purchase_date": "2023-01-25",
                "review": "Легкий и компактный, отлично подходит для путешествий",
                "delivery_service": "UltraExpress"
            },
            {
                "customer_name": "Артем Миронов",
                "purchase_date": "2023-02-10",
                "review": "Удобный и стильный, хорошая цена",
                "delivery_service": "ExpressUltraTech"
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
                "delivery_service": "PowerExpress"
            },
            {
                "customer_name": "Екатерина Кузнецова",
                "purchase_date": "2023-04-15",
                "review": "Высокая производительность, стильный дизайн",
                "delivery_service": "ExpressPowerTech"
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
                "delivery_service": "AppleExpress"
            },
            {
                "customer_name": "Анна Ковалева",
                "purchase_date": "2023-04-20",
                "review": "Прекрасная камера, стильный дизайн",
                "delivery_service": "iPhoneDelivery"
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
                "delivery_service": "PixelExpress"
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
                "delivery_service": "OneExpress"
            },
            {
                "customer_name": "Артем Миронов",
                "purchase_date": "2023-04-02",
                "review": "Операционная система OxygenOS на высшем уровне",
                "delivery_service": "OneDelivery"
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
                "customer_name": "Ирина Кудрявцева",
                "purchase_date": "2023-04-05",
                "review": "Большой и красочный экран, отличная камера",
                "delivery_service": "MiExpress"
            },
            {
                "customer_name": "Владимир Попов",
                "purchase_date": "2023-04-18",
                "review": "Доступная цена, высокая производительность",
                "delivery_service": "XiaomiDelivery"
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
                "delivery_service": "SonyExpress"
            },
            {
                "customer_name": "Анастасия Семенова",
                "purchase_date": "2023-04-15",
                "review": "Удобный и стильный, отличное качество сборки",
                "delivery_service": "XperiaDelivery"
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
                "delivery_service": "RedmiExpress"
            },
            {
                "customer_name": "Василий Иванов",
                "purchase_date": "2023-03-12",
                "review": "Долгая автономия, быстрая доставка",
                "delivery_service": "XiaomiNoteDelivery"
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
                "delivery_service": "AudioExpress"
            },
            {
                "customer_name": "Сергей Игнатов",
                "purchase_date": "2023-02-08",
                "review": "Хороший выбор за свою цену",
                "delivery_service": "SoundDelivery"
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
                "delivery_service": "BassExpress"
            },
            {
                "customer_name": "Ольга Козлова",
                "purchase_date": "2023-04-02",
                "review": "Отличное шумоподавление, удобные в ношении",
                "delivery_service": "ExpressBassTech"
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
                "delivery_service": "SonicExpress"
            },
            {
                "customer_name": "Андрей Семенов",
                "purchase_date": "2023-04-18",
                "review": "Комфортные наушники, отличное качество звука",
                "delivery_service": "ExpressSonicTech"
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
                "delivery_service": "UltraExpress"
            },
            {
                "customer_name": "Марина Миронова",
                "purchase_date": "2023-02-10",
                "review": "Легкие и удобные, отличное соотношение цена-качество",
                "delivery_service": "ExpressUltraTech"
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
                "delivery_service": "HarmonyExpress"
            },
            {
                "customer_name": "Денис Семенов",
                "purchase_date": "2023-04-15",
                "review": "Хорошее сочетание цвета и качества звука",
                "delivery_service": "ExpressHarmonyTech"
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
                "delivery_service": "UltraExpress"
            },
            {
                "customer_name": "Людмила Козлова",
                "purchase_date": "2023-04-02",
                "review": "Умные функции работают на ура",
                "delivery_service": "SmartVisionDelivery"
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
                "delivery_service": "ProExpress"
            },
            {
                "customer_name": "Дмитрий Игнатьев",
                "purchase_date": "2023-04-18",
                "review": "Идеальный выбор для киноманов",
                "delivery_service": "ExpressProTech"
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
                "delivery_service": "VisionaryExpress"
            },
            {
                "customer_name": "Алиса Новикова",
                "purchase_date": "2023-02-10",
                "review": "Умные функции удобны в использовании",
                "delivery_service": "ExpressVisionaryTech"
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
                "delivery_service": "SmartViewExpress"
            },
            {
                "customer_name": "Иван Семенов",
                "purchase_date": "2023-04-15",
                "review": "Прост в использовании, красочное изображение",
                "delivery_service": "ExpressSmartViewTech"
            }
        ]
    }
    ]

    shop_collection.delete_many({})

    for document in shop_data:
        shop_collection.insert_one(document)
    print(len(shop_data))
    

# save_document()
import tkinter as tk
from tkinter import ttk
import pymongo

class ProductQueryApp:
    def __init__(self, master, collection):
        self.master = master
        self.master.title("Product Query App")

        self.collection = collection

        self.create_widgets()

    def create_widgets(self):
        self.category_label = tk.Label(self.master, text="Категория:")
        self.category_label.grid(row=0, column=0, padx=10, pady=10)

        self.category_entry = tk.Entry(self.master)
        self.category_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        self.query_button_1 = tk.Button(self.master, text="1. Названия товаров по категории", command=self.query_1)
        self.query_button_1.grid(row=1, column=0, padx=10, pady=10)

        self.query_button_2 = tk.Button(self.master, text="2. Характеристики товаров по категории", command=self.query_2)
        self.query_button_2.grid(row=1, column=1, padx=10, pady=10)

        self.query_button_3 = tk.Button(self.master, text="3. Товары, купленные заданным покупателем", command=self.query_3)
        self.query_button_3.grid(row=1, column=2, padx=10, pady=10)

        self.query_button_4 = tk.Button(self.master, text="4. Товары с заданным цветом", command=self.query_4)
        self.query_button_4.grid(row=1, column=3, padx=10, pady=10)

        self.query_button_5 = tk.Button(self.master, text="5. Общая сумма проданных товаров", command=self.query_5)
        self.query_button_5.grid(row=2, column=0, padx=10, pady=10)

        self.query_button_6 = tk.Button(self.master, text="6. Количество товаров в каждой категории", command=self.query_6)
        self.query_button_6.grid(row=2, column=1, padx=10, pady=10)

        self.query_button_7 = tk.Button(self.master, text="7. Имена покупателей заданного товара", command=self.query_7)
        self.query_button_7.grid(row=2, column=2, padx=10, pady=10)

        self.query_button_8 = tk.Button(self.master, text="8. Имена покупателей с доставкой от заданной фирмы", command=self.query_8)
        self.query_button_8.grid(row=2, column=3, padx=10, pady=10)

        self.result_label = tk.Label(self.master, text="Результат:")
        self.result_label.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

    def query_1(self):
        category = self.category_entry.get()
        result_text = f"1. Названия товаров по категории '{category}':\n"
        result_text += f"{self.get_product_names_by_category(category)}\n"
        self.update_result_text(result_text)

    def query_2(self):
        category = self.category_entry.get()
        result_text = f"2. Характеристики товаров по категории '{category}':\n"
        result_text += f"{self.get_product_characteristics_by_category(category)}\n"
        self.update_result_text(result_text)

    def query_3(self):
        customer_name = self.category_entry.get()
        result_text = f"3. Товары, купленные покупателем '{customer_name}':\n"
        result_text += f"{self.get_products_by_customer(customer_name)}\n"
        self.update_result_text(result_text)

    def query_4(self):
        color = self.category_entry.get()
        result_text = f"4. Товары с цветом '{color}':\n"
        result_text += f"{self.get_products_by_color(color)}\n"
        self.update_result_text(result_text)

    def query_5(self):
        result_text = f"5. Общая сумма проданных товаров:\n"
        result_text += f"{self.get_total_sold_amount()}\n"
        self.update_result_text(result_text)

    def query_6(self):
        result_text = f"6. Количество товаров в каждой категории:\n"
        result_text += f"{self.get_products_count_by_category()}\n"
        self.update_result_text(result_text)

    def query_7(self):
        product_name = self.category_entry.get()
        result_text = f"7. Имена покупателей товара '{product_name}':\n"
        result_text += f"{self.get_customer_names_by_product(product_name)}\n"
        self.update_result_text(result_text)

    def query_8(self):
        product_name = self.category_entry.get()
        delivery_service = "YourDeliveryService"  # Замените на фактическую службу доставки
        result_text = f"8. Имена покупателей товара '{product_name}' с доставкой от '{delivery_service}':\n"
        result_text += f"{self.get_customer_names_by_product_and_delivery(product_name, delivery_service)}\n"
        self.update_result_text(result_text)

    def get_product_names_by_category(self, category):
        # Ваши запросы
        return ["Product1", "Product2", "Product3"]

    def get_product_characteristics_by_category(self, category):
        # Ваши запросы
        return [{"characteristic1": "value1"}, {"characteristic2": "value2"}, {"characteristic3": "value3"}]

    def get_products_by_customer(self, customer_name):
        # Ваши запросы
        return ["Product1", "Product2", "Product3"]

    def get_products_by_color(self, color):
        # Ваши запросы
        return ["Product1", "Product2", "Product3"]

    def get_total_sold_amount(self):
        # Ваши запросы
        return "$1000.00"

    def get_products_count_by_category(self):
        # Ваши запросы
        return {"Category1": 10, "Category2": 15, "Category3": 8}

    def get_customer_names_by_product(self, product_name):
        # Ваши запросы
        return ["Customer1", "Customer2", "Customer3"]

    def get_customer_names_by_product_and_delivery(self, product_name, delivery_service):
        # Ваши запросы
        return ["Customer1", "Customer2", "Customer3"]

    def update_result_text(self, text):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)

# Пример использования
client = pymongo.MongoClient('192.168.112.103')
database = client['your_database_name']
collection_name = database["your_collection_name"]

root = tk.Tk()
app = ProductQueryApp(root, collection_name)
root.mainloop()

