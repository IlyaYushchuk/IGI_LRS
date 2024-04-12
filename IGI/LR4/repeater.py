import input_checker

def repeater(str):
    while(True):
        print(str,'Repeat program execution? (yes/no)\n')
        str = input()
        if str.lower() in ('yes','y','да','д',1):
            return True
        elif str.lower() in ('no','n','нет','н',0):
            return False
        else:
            print('Sorry, please enter yes/no\n')