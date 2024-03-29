def int_check(*args):
    while True:
        num = input()
        if is_int(num):
            if len(args) == 2 and not (args[0] <= int(num) <= args[1]):
                print('\nError, enter the number in correct interval!\n')
            else:
                return int(num)
        else:
            print('\nError, enter the number!\n')

def float_check(*args):
    while True:
        num = input()
        if is_float(num):
            if len(args) == 2 and not (args[0] <= float(num) <= args[1]):
                print('\nError, enter the number in correct interval!\n')
            else:
                return float(num)
        else:
            print('\nError, enter the number!\n')

def is_float(value):
    try:
        value = float(value)
        return True
    except ValueError:
        return False
    
def is_int(value):
    try:
        value = int(value)
        return True
    except ValueError:
        return False