import re


def load_common_password():
    with open('10_million_password_list_top_10000.txt', 'r',
              encoding="utf-8") as password_words:
        black_list = password_words.read()
        return black_list


def password_text_to_dict(black_list):
    black_list_dict = re.findall(r'\w+', black_list)
    return black_list_dict


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
    return bool(re.search(r'[@#$]', password))


def check_password_in_black_list(password, password_dict):
    flag = 4
    for word in password_dict:
        if password == word:
            flag = 0
    return flag


def get_password_strength(password, min_length, max_length, password_dict):
    password_list = [check_min_password_length(password, min_length),
                     check_max_password_length(password, max_length),
                     check_digit_in_password(password),
                     check_lowercase_in_password(password),
                     check_uppercase_in_password(),
                     check_symbol_in_password(),
                     check_password_in_black_list(password, password_dict)]
    password_strength = sum(password_list)
    return password_strength


if __name__ == '__main__':
    min_length = 8
    max_length = 12
    password = input('Enter your password: ')
    load_password_file = load_common_password()
    password_dict = password_text_to_dict(load_password_file)
    print('Password strength score = {}'.format(get_password_strength(password,
                                                             min_length,
                                                             max_length,
                                                             password_dict)))
