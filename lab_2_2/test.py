import pymongo
import tkinter as tk
from tkinter import ttk




class MainMenu:
        # Подключение
    client = pymongo.MongoClient('localhost')
    # Выбор базы данных (если ее нет, она будет создана)
    db = client['22305']

    # Выбор коллекции (если ее нет, она будет создана)
    collection = db['Gashkov-listProducts']


    listCategory = list(collection.distinct("Название категории"))
    listBuyer = list(collection.distinct("Товары.Покупатели.Имя"))
    listColor = list(collection.distinct("Товары.Особые характеристики.Цвет"))
    listProduct = list(collection.distinct("Товары.Название товара"))
    listDelivery = list(collection.distinct("Товары.Покупатели.Служба доставки"))

    def SummaProduct(self):
        return (list(self.collection.aggregate([
            {"$unwind": "$Товары"},
            {"$unwind": "$Товары.Покупатели"},
            {"$group": {
                "_id": None,
                "total_sold": {"$sum": "$Товары.Цена"}
            }},
            {"$project": {"_id": 0, "total_sold": 1}}
        ]))[0]['total_sold'])


    def __init__(self, root):
        self.root = root
        self.root.title("Главное меню")

        # Создание верхнего ряда блоков
        self.create_block("Товары в категории", "укажите категорию", self.listCategory, self.show_stub1)
        self.create_block("Характеристики товаров", "укажите категорию", self.listCategory, self.show_stub2)
        self.create_block("Покупки покупателя", "укажите покупателя", self.listBuyer, self.show_stub3)
        self.create_block("Товары заданного цвета", "укажите цвет", self.listColor, self.show_stub4)

        # Создание нижнего ряда блоков
        self.create_block_with_result("Общая сумма", self.show_result, str(self.SummaProduct()))
        self.create_block("Товары в категориях", None, None, self.show_stub6, "no_arguments")
        self.create_block("Покупатели товара", "укажите товар", self.listProduct, self.show_stub7)
        self.create_block_with_two_dropdowns("Доставка", self.listProduct, self.listDelivery, self.show_stub8)

    def create_block(self, title, label_text, dropdown_options, command, *args):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=len(self.root.grid_slaves()) // 4, column=len(self.root.grid_slaves()) % 4, sticky="nsew")
        self.root.grid_columnconfigure(len(self.root.grid_slaves()) % 4, weight=1)

        ttk.Label(frame, text=title).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        if label_text:
            ttk.Label(frame, text=label_text).grid(row=1, column=0)
            category_var = tk.StringVar()
            category_dropdown = ttk.Combobox(frame, textvariable=category_var, values=dropdown_options)
            category_dropdown.grid(row=1, column=1, pady=(0, 10))

        if args:
            ttk.Button(frame, text="Просмотр", command=command).grid(row=2, column=0, columnspan=2)
        else:
            ttk.Button(frame, text="Просмотр", command=lambda: command(category_var.get())).grid(row=2, column=0,
                                                                                                 columnspan=2)

    def create_block_with_result(self, title, command, result):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=len(self.root.grid_slaves()) // 4, column=len(self.root.grid_slaves()) % 4, sticky="nsew")
        self.root.grid_columnconfigure(len(self.root.grid_slaves()) % 4, weight=1)

        ttk.Label(frame, text=title).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        result_label = ttk.Label(frame, text="")
        result_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        def show_result():
            result_label.config(text=result)

        ttk.Button(frame, text="Просмотр", command=show_result).grid(row=2, column=0, columnspan=2)

    def create_block_with_two_dropdowns(self, title, dropdown1_options, dropdown2_options, command):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=len(self.root.grid_slaves()) // 4, column=len(self.root.grid_slaves()) % 4, sticky="nsew")
        self.root.grid_columnconfigure(len(self.root.grid_slaves()) % 4, weight=1)

        ttk.Label(frame, text=title).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Label(frame, text="Товар").grid(row=1, column=0)
        product_var = tk.StringVar()
        product_dropdown = ttk.Combobox(frame, textvariable=product_var, values=dropdown1_options)
        product_dropdown.grid(row=1, column=1, pady=(0, 10))

        ttk.Label(frame, text="Доставка").grid(row=2, column=0)
        delivery_var = tk.StringVar()
        delivery_dropdown = ttk.Combobox(frame, textvariable=delivery_var, values=dropdown2_options)
        delivery_dropdown.grid(row=2, column=1, pady=(0, 10))

        ttk.Button(frame, text="Просмотр", command=lambda: command(product_var.get(), delivery_var.get())).grid(row=3, column=0, columnspan=2)

    def show_category_products_window(self, category):
        products_window = tk.Toplevel(self.root)
        products_window.title(f"Товары в категории: {category}")

        # Retrieve products for the given category from the database

        products = []
        category_name = str(category)
        a = self.collection.aggregate(
            [
                {"$match": {"Название категории": category_name}},
                {"$unwind": "$Товары"},
                {"$project": {"название_товара": "$Товары.Название товара"}}
            ]
        )
        for i in a:
            products.append(i['название_товара'])

        # Create a treeview for displaying the products
        tree = ttk.Treeview(products_window, columns=("Название товара",), show="headings")
        tree.heading("Название товара", text="Название товара")

        # Insert data into the treeview
        for product in products:
            tree.insert("", "end", values=(product,))

        tree.pack(expand=True, fill="both")

    def show_stub1(self, selected_value):
        print(f"Функция заглушка 1 вызвана с параметром: {selected_value}")
        if selected_value:
            self.show_category_products_window(selected_value)

    def show_characteristics_window(self, category):
        characteristics_window = tk.Toplevel(self.root)
        characteristics_window.title(f"Характеристики товаров в категории: {category}")

        # Retrieve product characteristics for the given category from the database
        characteristics = []
        category_name = str(category)
        a = self.collection.aggregate([
            {"$match": {"Название категории": category_name}},
            {"$unwind": "$Товары"},
            {"$unwind": "$Товары.Особые характеристики"},
            {"$group": {
                "_id": "$Товары.Название товара",
                "характеристики": {"$addToSet": "$Товары.Особые характеристики"}
            }},
            {"$project": {
                "товар": "$_id",
                "характеристики": 1,
                "_id": 0
            }}
        ])
        for i in a:
            product_name = i.get("товар", "")
            product_characteristics = i.get("характеристики", {})
            characteristics.append({"название_товара": product_name, "характеристики": product_characteristics})

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(characteristics_window, orient="vertical")

        # Create a canvas to hold the blocks and connect it to the scrollbar
        canvas = tk.Canvas(characteristics_window, yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)

        # Configure the scrollbar to scroll the canvas
        scrollbar.config(command=canvas.yview)

        # Create a frame to hold the blocks
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Function to update the scroll region
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame.bind("<Configure>", on_frame_configure)

        # Insert data into the frame
        for product_data in characteristics:
            product_name = product_data.get("название_товара", "")
            product_characteristics = product_data.get("характеристики", {})

            # Create a block for each product
            product_block = ttk.Frame(frame, padding="10", relief="solid", borderwidth=1)
            product_block.pack(side="top", fill="x", pady=5)

            # Add the product name as the title
            ttk.Label(product_block, text=f"{product_name}").pack(side="top", anchor="w")

            # Add characteristics as key-value pairs
            for characteristic in product_characteristics:
                for key, value in characteristic.items():
                    ttk.Label(product_block, text=f"{key}: {value}").pack(side="top", anchor="w")

        # Bind mousewheel scrolling to the canvas
        characteristics_window.bind_all("<MouseWheel>",
                                        lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    def show_stub2(self, selected_value):
        print(f"Функция заглушка 2 вызвана с параметром: {selected_value}")
        if selected_value:
            self.show_characteristics_window(selected_value)

    def show_buyer_purchases_window(self, buyer_name):
        buyer_purchases_window = tk.Toplevel(self.root)
        buyer_purchases_window.title(f"Покупки покупателя: {buyer_name}")

        # Query data for buyer's purchases
        purchases = []
        a = self.collection.aggregate([
            {"$match": {"Товары.Покупатели.Имя": buyer_name}},
            {"$unwind": "$Товары"},
            {"$unwind": "$Товары.Покупатели"},
            {"$match": {"Товары.Покупатели.Имя": buyer_name}},
            {"$project": {
                "название_товара": "$Товары.Название товара",
                "цена": "$Товары.Цена"
            }}
        ])
        for i in a:
            product_name = i.get("название_товара", "")
            price = i.get("цена", "")
            purchases.append({"название_товара": product_name, "цена": price})

        # Create a treeview for displaying the purchases
        tree = ttk.Treeview(buyer_purchases_window, columns=("Название товара", "Цена"), show="headings")
        tree.heading("Название товара", text="Название товара")
        tree.heading("Цена", text="Цена")

        # Insert data into the treeview
        for purchase in purchases:
            product_name = purchase.get("название_товара", "")
            price = purchase.get("цена", "")
            tree.insert("", "end", values=(product_name, price))

        tree.pack(expand=True, fill="both")

    def show_stub3(self, selected_value):
        print(f"Функция заглушка 3 вызвана с параметром: {selected_value}")
        if selected_value:
            self.show_buyer_purchases_window(selected_value)

    def show_products_by_color_window(self, color_to_find):
        products_by_color_window = tk.Toplevel(self.root)
        products_by_color_window.title(f"Товары {color_to_find} цвета")

        # Query data for products with the specified color
        products = []
        a = self.collection.aggregate([
            {"$unwind": "$Товары"},
            {"$match": {"Товары.Особые характеристики.Цвет": color_to_find}},
            {"$project": {
                "Название товара": "$Товары.Название товара",
                "Производитель": "$Товары.Производитель",
                "Цена": "$Товары.Цена",
                "_id": 0
            }}
        ])
        for i in a:
            product_name = i.get("Название товара", "")
            manufacturer = i.get("Производитель", "")
            price = i.get("Цена", "")
            products.append({"Название товара": product_name, "Производитель": manufacturer, "Цена": price})

        # Create a treeview for displaying the products
        tree = ttk.Treeview(products_by_color_window, columns=("Название товара", "Производитель", "Цена"),
                            show="headings")
        tree.heading("Название товара", text="Название товара")
        tree.heading("Производитель", text="Производитель")
        tree.heading("Цена", text="Цена")

        # Insert data into the treeview
        for product in products:
            product_name = product.get("Название товара", "")
            manufacturer = product.get("Производитель", "")
            price = product.get("Цена", "")
            tree.insert("", "end", values=(product_name, manufacturer, price))

        tree.pack(expand=True, fill="both")

    def show_stub4(self, selected_value):
        print(f"Функция заглушка 4 вызвана с параметром: {selected_value}")
        if selected_value:
            self.show_products_by_color_window(selected_value)

    def show_products_by_category_window(self):
        products_by_category_window = tk.Toplevel(self.root)
        products_by_category_window.title("Товары в категориях")

        # Query data for the total number of products in each category
        categories_data = []
        a = self.collection.aggregate([
            {"$unwind": "$Товары"},
            {"$group": {
                "_id": "$Название категории",
                "total_products": {"$sum": 1}
            }},
            {"$project": {"_id": 0, "category": "$_id", "total_products": 1}}
        ])
        for i in a:
            category_name = i.get("category", "")
            total_products = i.get("total_products", "")
            categories_data.append({"Название категории": category_name, "Количество товара": total_products})

        # Create a treeview for displaying the categories and total products
        tree = ttk.Treeview(products_by_category_window, columns=("Название категории", "Количество товара"),
                            show="headings")
        tree.heading("Название категории", text="Название категории")
        tree.heading("Количество товара", text="Количество товара")

        # Insert data into the treeview
        for category_data in categories_data:
            category_name = category_data.get("Название категории", "")
            total_products = category_data.get("Количество товара", "")
            tree.insert("", "end", values=(category_name, total_products))

        tree.pack(expand=True, fill="both")

    def show_stub6(self):
        print(f"Функция заглушка 6 вызвана")
        self.show_products_by_category_window()

    def show_buyers_of_product_window(self, product_name):
        buyers_of_product_window = tk.Toplevel(self.root)
        buyers_of_product_window.title(f"Покупатели {product_name}")

        # Query data for the buyers of the specified product
        buyers_data = []
        a = self.collection.aggregate([
            {"$unwind": "$Товары"},
            {"$match": {"Товары.Название товара": product_name}},
            {"$unwind": "$Товары.Покупатели"},
            {"$project": {"_id": 0, "buyer_name": "$Товары.Покупатели.Имя"}}
        ])
        for i in a:
            buyer_name = i.get("buyer_name", "")
            buyers_data.append({"Покупатель": buyer_name})

        # Create a treeview for displaying the buyers
        tree = ttk.Treeview(buyers_of_product_window, columns=("Покупатель",), show="headings")
        tree.heading("Покупатель", text="Покупатель")

        # Insert data into the treeview
        for buyer_data in buyers_data:
            buyer_name = buyer_data.get("Покупатель", "")
            tree.insert("", "end", values=(buyer_name,))

        tree.pack(expand=True, fill="both")

    def show_stub7(self, selected_value):
        print(f"Функция заглушка 7 вызвана с параметром: {selected_value}")
        if selected_value:
            self.show_buyers_of_product_window(selected_value)

    def show_buyers_of_product_with_delivery_window(self, product_name, delivery_service):
        buyers_of_product_with_delivery_window = tk.Toplevel(self.root)
        buyers_of_product_with_delivery_window.title(f"{product_name} с доставкой {delivery_service}")

        # Query data for buyers of the specified product with the specified delivery service
        buyers_data = []
        a = self.collection.aggregate([
            {"$unwind": "$Товары"},
            {"$match": {"Товары.Название товара": product_name}},
            {"$unwind": "$Товары.Покупатели"},
            {"$match": {"Товары.Покупатели.Служба доставки": delivery_service}},
            {"$project": {"_id": 0, "buyer_name": "$Товары.Покупатели.Имя"}}
        ])
        for i in a:
            buyer_name = i.get("buyer_name", "")
            buyers_data.append({"Покупатель": buyer_name})

        # Create a treeview for displaying the buyers
        tree = ttk.Treeview(buyers_of_product_with_delivery_window, columns=("Покупатель",), show="headings")
        tree.heading("Покупатель", text="Покупатель")

        # Insert data into the treeview
        for buyer_data in buyers_data:
            buyer_name = buyer_data.get("Покупатель", "")
            tree.insert("", "end", values=(buyer_name,))

        tree.pack(expand=True, fill="both")

    def show_stub8(self, product_value, delivery_value):
        print(f"Функция заглушка 8 вызвана с параметрами: {product_value}, {delivery_value}")
        if product_value and delivery_value:
            self.show_buyers_of_product_with_delivery_window(product_value, delivery_value)

    def show_result(self):
        print("Просмотр результатов.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()