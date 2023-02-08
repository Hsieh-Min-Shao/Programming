先下載  
MySQL Community Server (8.0.32) (壓縮板)  
https://dev.mysql.com/downloads/mysql/  
MySQL Workbench (8.0.32)  
https://dev.mysql.com/downloads/workbench/  
  
將下載好的 MySQL Community Server (8.0.32) (壓縮板) 解壓縮放至C槽  
創立一個檔案，名稱為my.ini  
輸入以下程式碼並儲存在my.ini  
```
[mysqld]
# 預設port為3306
port=3306
# mysql的安裝根目錄
basedir=C:\mysql-8.0.32-winx64
# mysql的資料根目錄
datadir=C:\mysql-8.0.32-winx64/data
# 預設時區
default-time-zone='+8:00'
# 連接數上限
max_connections=200
# 允許連接失敗的次數上限. 以防止資料庫被攻擊
max_connect_errors=10
# Server端預設字元編碼
character-set-server=utf8mb4
# 預設儲存引擎
default-storage-engine=INNODB
# 預設認證套件
default_authentication_plugin=mysql_native_password
# 接受大寫命名
lower_case_table_names=2
# 封包大小上限
max_allowed_packet=10M
[mysql]
# Client端預設字元編碼
default-character-set=utf8
[client]
# Client端連接Server端時, 預設使用的port
port=3306
default-character-set=utf8
```
  
接下來再以系統管理員的身分開啟CMD，並先切到檔案位置  
```
cd C:\mysql-8.0.32-winx64\bin
```
```
mysqld --initialize --console
```
  
臨時密碼 root@localhost: 7!G#JlfxRkN8 (每個人不一樣)  
--> 7!G#JlfxRkN8  
  
```
mysqld --install
```

修改密碼  
```
mysqladmin -u root -p password
```
  
登入SQL  
```
mysql -u root -p
```

輸入密碼成功就可以看到這個頁面
