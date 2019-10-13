from peewee import *
from datetime import date


db = MySQLDatabase("spider", host="127.0.0.1", port=3306, user="root", password="123456")


class Person(Model):
    name = CharField(max_length=20)
    birthday = DateTimeField()

    class Meta:
        database = db


# 数据的增、删、改、查
if __name__ == "__main__":
    db.create_tables([Person])

    # 生成数据
    uncle_bob = Person(name="linux", birthday=date(1992, 1, 15))
    uncle_bob.save()

    # uncle_bob = Person(name="unix", birthday=date(1990, 12, 15))
    # uncle_bob.save()

    # 查询数据 这种方法在取不到数据会抛出异常
    # bobby = Person.select().where(Person.name == "linux1").get()
    # print(bobby.birthday)
    # Person.get(Person.name == "linux1")

    # 获取多个数据
    query_list = Person.select().where(Person.name == "linux")
    for person in query_list:
        # 更新数据
        # person.birthday = date(2019, 9, 10)
        # person.save()
        # 删除数据
        person.delete_instance()
