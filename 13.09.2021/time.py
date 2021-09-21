def time(num: int):
    days = num // (60 * 60 * 24)
    num %= 60 * 60 * 24
    hours = num // (60 * 60)
    num %= 60 * 60
    minutes = num // 60
    num %= 60
    seconds = num
    return f'{days}:{hours}:{minutes}:{seconds}'


print(time(86400))
