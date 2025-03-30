
import pytest 
def fix_phone_num(phone_num_to_fix):
    # Remove non-digit characters
    phone_num = ''.join(filter(str.isdigit, phone_num_to_fix))
    # Check if the number has exactly 10 digits
    if len(phone_num) != 10:
        raise ValueError("Phone number must contain exactly 10 digits.")
    # Format the phone number in the desired format
    return f"({phone_num[:3]}) {phone_num[3:6]} {phone_num[6:]}"

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
