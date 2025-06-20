numbers = [-5, 3, -2, 8, -1, 4, -7, 6]

first_positive = next((num for num in numbers if num > 0), None)
last_negative = next((num for num in reversed(numbers) if num < 0), None)

print(f"Первый положительный: {first_positive}")
print(f"Последний отрицательный: {last_negative}")