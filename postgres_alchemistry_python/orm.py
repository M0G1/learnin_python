from sqlalchemy import create_engine
from sqlalchemy import Table, Column, DateTime
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

# DATABASE = {
#     'drivername': 'postgressql',  # Тут можно использовать MySQL или другой драйвер
#     'host': 'localhost',
#     'port': '5432',
#     'username': 'postgres',
#     'password': 'M0g1_elf=MagHardworker2021',
#     'database': 'training_db'
# }

# engine = create_engine(URL(**DATABASE))

# # по умолчанию вариант
# # engine  = create_engine('postgres://youuser:youpassword@localhost:5432/youdb')
# engine  = create_engine('postgres://postgres:M0g1_elf=MagHardworker2021@localhost:5433/training_db')
#
# # При использовании psycopg2
# # engine = create_engine('postgresql+psycopg2://youuser:youpassword@localhost/youdb')
# engine = create_engine('postgresql+psycopg2://M0g1_elf=MagHardworker2021@localhost:5433/training_db')

# metadata = MetaData()
# domains = Table(
#     'domains'
# )

DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)

    def __repr__(self):
        return f"id {self.id} name {self.name} url {self.url}"


def main():
    # Создаем объект Engine, который будет использоваться объектами ниже для связи с БД
    engine = create_engine('postgresql+psycopg2://postgres:M0g1_elf=MagHardworker2021@localhost:5432/postgres')
    # engine = create_engine(URL(**DATABASE))

    # simplepassword

    # Метод create_all создает таблицы в БД , определенные с помощью  DeclarativeBase
    DeclarativeBase.metadata.create_all(engine)

    # Создаем фабрику для создания экземпляров Session. Для создания фабрики в аргументе
    # bind передаем объект engine
    Session = sessionmaker(bind=engine)

    # Создаем объект сессии из вышесозданной фабрики Session
    session = Session()

    # Создаем новую запись.
    new_post = Post(name='Two record', url="http://testsite.ru/first_record")

    # Добавляем запись
    session.add(new_post)

    # Благодаря этой строчке мы добавляем данные а таблицу
    session.commit()

    # А теперь попробуем вывести все посты , которые есть в нашей таблице
    for post in session.query(Post):
        print(post)

    query = session.query(Post).where(Post.id >= 2)
    data = session.execute(query)

    print(list(data))


if __name__ == "__main__":
    main()
