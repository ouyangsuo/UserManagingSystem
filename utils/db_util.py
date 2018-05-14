import pymysql
import redis

'''
MySQL操作工具
'''
class MysqlUtil:
    '''
    ·通过表名和条件字典（列名-值）进行数据的增删改查
    ·根据表名和条件字典拼装SQL语句并执行
    ·随用随连，用完就断开
    '''

    # 删除记录
    # tablename=表名
    # dataDict=要插入的数据
    @classmethod
    def insert(cls, tablename, dataDict):
        cls.connect()
        # CRUD...

        colnames =''
        values=''
        for k,v in dataDict.items():
            colnames += (k+",")
            values += ("'"+v+"',")

        # 去掉最后一个逗号
        colnames =colnames[:-1]
        values =values[:-1]

        # insert into t_usr(username,password) values('xxx','xxx');
        sql = 'insert into %s(%s) values(%s);' % (tablename, colnames, values)
        print(sql)
        cls.cursor.execute(sql)
        cls.conn.commit()

        cls.disconnect()

    # 删除记录
    # tablename=要删除的表
    # selectionDict=删除条件
    @classmethod
    def delete(cls, tablename, selectionDict):
        cls.connect()
        # CRUD...
        cls.disconnect()

    # 修改表数据
    # selectionDict = 要修改的数据条件
    # dataDict = 要修改为的数据
    @classmethod
    def update(cls, tablename, selectionDict,dataDict):
        cls.connect()
        # CRUD...
        cls.disconnect()

    # 删除记录
    # tablename=表名
    # selectionDict=查询条件
    @classmethod
    def query(cls, tablename, selectionDict):
        cls.connect()

        # CRUD...
        # 构造where子句
        whereClause = ''
        for k,v in selectionDict.items():
            whereClause += (k+"='"+v+"' and ")
        whereClause = whereClause[:-5]
        # select * from t_usr where username='xxx' and password='xxxx';
        sql = "select * from %s where %s;"%(tablename,whereClause)
        print(sql)
        affected = cls.cursor.execute(sql)
        if affected == 0:
            return None

        ret = cls.cursor.fetchall()
        print(affected,ret)

        cls.disconnect()
        return ret

    # 执行传入的原生SQL语句
    @classmethod
    def execute(cls, sql):
        cls.connect()
        cls.cursor.execute(sql)
        cls.disconnect()
        pass

    # 连接数据库，并生成全局可用的连接对象和查询游标
    @classmethod
    def connect(cls):
        cls.conn = pymysql.connect(
            host='localhost', port=3306, user='root', password="123456", database='homework'
        )
        cls.cursor = cls.conn.cursor()

    # 关闭全局游标，断开全局连接
    @classmethod
    def disconnect(cls):
        cls.cursor.close()
        cls.conn.close()

'''
Redis操作工具
'''
class RedisUtil:

    # 判断键是否存在
    @classmethod
    def exists(cls, key):
        return cls.client.exists(key)

    # 获取键对应的值
    @classmethod
    def get(cls, key):
        return cls.client.get(key).decode("utf-8")

    # 存储键值
    @classmethod
    def set(cls, key, value):
        cls.client.setex(key, value, 30)

    # 全局连接方法
    connected = False
    @classmethod
    def connect(cls):

        # 创建全局的Redis客户端
        if not cls.connected:
            cls.client = redis.Redis(
                host='localhost', port=6379, db=15, password='123456'
            )
            cls.connected = True
