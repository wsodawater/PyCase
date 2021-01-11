import pytest
import yaml

from Calculator.Calculator import Calculator

with open("./datas.yaml") as f:
    datas = yaml.safe_load(f)
    print(datas)
    calc_add_datas = datas["add"]
    calc_sub_datas = datas["sub"]
    calc_div_datas = datas["div"]
    calc_mul_datas = datas["mul"]


@pytest.fixture(params=calc_add_datas)
def get_add(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(params=calc_sub_datas)
def get_sub(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(params=calc_div_datas)
def get_div(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(params=calc_mul_datas)
def get_mul(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(scope='module')
def get_calc():
    print("获取计算机实例")
    calc = Calculator()
    return calc