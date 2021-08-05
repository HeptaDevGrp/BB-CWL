import MySQLdb


def read_into_mysql(data):
    # note the port you want to use for connection
    db = MySQLdb.connect(host='101.34.39.209',
                         user='write_autho',
                         passwd='write123456',
                         db='bb_data',
                         port=8080,
                         charset='utf8')
    cursor = db.cursor()

    try:  
        for i in range(len(data['Title'])):
            course_code = MySQLdb.escape_string(data['Posted To'][i])
            announcement = MySQLdb.escape_string(data['Title'][i])
            # the date needed to be transformed into YYYY-MM-DD HH:MM:SS (Null able)
            date = MySQLdb.escape_string(data['Posted On'][i])
            who = MySQLdb.escape_string(data['Posted By'][i])
            title = MySQLdb.escape_string(data['Title'][i])
            cursor.execute("insert into `assignment_outline`(`course_code`,`announcement`,`who`,`date`,`title`) values (%s,%s,%s,%s,%s)",
                           (course_code,announcement,who,date,title))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    cursor.close()
    db.close()

    return
