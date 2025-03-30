
import pytest 

def fix_phone_num(phone_num_to_fix):
    # Remove non-digit characters
    phone_num = ''.join(filter(str.isdigit, phone_num_to_fix))
    # Check if the number has exactly 10 digits
    if len(phone_num) != 10:
        raise ValueError("Phone number must contain exactly 10 digits.")
    # Split the parts and format the number
    area_code = phone_num[0:3]
    three_part = phone_num[3:6]
    four_part = phone_num[6:]
    fixed_num = f"({area_code}) {three_part} {four_part}"
    return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
