while True:
    char = input("Введите символ C: ").strip()
    if char:
        char = char[0]
        break
    print("Символ не должен быть пустым!")

A = []
print("Введите строки (enter для завершения):")
while True:
    s = input().strip()
    if not s:
        break
    A.append(s)

count = 0
for s in A:
    if len(s) > 1 and s.startswith(char) and s.endswith(char):
        count += 1

print(f"Количество элементов, начинающихся и заканчивающихся на '{char}': {count}")