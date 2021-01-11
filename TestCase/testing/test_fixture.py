import pytest

# def setup():
#     print("测试开始")
#
# def teardown():
#     print("测试结束")

#创建一个登陆的fixture方法
@pytest.fixture()
def login():
    print('\n'"登陆")
#获取数据
    print("获取token")
    username = "tim"
    token = "token123"
#添加登出操作
    yield [username,token]
    print("退出")

#需要提前登陆
def test_case1(login):
    print('\n'f"获取数据:{login}")
    print("执行测试用例111")

#需要提前登陆
# @TestCase.mark.usefixtures("login")
def test_case2(login):
    print('\n'f"获取数据:{login}")
    print("执行测试用例222")

def test_case3(connectDB):
    print('\n'"执行测试用例333")

def test_case4():
    print('\n'"执行测试用例444")