'''
业务逻辑调度器
'''


from demos.W8.day1.UserManage.model.models import User, UserDao
from demos.W8.day1.UserManage.utils.db_util import RedisUtil

# 登录方法
def login(user):

    '''查看Redis缓存中是否有用户数据'''

    # 如果缓存中没有用户名，就访问MySQL数据库
    if not RedisUtil.exists(user.username):
        print("get user from mysql...")

        # 通过UserDao向MySQL查询用户是否存在，返回用户信息
        theUser = UserDao.query(user)

        # MySQL用户存在,登录成功并缓存到Redis
        if theUser:

            print("mysql:login ok")
            # 如果查到数据，缓存到redis
            RedisUtil.set(theUser.username,theUser.password)

        # MySQL中不存在该用户，登录失败
        else:
            print("mysql:wrong username or password")

    # 缓存中有用户名，且密码匹配，登录成功
    elif RedisUtil.get(user.username) == user.password:
        print("redis:login ok")

    # 密码不匹配，登录失败
    else:
        print(RedisUtil.get(user.username))
        print("redis:wrong username or password")

# 数据初始化方法
def init():

    # 建表和插入数据
    # UserDao.createTable()
    # user1 = User("bill", "123456")
    # user2 = User("jobs", "123456")
    # user3 = User("jackma", "123456")
    # UserDao.insert(user1)
    # UserDao.insert(user2)
    # UserDao.insert(user3)

    # 连接redis数据库
    RedisUtil.connect()

# 访问主页
def index():
    # 初始化数据，建立Redis数据库连接
    init()

    # 接收用户输入
    username, password = input("please enter username and password:").split(",")
    user = User(username, password)

    # 调用登录逻辑
    login(user)
    print('GAME OVER')

if __name__ == '__main__':

    index()
    pass