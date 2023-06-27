import mysql.connector

# 创建连接和游标
cnx = mysql.connector.connect(user='root', password='123456', host='192.168.100.11', database='collect')
cursor = cnx.cursor()

# 获取数据
cursor.execute("SELECT title, size, time, path, tag, fsize FROM menu2")
data = cursor.fetchall()

# 关闭连接
cursor.close()
cnx.close()


# 创建连接和游标
cnx = mysql.connector.connect(user='root', password='Wm123456', host='localhost', database='collect')
cursor = cnx.cursor()

# 写入数据
for row in data:
    sql = "INSERT INTO menu ( title, size, time, path, tag, fsize) VALUES ( %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, row)

# 提交事务并关闭连接
cnx.commit()
cursor.close()
cnx.close()
