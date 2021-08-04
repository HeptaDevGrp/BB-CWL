import MySQLdb


def read_into_mysql(data):
    db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8')
    cursor = db.cursor()

    for line in data.splitlines():
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchone()
        print("Database version : %s " % data)

    db.close()

    return
