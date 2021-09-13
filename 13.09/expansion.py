def expansion(string: str):
    return string.split('.')[-1]


print(expansion('file.exe'))
print(expansion('file.py'))
print(expansion('file.html'))
