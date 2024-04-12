import repeater
import input_checker
import task1 
import task2 
import task3 
import task4 
import task5 

tasks = [task1.Task1, task2.Task2, task3.Task3, task4.Task4, task5.Task5]


def main():
    repeat = True
    while(repeat):
        print('Select a task to run.\nEnter a number from 1 to 5 to select\n')
        task_num = input_checker.int_check("",1,5)
        tasks[task_num-1](task_num).start_task()
        
        # match task_num:
        #     case 1:
        #         tasks[3](4).start_task()
        #     case 2:
        #         print(lr4_task2.task.__doc__)
        #         lr4_task2.task()
        #     case 3:
        #         print(lr4_task3.task.__doc__)
        #         lr4_task3.task()
        #     case 4:
        #         print(lr4_task4.task.__doc__)
        #         lr4_task4.task()
        #     case 5:
        #         print(lr4_task5.task.__doc__3)
        #         lr4_task5.task()
        repeat = repeater.repeater("LR 4: ")

if __name__ == '__main__':
    main()