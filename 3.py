class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = date_start
        self.DateFinish = date_finish
        self.Description = description

tasks = [
    Task("2024-01-10 09:00", "2024-01-10 11:05", "Пара по математике"),
    Task("2024-01-10 12:00", "2024-01-10 12:30", "Лекция по программированию"),
    Task("2024-01-10 12:35", "2024-01-10 13:45", "Консультация по лингвистике"),
    Task("2024-01-10 13:50", "2024-01-10 15:00", "УиФИС"),
    Task("2024-02-15 10:00", "2024-02-15 14:10", "Учебная практика")
]

latest_task = tasks[0]
for task in tasks:
    if task.DateFinish > latest_task.DateFinish:
        latest_task = task

print(f"\nПозднее занятие: {latest_task.Description}\n")
print(f"Начало: {latest_task.DateStart}\nОкончание: {latest_task.DateFinish}")