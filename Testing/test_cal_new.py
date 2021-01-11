
import pytest



class Testcal:

    @pytest.mark.run(order=1)
    def test_add (self,get_add,get_calc):
        result = None
        try:
            result = get_calc.add(get_add[0], get_add[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add[2]

    @pytest.mark.run(order=4)
    def test_div (self,get_div,get_calc):
        result = get_calc.div(get_div[0], get_div[1])
        assert result == get_div[2]

    @pytest.mark.run(order=2)
    def test_sub (self,get_sub,get_calc):
        result = get_calc.sub(get_sub[0], get_sub[1])
        assert result == get_sub[2]

    @pytest.mark.run(order=3)
    def test_mul (self,get_mul,get_calc):
        result = get_calc.mul(get_mul[0], get_mul[1])
        assert result == get_mul[2]







