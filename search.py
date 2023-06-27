import pymysql
def search(value):
    db = pymysql.connect(host='localhost', user='root', password='Wm123456', port=3306, db='collect')
    cursor = db.cursor()
    sql = "select substring(a.title,locate('"+value+"',lower(title)),50),path,size from menu a where lower(a.title) like '%"+value+"%' order by title"
    print(sql)
    try:
        cursor.execute(sql)
        while True:
            row = cursor.fetchone()
            if not row:
                break
            for column in row:
                print(' {: <50}  '.format(column),end="")
            print();
    except Exception as e:
        print(e)
        db.rollback()
        print("查询数据失败")
    db.close()

while(1):
    car_num = input("请输入车牌号：")
    search(car_num.lower())
