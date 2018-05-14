from demos.W8.day1.UserManage.utils.db_util import MysqlUtil

# 用户模型
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# User类的数据库访问对象
# 封装了对User数据的增删改查
# Dao=Database Access Object 数据库访问对象
class UserDao:

    # 定义常量：表名、字段...
    TABLENAME = "t_usr"
    COL_USERNAME = "username"
    COL_PASSWORD = "password"

    # 创建User表
    @classmethod
    def createTable(cls):
        # 不存在用户表则创建用户表
        sql='''
        create table if not EXISTS t_usr(
          id INTEGER PRIMARY KEY auto_increment,
          username varchar(20) unique not null,
          password varchar(20) not null
        );
        '''

        # 调用数据库工具的原生sql接口
        MysqlUtil.execute(sql)
        pass

    '''
    增删改查全部调用数据库工具的增删改查方法（API）
    '''

    # 插入一条User数据
    @classmethod
    def insert(cls, user):
        dataDict = {}
        dataDict[cls.COL_USERNAME] = user.username
        dataDict[cls.COL_PASSWORD] = user.password
        MysqlUtil.insert(cls.TABLENAME,dataDict)
        pass

    # 删除一条User数据
    @classmethod
    def delete(cls, user):
        pass

    # 修改一条User数据
    # user=要修改的对象，targetDict=新的属性值字典
    @classmethod
    def update(cls, user, targetDict):
        pass

    # 查询User数据是否存在
    @classmethod
    def query(cls, user):
        dataDict = {
            cls.COL_USERNAME:user.username,
            cls.COL_PASSWORD:user.password
        }
        ret = MysqlUtil.query(cls.TABLENAME,dataDict)
        if ret:
            return User(ret[0][1],ret[0][2])