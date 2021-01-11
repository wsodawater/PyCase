
import pytest
import yaml

from Calculator.Calculator import Calculator



class Testcal:


    def setup_class(self):
        self.cal = Calculator()
        print("开始测试")

    def teardown_class(self):
        self.cal = Calculator()
        print("测试结束")

    def setup (self):
        print("开始计算")

    def teardown (self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,exp",yaml.safe_load(open("./data.yaml"))["add"])
    def test_add (self,a,b,exp):
        result = self.cal.add(a,b)
        assert result == exp

    @pytest.mark.parametrize("a,b,exp",yaml.safe_load(open("./data.yaml"))["sub"])
    def test_sub (self,a,b,exp):
        result = self.cal.sub(a,b)
        assert result == exp
    #
    @pytest.mark.parametrize("a,b,exp",yaml.safe_load(open("./data.yaml"))["mul"])
    def test_mul (self,a,b,exp):
        result = self.cal.mul(a,b)
        assert result == exp

    @pytest.mark.parametrize("a,b,exp",yaml.safe_load(open("./data.yaml"))["div"])
    def test_div (self,a,b,exp):
        result = self.cal.div(a,b)
        assert result == exp





