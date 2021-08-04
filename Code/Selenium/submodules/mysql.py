import MySQLdb


def read_into_mysql(data):
    # note the port you want to use for connection
    db = MySQLdb.connect("localhost", "user_name", "password", "database_name", charset='utf8')
    cursor = db.cursor()

    # Lyon: YOUR CODE STARTS HERE
    # You need to dump products/formatted_data.json into the MySQL database
    for line in data.splitlines():
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchone()
        print("Database version : %s " % data)

    db.close()
    return
