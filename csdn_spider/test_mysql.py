import pymysql.cursors


connection = pymysql.connect(host="localhost", user="root", password="123456", db="spider", charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('liushixiongcpp@163.com', 'password'))

    connection.commit()

    with connection.cursor() as cursor:
        sql = "select `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('liushixiongcpp@163.com', ))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

