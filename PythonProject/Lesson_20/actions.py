# Вынес всю работу с сессиями и CRUD-операции в этот слой бизнес-логики.
# Передаем объект сессии (db) параметром в каждую функцию, как это принято в архитектуре ORM.
from sqlalchemy.orm import Session
from my_models import User, Task

def create_user(db: Session, name: str):
    """Создание нового пользователя с отловом ошибок уникальности (UNIQUE)"""
    try:
        user = User(username=name)
        db.add(user)
        db.commit()
        return user
    except Exception:
        # Если имя неуникально, откатываем транзакцию, чтобы не вешать сессию
        db.rollback()
        return None

def get_users(db: Session):
    """Получение полного списка зарегистрированных пользователей"""
    return db.query(User).all()

def create_task(db: Session, title: str, user_id: int):
    """Привязка новой задачи к конкретному ID пользователя"""
    task = Task(title=title, user_id=user_id)
    db.add(task)
    db.commit()
    return task

def get_tasks(db: Session):
    """Получение всех существующих задач для общего вывода"""
    return db.query(Task).all()

def update_task_status(db: Session, task_id: int, done: bool):
    """Изменение статуса выполнения задачи по ее уникальному идентификатору"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.is_done = done
        db.commit()
    return task

def delete_task(db: Session, task_id: int):
    """Удаление задачи из системы"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False