import csv

# with open("data.csv", 'w') as file:  # открываем файл на запись
#     writer = csv.writer(file)  # создаём объект писателя и метод writer, в параметры которого передаём наш файл
#     # метод writerow записывает строку и принимает один аргумент
#     writer.writerow(
#         #names
#         ("user_name", "user_adress")  # заголовки
#     )

# users_data = [
#     ("user_name", "user_adress"),
#     ["user1", "address1"],
#     ["user2", "address2"],
#     ["user3", "address3"],
# ]

# for user in users_data:
#     with open("data.csv", "a") as file:
#         writer = csv.writer(file)
#         writer.writerow(user)

# можно и без перебора метод writerow построчно запишет данные
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(users_data)

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "Цена",
            "Кол-во монет",
            "Итог"
        )
    )
