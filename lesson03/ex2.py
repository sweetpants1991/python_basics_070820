# case2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_func(user_first_name, user_last_name, user_yearofbirth, user_city, user_email, user_phone):
    print(user_first_name, user_last_name, user_yearofbirth, user_city, user_email, user_phone)


user_func(user_first_name="Artem", user_last_name="Pakentreyger", user_yearofbirth="1992",
          user_city="Saint-Petersburg", user_email="User's E-mail", user_phone="User's phone number")
