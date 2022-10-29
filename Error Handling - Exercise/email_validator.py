import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()

    if command == 'End':
        break

    email = command
    name = re.findall(r'([A-Za-z]+)@', email)
    symbol = re.search(r"@", email)
    domain = re.findall(r'(\.\w+)', email)

    if not symbol:
        raise MustContainAtSymbolError('Email must contain @')
    elif len(name[0]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    elif domain[0] not in ['.com', '.net', '.org', '.bg']:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org')
    else:
        print('Email is valid')