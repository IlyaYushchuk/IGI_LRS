def repeater(str):
    while(True):
        print(str,'Repeat program execution? (yes/no)\n')
        str = input()
        if str.lower() == 'yes':
            return True
        elif str.lower() == 'no':
            return False
        else:
            print('Sorry, please enter yes/no\n')