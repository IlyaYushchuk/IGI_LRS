import input_checker

def custom_generator(first, last, step):

    num = first
    while num != last:
        yield num
        num += step

def user_input_seq():
    print('Enter the starting value of the sequence:',end=' ')
    first = input_checker.float_check()
    print('Enter the ending value of the sequence:',end=' ')
    last = input_checker.float_check()
    print('Enter sequence step:',end=' ')
    step = input_checker.float_check()
    return custom_generator(first, last, step)

def gen_input_seq():
    list = []
    print('Enter the number of sequence elements:\n')
    count = input_checker.int_check(1, float('inf'))
    for i in range(count):
        print(i,':',end=' ')
        list.append(input_checker.float_check())
    return list