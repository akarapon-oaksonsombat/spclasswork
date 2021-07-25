def staircase(n):
    text = ''
    for i in range(0, n):
        text += staircase_row(n, i+1)
        if i < n-1:
            text += '\n'
    return text


def staircase_row(number, row):
    return f'{" " * (number-row)}' + f'{"#" * row}'
