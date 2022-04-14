import os


def replace_text(file: str, to_replace: str, for_replace: str) -> str:
    if os.path.exists(file) and file.split('.')[-1] == 'txt' and os.path.isfile(file):
        result = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if to_replace in line:
                    line = line.replace(to_replace, for_replace)
                    result.append(line)
                else:
                    result.append(line)
                    print('такова нема')
            f.close()
        with open(file, 'w') as f:
            f.writelines(result)
            f.close()
        return 'Complete'
    else:
        return 'Error'


print(replace_text('test.txt', 'чмо', 'я'))
