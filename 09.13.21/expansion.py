def expansion(string: str):
    return string.split('.')[-1]


print(expansion('logpassfile.exe'))
print(expansion('logpassfile.py'))
print(expansion('logpassfile.html'))
