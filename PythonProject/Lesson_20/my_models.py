# Долго думал над структурой, решил объединить конфигурацию движка и декларативную базу здесь,
# чтобы не плодить лишние файлы настроек сессии и не путаться в циклических импортах.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# Базу сохраняем локально, здесь же инициализируем сессию для последующей работы в actions
engine = create_engine("sqlite:///tasks_v2.db")
SessionLocal = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    # По условию задачи добавляем ограничение UNIQUE на имя пользователя
    username = Column(String, unique=True, nullable=False)

    # Каскадное удаление необходимо, чтобы при удалении юзера не оставалось сиротских задач
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))

    user = relationship("User", back_populates="tasks")


def init_db():
    # Метод создает таблицы в файле базы данных, если их там еще нет
    Base.metadata.create_all(bind=engine)