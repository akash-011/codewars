"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.


"""

#My Solution


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False 

 #Best Solution 

 def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()