import repeater
import input_checker
import lr3_task1
import lr3_task2
import lr3_task3
import lr3_task4
import lr3_task5


repeat = True
while(repeat):
    print('Select a task to run.\nEnter a number from 1 to 5 to select\n')
    task_num = input_checker.int_check(1,5)
    match task_num:
        case 1:
            print(lr3_task1.task.__doc__)
            lr3_task1.task()
        case 2:
            print(lr3_task2.task.__doc__)
            lr3_task2.task()
        case 3:
            print(lr3_task3.task.__doc__)
            lr3_task3.task()
        case 4:
            print(lr3_task4.task.__doc__)
            lr3_task4.task()
        case 5:
            print(lr3_task5.task.__doc__)
            lr3_task5.task()
    repeat = repeater.repeater('LR 3: ')


