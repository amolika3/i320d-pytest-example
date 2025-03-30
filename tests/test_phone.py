import pytest
from my_code import fix_phone_num

def test_fix_phone_num():
    assert fix_phone_num("5125558823") == "(512) 555 8823"
    assert fix_phone_num("5554429876") == "(555) 442 9876"
    assert fix_phone_num("3216543333") == "(321) 654 3333"

def test_fix_phone_num_invalid_formats():
    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761")
    assert fix_phone_num("(321) 654 3333") == "(321) 654 3333"

def test_fix_phone_num_value_error():
    with pytest.raises(ValueError):
        fix_phone_num("not a number")
    with pytest.raises(ValueError):
        fix_phone_num("123ABC7890")

