string = input()
stack = []
balanced = True

for symbol in string:
    if symbol in '({[':
        stack.append(symbol)
    else:
        if stack:
            last_symbol = stack.pop()
            combination = last_symbol + symbol

            if combination not in '(){}[]':
                balanced = False
                break
        else:
            balanced = False
            break

if balanced:
    print('YES')
else:
    print('NO')
