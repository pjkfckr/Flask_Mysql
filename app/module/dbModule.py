import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='',
                                  db='test_db',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursor.Dictcursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.executeAll(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()



        