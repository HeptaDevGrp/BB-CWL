#%%
import MySQLdb
import json
def read_into_mysql(data):
    # note the port you want to use for connection
    db = MySQLdb.connect(host = '101.34.39.209',
                     user = 'write_autho',
                     passwd = 'write123456', 
                     db = 'bb_data', 
                     port = 8080, 
                     charset='utf8')
    cursor = db.cursor()
    # Lyon: YOUR CODE STARTS HERE
    # You need to dump products/formatted_data.json into the MySQL database
    
    # for line in data.splitlines():
    #     # 使用execute方法执行SQL语句
    #     cursor.execute("SELECT VERSION()")
    #     # 使用 fetchone() 方法获取一条数据
    #     data = cursor.fetchone()
    #     print("Database version : %s " % data)
    try:  
        for i in range(len(data['Title'])):
            course_code = MySQLdb.escape_string(data['Posted To'][i])
            announcement = MySQLdb.escape_string(data['Title'][i])
            # the date needed to be transformed into YYYY-MM-DD HH:MM:SS (Null able)
            # date = MySQLdb.escape_string(data['Posted On'][i]) 
            who = MySQLdb.escape_string(data['Posted By'][i])
            title = MySQLdb.escape_string(data['Title'][i])
            cursor.execute("insert into `assignment_outline`(`course_code`,`announcement`,`who`,`title`) values (%s,%s,%s,%s)",
                           (course_code,announcement,who,title))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()    
    db.close()
    return
#%%
# import MySQLdb
# import json
# fp = open('D:/hepta\BB-CWL/Code/Selenium/products/formatted_data.json','r',encoding = 'utf8')
# json_data = json.load(fp)
# #%%
# db = MySQLdb.connect(host = '101.34.39.209',
#                       user = 'write_autho',
#                       passwd = 'write123456', 
#                       db = 'bb_data', 
#                       port = 8080, 
#                       charset='utf8')
# cursor = db.cursor()
# #%%
# try:  
#     for i in range(len(json_data['Title'])):
#         course_code = MySQLdb.escape_string(json_data['Posted To'][i])
#         announcement = MySQLdb.escape_string(json_data['Stipulate'][i])
#         title = MySQLdb.escape_string(json_data['Title'][i])
#         # the date needed to be transformed into YYYY-MM-DD HH:MM:SS (Null able)
#         date = MySQLdb.escape_string(json_data['Posted On'][i]) 
#         who = MySQLdb.escape_string(json_data['Posted By'][i])
#         cursor.execute("insert into `assignment_outline`(`course_code`,`announcement`,`who`,`date`,`title`) values (%s,%s,%s,%s,%s)",
#                         (course_code,announcement,who,date,title))
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
# #%%
# cursor.close()
# db.close()
