import re
import getpass


def load_passwords_file():
    with open('10_million_password_list_top_10000.txt', 'r',
              encoding="utf-8") as file_with_passwords:
        passwords_from_file = file_with_passwords.read()
        return passwords_from_file


def check_min_password_length(password, min_length):
    return bool(min_length <= len(password))


def check_max_password_length(password, max_length):
    return bool(len(password) <= max_length)


def check_digit_in_password(password):
    return bool(re.search(r'\d', password))


def check_lowercase_in_password(password):
    return bool(re.search(r'[a-z]', password))


def check_uppercase_in_password(password):
    return bool(re.search(r'[A-Z]', password))


def check_symbol_in_password(password):
    return bool(re.search(r'[@#$%^&*!~";:?+-/|\=_]', password))


def check_password_in_black_list(password, password_file):
    return bool(password not in password_file)*4


def get_password_strength(password, min_length, max_length, password_file):
    checklist = [check_min_password_length(password, min_length),
                 check_max_password_length(password, max_length),
                 check_digit_in_password(password),
                 check_lowercase_in_password(password),
                 check_uppercase_in_password(password),
                 check_symbol_in_password(password),
                 check_password_in_black_list(password, password_file)]
    password_strength = sum(checklist)
    return password_strength


if __name__ == '__main__':
    min_length = 8
    max_length = 12
    password = getpass.getpass('Type your password: ')
    password_file = load_passwords_file()
    print('Password strength score = {}'.format(get_password_strength
                                                (password, min_length,
                                                 max_length, password_file)))
