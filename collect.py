import pymysql
import os
import mysql.connector
def insert(value):
    db = pymysql.connect(host='192.168.100.11', user='root', password='123456', port=3306, db='collect')
    cursor = db.cursor()
    sql = "INSERT INTO menu(title,size,time,path,tag) values(%s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql, value)
        db.commit()
        print('插入数据成功')
    except Exception as e:
        print(e)
        db.rollback()
        print("插入数据失败")
    db.close()

def insert_batch(file_list):
    cnx = mysql.connector.connect(user='root', password='Wm123456', host='localhost', database='collect')
    cursor = cnx.cursor()

    # 批量插入的 SQL 语句
    sql = "INSERT INTO menu (title, time, size, path, tag) VALUES (%s, %s, %s, %s, %s)"

    # 执行批量插入
    cursor.executemany(sql, file_list)

    # 提交事务并关闭连接
    cnx.commit()
    cursor.close()
    cnx.close()

def get_file_size(filePath):
    unit=''
    fsize = os.path.getsize(filePath)
    if fsize > 1024 * 1024 * 1024:
        fsize = fsize/float(1024 * 1024 * 1024)
        unit = 'G'
    elif fsize > 1024 * 1024:
        fsize = fsize/float(1024 * 1024)
        unit = 'M'
    elif fsize > 1024:
        fsize = fsize/float(1024)
        unit = 'K'
    return str(round(fsize, 2))+unit
import time 
def get_file_time(file):
    #return time.ctime(os.path.getmtime(file)).format('yyyy-MM-dd HH:mm:ss')
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file)))
def insert_file_info(my_path):
    #my_path = 'D://menu.txt'
    #print('title = '+os.path.basename(os.path.realpath(my_path)))
    #print('size = '+get_file_size(my_path))
    #print('path = '+os.path.dirname(os.path.realpath(my_path)))
    #print('time = '+get_file_time(my_path))
    #print('tag = '+'#'.join(os.path.basename(os.path.realpath(my_path)).split('#')[1:]))

    title = os.path.basename(os.path.realpath(my_path))
    size = get_file_size(my_path)
    path = os.path.dirname(os.path.realpath(my_path))
    time = get_file_time(my_path)
    tag = '#'.join(os.path.basename(os.path.realpath(my_path)).split('#')[1:])
    return (title, time, size ,path ,tag)
    
def scan_file(root):
    for root, dirs, files in os.walk(root):
        for file in files:
            print(os.path.join(root, file)) #当前路径下所有非目录子文件
def get_all_path(open_file_path):
    rootdir = open_file_path
    path_list = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    file_list = []
    for i in range(0, len(list)):
        com_path = os.path.join(rootdir, list[i])
        #print(com_path)
        if os.path.isfile(com_path):
            #path_list.append(com_path)
            print(com_path)
            file_info = insert_file_info(com_path)
            file_list.append(file_info)
        if os.path.isdir(com_path):
            #path_list.extend(get_all_path(com_path))
            print(com_path + "乃是一个文件夹")
            get_all_path(com_path)
    insert_batch(file_list)
while(1):
    file_path = input("请输入文件夹路径：")
    get_all_path(file_path)

