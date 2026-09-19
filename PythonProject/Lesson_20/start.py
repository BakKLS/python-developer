# Главный исполняемый файл приложения. Отвечает за бесконечный цикл консольного меню
# и первичную инициализацию соединения с SQLite базой данных.
import sys
from my_models import init_db, SessionLocal
import actions


def main():
    # Перед запуском цикла создаем схему данных
    init_db()
    db = SessionLocal()

    while True:
        print("\n--- МЕНЮ УПРАВЛЕНИЯ ---")
        print("1. Создать пользователя")
        print("2. Показать пользователей")
        print("3. Создать задачу")
        print("4. Показать все задачи")
        print("5. Изменить статус задачи")
        print("6. Удалить задачу")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Введите уникальное имя пользователя: ")
            user = actions.create_user(db, name)
            if user:
                print(f"Пользователь успешно добавлен. ID: {user.id}")
            else:
                print("Ошибка: Пользователь с таким именем уже существует в системе.")

        elif choice == "2":
            users = actions.get_users(db)
            if not users:
                print("Список пользователей пуст.")
            for u in users:
                print(f"ID: {u.id} | Имя: {u.username}")

        elif choice == "3":
            try:
                user_id = int(input("Введите ID пользователя для привязки задачи: "))
                title = input("Введите название задачи: ")
                actions.create_task(db, title, user_id)
                print("Задача успешно добавлена и привязана к пользователю.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "4":
            tasks = actions.get_tasks(db)
            if not tasks:
                print("Задач в базе данных не обнаружено.")
            for t in tasks:
                status = "Выполнена" if t.is_done else "В процессе"
                print(f"ID: {t.id} | [{status}] {t.title} | (Владелец ID: {t.user_id})")

        elif choice == "5":
            try:
                t_id = int(input("Введите ID задачи для редактирования: "))
                done = input("Установить статус выполнения? (1 - да, 0 - нет): ") == "1"
                if actions.update_task_status(db, t_id, done):
                    print("Статус задачи успешно обновлен.")
                else:
                    print("Задача с указанным ID не найдена.")
            except ValueError:
                print("Ошибка ввода. Идентификатор должен быть числовым.")

        elif choice == "6":
            try:
                t_id = int(input("Введите ID задачи для удаления: "))
                if actions.delete_task(db, t_id):
                    print("Задача успешно удалена из базы данных.")
                else:
                    print("Задача с указанным ID не найдена.")
            except ValueError:
                print("Ошибка ввода. Идентификатор должен быть числовым.")

        elif choice == "0":
            print("Завершение работы программы.")
            break

    # Перед завершением работы обязательно закрываем сессию соединения
    db.close()


if __name__ == "__main__":
    main()