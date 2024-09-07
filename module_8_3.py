class IncorrectVinNumber(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)


class IncorrectCarNumbers(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)


class Car:
	def __init__(self, model, vin_number, numbers):
		self.model = model
		self.__vin = vin_number
		self.__numbers = numbers
		self.__is_valid_vin(self.__vin)
		self.__is_valid_numbers(self.__numbers)

	def __is_valid_vin(self, vin_number):
		if not isinstance(vin_number, int):
			raise IncorrectVinNumber('Некорректный тип vin номер')
		if vin_number < 1000000 or vin_number > 9999999:
			raise IncorrectVinNumber('Неверный диапазон для vin номера')
		return True

	def __is_valid_numbers(self, numbers):
		if not isinstance(numbers, str):
			raise IncorrectCarNumbers('Некорректный тип данных для номеров')
		if len(numbers) != 6:
			raise IncorrectCarNumbers('Неверная длина номера, должна состоять ровно из 6 символов')
		return True

try:
	car1 = Car("Toyota Camry", 1234567, "ABC123")
	print("Автомобиль создан:", car1.model)
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
	print("Ошибка:", e.message)

try:
	car2 = Car("Honda Accord", 12345678, "AB123")  # Неверный vin номер и номер автомобиля
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
	print("Ошибка:", e.message)

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

