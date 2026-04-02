import functions   

def test_custom_power():
    assert functions.custom_power.__name__ == "<lambda>"
    assert functions.custom_power(2) == 2
    assert functions.custom_power(2, 3) == 8
    assert functions.custom_power(49, e=0.5) == 7

def test_custom_equation():
    assert functions.custom_equation(1, 2) == 3
    assert functions.custom_equation(1, 2, 3) == 3
    assert functions.custom_equation(1, 2, 3, 4) == 17
    assert round(functions.custom_equation(1, 2, 3, 4, c=5), 1) == 3.4
    assert functions.custom_equation(1, 2, 3, c=5, b=6) == 13

def test_fn_w_counter():
    for i in range(1, 6):
        val = functions.fn_w_counter()
        assert val == (i, {"functions": i})
