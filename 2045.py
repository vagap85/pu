import json
from collections import defaultdict

# Открываем и загружаем JSON-файл
with open(r'C:\Users\dublk\Downloads\july2023.json', "r") as my_file:
    data = json.load(my_file)

# Инициализация переменных
max_price = 0
max_price_order = ''
max_items = 0
max_items_order = ''
orders_per_day = defaultdict(int)
orders_per_user = defaultdict(int)
total_spent_per_user = defaultdict(float)
total_orders_price = 0
total_items_price = 0
total_orders = 0
total_items = 0

# Обработка данных
for order_num, order_data in data.items():
    # Проверяем наличие ключа 'price'
    if 'price' not in order_data:
        print(f"В заказе {order_num} отсутствует ключ 'price'. Пропускаем этот заказ.")
        continue

    # Стоимость заказа
    price = order_data['price']

    # Количество товаров в заказе (если ключ 'items' отсутствует, считаем количество товаров равным 0)
    items_count = len(order_data.get('items', []))  # Используем метод .get() для безопасного доступа

    # Дата заказа (если ключ 'date' отсутствует, используем значение по умолчанию)
    order_date = order_data.get('date', 'Неизвестная дата')

    # Пользователь (если ключ 'user' отсутствует, используем значение по умолчанию)
    user = order_data.get('user', 'Неизвестный пользователь')

    # Поиск самого дорогого заказа
    if price > max_price:
        max_price = price
        max_price_order = order_num

    # Поиск заказа с самым большим количеством товаров
    if items_count > max_items:
        max_items = items_count
        max_items_order = order_num

    # Подсчет количества заказов по дням
    orders_per_day[order_date] += 1

    # Подсчет количества заказов по пользователям
    orders_per_user[user] += 1

    # Подсчет суммарной стоимости заказов по пользователям
    total_spent_per_user[user] += price

    # Общая стоимость всех заказов
    total_orders_price += price

    # Общая стоимость всех товаров (если ключ 'items' присутствует)
    if 'items' in order_data:
        for item in order_data['items']:
            if 'price' in item:  # Проверяем наличие ключа 'price' у товара
                total_items_price += item['price']
                total_items += 1

    # Общее количество заказов
    total_orders += 1

# Находим день с наибольшим количеством заказов
max_orders_day = max(orders_per_day, key=orders_per_day.get)

# Находим пользователя с наибольшим количеством заказов
max_orders_user = max(orders_per_user, key=orders_per_user.get)

# Находим пользователя с наибольшей суммарной стоимостью заказов
max_spent_user = max(total_spent_per_user, key=total_spent_per_user.get)

# Средняя стоимость заказа
average_order_price = total_orders_price / total_orders if total_orders > 0 else 0

# Средняя стоимость товара
average_item_price = total_items_price / total_items if total_items > 0 else 0

# Вывод результатов
print(f'1. Номер самого дорогого заказа: {max_price_order}, стоимость: {max_price}')
print(f'2. Номер заказа с самым большим количеством товаров: {max_items_order}, количество товаров: {max_items}')
print(f'3. День с наибольшим количеством заказов: {max_orders_day}, количество заказов: {orders_per_day[max_orders_day]}')
print(f'4. Пользователь с наибольшим количеством заказов: {max_orders_user}, количество заказов: {orders_per_user[max_orders_user]}')
print(f'5. Пользователь с наибольшей суммарной стоимостью заказов: {max_spent_user}, суммарная стоимость: {total_spent_per_user[max_spent_user]}')
print(f'6. Средняя стоимость заказа в июле: {average_order_price:.2f}')
print(f'7. Средняя стоимость товара в июле: {average_item_price:.2f}')