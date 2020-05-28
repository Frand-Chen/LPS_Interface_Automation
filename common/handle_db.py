# -*- coding=utf-8 -*-

"""
该模块用来处理数据库
"""
import pymysql

from common.handle_config import sec_conf


class HandleDB:

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(host=sec_conf.get("mysql", "host"),
                                       port=sec_conf.getint("mysql", "port"),  # port 要是 int 类型
                                       user=sec_conf.get("mysql", "user"),
                                       password=sec_conf.get("mysql", "password"),
                                       charset="utf8"
                                       )
        # 创建一个游标对象
        self.cursor = self.connect.cursor()

    def get_one(self, sql):
        """获取查询到的第一条数据"""
        # 先提交事务，为了保证与当前数据库数据一致
        self.connect.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_all(self, sql):
        """获取查询到的所有数据"""
        self.connect.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def count(self, sql):
        """获取查询到的数据个数"""
        self.connect.commit()
        return self.cursor.execute(sql)

    def close(self):
        # 关闭游标对象
        self.cursor.close()
        # 关闭数据库连接
        self.connect.close()


if __name__ == '__main__':
    # sql = "SELECT leave_amount FROM futureloan.member WHERE id={}".format(1)
    sql = "SELECT leave_amount FROM futureloan.member"
    db = HandleDB()
    result = db.get_all(sql)
    # result = db.get_one(sql)
    print(result)
