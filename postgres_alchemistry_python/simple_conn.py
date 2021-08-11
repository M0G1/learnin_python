from sqlalchemy import create_engine
from sqlalchemy import Table, Column, DateTime
from sqlalchemy import MetaData
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
#     'database': 'postgres'
# }

metadata = MetaData()
posts = Table(
    "posts", metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('url', String),
)

# engine = create_engine(URL(**DATABASE))

engine = create_engine('postgresql+psycopg2://postgres:M0g1_elf=MagHardworker2021@localhost:5432/postgres')

with engine.connect() as conn:
    query = posts.select()
    # query2 = query.where(posts.c.id >= 2)
    data = conn.execute(query).fetchall()
    print(data)

    in_query = posts.insert().values(
        {"name": "aaa project", "url": "vk.com"},
        {"name": "aaa project", "url": "vk.com"},
    )

    in_query_data = conn.execute(in_query).fetchall()
    data = conn.execute(query).fetchall()

    print("\n", data)
