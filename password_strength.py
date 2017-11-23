import re
import getpass


def load_passwords_file():
    with open('10_million_password_list_top_10000.txt', 'r',
              encoding="utf-8") as password_words:
        black_list = password_words.read()
        return black_list


def check_min_password_length(password, min_length):
    return bool(min_length <= len(password))


def check_max_password_length(password, max_length):
    return bool(len(password) <= max_length)


def check_digit_in_password(password):
    return bool(re.search(r'\d', password))


def check_lowercase_in_password(password):
    return bool(re.search(r'[a-z]', password))


def check_uppercase_in_password():
    return bool(re.search(r'[A-Z]', password))


def check_symbol_in_password():
    return bool(re.search(r'[@#$%^&*!~";:?+-/|\=_]', password))


def check_password_in_black_list(password, password_file):
    flag = 4
    if password in password_file:
        flag = 0
    return flag


def get_password_strength(password, min_length, max_length, password_file):
    password_list = [check_min_password_length(password, min_length),
                     check_max_password_length(password, max_length),
                     check_digit_in_password(password),
                     check_lowercase_in_password(password),
                     check_uppercase_in_password(),
                     check_symbol_in_password(),
                     check_password_in_black_list(password, password_file)]
    password_strength = sum(password_list)
    return password_strength


if __name__ == '__main__':
    min_length = 8
    max_length = 12
    password = getpass.getpass('Type your password: ')
    password_file = load_passwords_file()
    print('Password strength score = {}'.format(get_password_strength
                                                (password, min_length,
                                                 max_length, password_file)))
