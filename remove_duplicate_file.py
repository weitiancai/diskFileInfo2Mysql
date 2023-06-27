import os
import pymysql

# for root, dirs, files in os.walk(operate_path):
#     print('root:',root)
#     print('dirs:',dirs)
#     print('files:',files)
#     print('\n')

def remove_duplicate_file(disk):
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='collect')
    cursor = db.cursor()
    sql = '''select concat(min_path,"/",title) from(
    select min(id) id,title,size, min(path) min_path,group_concat(case when length(path)>15 then substr(path,1,15) else path end order by id) as join_path 
    from menu a 
    group by title,size 
    having count(path) > 1
    )a where a.join_path like "{0}:%"
    '''.format(disk)
    
    del_sql = '''delete from menu where title in (
    select title from(
        select title,size, min(path) min_path,group_concat(case when length(path)>15 then substr(path,1,15) else path end order by id) as join_path 
        from menu a 
        group by title,size 
        having count(path) > 1
    )a where a.join_path like  "{0}:%") and path like  "{1}:%"'''.format(disk,disk)
    try:
        cursor.execute(sql)
        file_list = cursor.fetchall()
        db.commit()
        # print(file_list)
        cnt = 1
        for file in file_list:
            path =str(file)[2:-3]
            print(path)
            path = path.replace('\\\\','/')
            # cnt= cnt+1
            # if(cnt> 10):
            #     break
            if os.path.exists(path):
                os.remove(path)
                print('删除'+path+'文件成功')
        if len(file_list)>0:
            cursor.execute(del_sql)
            cnt = cursor.fetchall()
            db.commit()
            # print("清除數據庫記錄" + str(cnt) +"条")
            print("删除记录成功")
            print(cnt)
    except Exception as e:
        print(e)
        db.rollback()
        print("刪除数据失败")
    finally:
        db.close()
while(1):
    disk_label = input("输入盘符：")
    remove_duplicate_file(disk_label)
