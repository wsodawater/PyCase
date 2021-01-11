import pytest


@pytest.fixture(params=[1,2,3])
def login(request):
    print(request.param)
    print("获取数据")

def test_case111(login):
    print('\n'"执行测试用例111")
