import pymysql
"""
##### 数据库连接类
##### 并没有对数据库进行封装
"""


class creat_mysql:
    def __init__(self):
        super().__init__()
        self.host = "localhost"
        self.user = "root"
        self.password = "123456"
        self.port = 3306
        self.database = "novel"
        self.con = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )
        self.cursor = self.con.cursor()

    def start(self, sql_language):
        self.cursor.execute(sql_language)
        result = self.cursor.fetchall()
        print(result)

    def close(self):
        self.cursor.close()
        self.con.close()


if __name__ == '__main__':
    sql = creat_mysql()
    sql.start("select * from novel;")
    sql.close()
