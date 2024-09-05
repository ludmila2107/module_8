def personal_sum(numbers):
	result = 0
	incorrect_data = 0

	for number in numbers:
		try:
			result += number
		except TypeError:
			incorrect_data += 1

	return result, incorrect_data


def calculate_average(numbers):
	try:
		# является ли numbers коллекцией (например, списком, кортежем)
		if not hasattr(numbers, '__iter__'):
			raise TypeError("В numbers записан некорректный тип данных")

		total_sum, incorrect_count = personal_sum(numbers)

		# Если коллекция не содержит чисел, необходимо обработать ZeroDivisionError
		count_of_numbers = len(numbers) - incorrect_count
		if count_of_numbers == 0:
			return 0

		average = total_sum / count_of_numbers
		return average
	except ZeroDivisionError:
		return 0
	except TypeError as e:
		print(e)
		return None

	print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
	print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
	print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
	print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
