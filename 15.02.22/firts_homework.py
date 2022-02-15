def alignment(list_of_items: list, pos: str, symbol_to_fill: str, count_of_symbols: int) -> str:
    """
    is a function to align items according to certain parameters
    :param list_of_items: is a list of items to be leveled
    :param pos: is a position to align
    :param symbol_to_fill: the symbol that will fill the empty space
    :param count_of_symbols: is a count symbols in string
    :return: aligned strings
    """
    result = ''
    if pos in ['center', 'right', 'left']:
        if pos == 'center':
            for item in list_of_items:
                result += '\n {0:{1}^{2}s}'.format(item, symbol_to_fill, count_of_symbols)
        elif pos == 'right':
            for item in list_of_items:
                result += '\n {0:{1}>{2}s}'.format(item, symbol_to_fill, count_of_symbols)
        elif pos == 'left':
            for item in list_of_items:
                result += '\n {0:{1}<{2}s}'.format(item, symbol_to_fill, count_of_symbols)
        return result
    else:
        return 'incorrect position to alignment'


print(alignment(['1233112', '124122', '1234'], 'center', '*', 20))
print(alignment.__doc__)
