def add_everything_up(a, b):
    try:
        # Сложить a и b
        return a + b
    except TypeError:
        # Если возникает ошибка, мы объединяем as строки
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))