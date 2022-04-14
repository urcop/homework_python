import os

print(os.getcwd())


def find_command(command: str):
    with open('/home/sirius/.bash_history', 'r') as file:
        f = file.readlines()
        result = [i for i in f if command in i]
        file.close()
        return result


com = input('Какую команду хотите найти? \n')
commands = find_command(com)
for command in commands:
    print('Хотите ли выполнить команду - {0} y/n/q'.format(command[0:-1]))
    arg = input()
    if arg == 'n':
        print('[INFO] Пропуск')
        continue
    elif arg == 'q':
        print('[INFO] Завершение')
        break
    else:
        print('[INFO] Выполняю команду')
        try:
            os.system(command=command[0:-1])
        except Exception as e:
            print(e)
        print('[INFO] Завершение')
        break
