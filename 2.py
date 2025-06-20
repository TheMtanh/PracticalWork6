class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

users = [
    User("MrGru", "qwerty123"),
    User("Labubo", "pass987"),
    User("JohnDoe", "hello2008"),
    User("8old8", "opensesame1"),
    User("MicroSort", "p@ssw0rd")
]

target_login = "8old8"
target_password = "opensesame1"

found_user = None
for user in users:
    if user.Login == target_login and user.Password == target_password:
        found_user = user
        break

if found_user:
    print(f"Логин: {found_user.Login}\nПароль: {found_user.Password}")
else:
    print("Пользователь не найден")