# diskFileInfo2Mysql
scan whole disk file info (not directory), write file info to mysql table , then find file quikly （好了不装了就是给小姐姐做好记录，好找）

# need python3    and pip install mysql-connector-python

# need mysql  

```
create database collect;

-- menu is the only table 
CREATE TABLE `menu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(1000) DEFAULT NULL,
  `size` varchar(10) DEFAULT NULL,
  `time` varchar(30) DEFAULT NULL,
  `path` varchar(300) DEFAULT NULL,
  `tag` varchar(100) DEFAULT NULL,
  `fsize` bigint(20) DEFAULT NULL comment 'no use now..',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

> if you wana use this python scripts don't forget change to your mysql username and password


# collect.py   write your disk path（root path） and Loop over files in the root path (when meet directory recursive traversal )

```
-- use python3 run the scripts 
--  if your disk path is  windows (D:)  or  macos (/Volumes/D)
python3 collect.py 
请输入文件夹路径：D:

请输入文件夹路径 means write your file path 

then whole file info can be collet into mysql table menu

youcan look your table data like this:


mysql> select * from menu a where a.title like '%mp4' limit 10;
+-----+----------------------------+-------+---------------------+-----------------------+------+-------+
| id  | title                      | size  | time                | path                  | tag  | fsize |
+-----+----------------------------+-------+---------------------+-----------------------+------+-------+
|  93 | xxxxxxxxxx.mp4            | 2.54G | 2021-11-30 10:31:58 | /Volumes/Z/2021-11-30 |      |  NULL |
|  95 | xxxxxxxxxx.mp4             | 3.03G | 2021-11-23 21:58:45 | /Volumes/Z/2021-11-30 |      |  NULL |
|  97 | xxxxxxxxxx.mp4             | 9.05G | 2022-06-19 18:23:46 | /Volumes/Z/2022-06-20 |      |  NULL |
|  99 | xxxxxxxxxx.mp4             | 3.85G | 2022-06-18 05:38:26 | /Volumes/Z/2022-06-20 |      |  NULL |
| 101 | xxxxxxxxxx.mp4             | 5.44G | 2022-06-19 20:48:08 | /Volumes/Z/2022-06-20 |      |  NULL |
| 103 | xxxxxxxxxx.mp4             | 8.45G | 2022-06-19 20:10:46 | /Volumes/Z/2022-06-20 |      |  NULL |
| 105 | xxxxxxxxxx.mp4             | 5.99G | 2022-06-18 16:59:21 | /Volumes/Z/2022-06-20 |      |  NULL |
| 107 | xxxxxxxxxx.mp4              | 10.3G | 2022-06-18 10:15:55 | /Volumes/Z/2022-06-20 |      |  NULL |
| 109 | xxxxxxxxxx.mp4              | 6.21G | 2022-06-19 15:57:18 | /Volumes/Z/2022-06-20 |      |  NULL |
| 111 | xxxxxxxxxx.mp4               | 4.94G | 2022-06-19 16:50:58 | /Volumes/Z/2022-06-20 |      |  NULL |
+-----+----------------------------+-------+---------------------+-----------------------+------+-------+
10 rows in set (0.00 sec)


```

# saear.py  封装了查询mysql 的语句而已

```
python3 search.py 
请输入车牌号：

write your title can fuzzy searches （模糊搜索）
```

# mysql2mysql.py  (迁移数据用)
```
import another remote mysql table data into your mysql table 
```

# remove_duplicate_file.py  节省磁盘空间
```
if your find you download two same name video in your disk 
you can remove one of them to save disk space 


use a complex sql to get this

原理是，看看当前磁盘中的内容，是否已经被存储，已经被存储，自动删除！！ 注意会自动删除重复项，小姐姐没了别怪我没提醒，只匹配title
python3 remove_duplicate_file.py
输入盘符:
```