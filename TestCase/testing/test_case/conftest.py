import pytest


@pytest.fixture(scope='session')
def connectDB():
    print('\n'"连接数据库")
    yield
    print("断开数据库")
