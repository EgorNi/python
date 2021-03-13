def user_info(name, surname, year_of_birth, city_of_residence, email, phone):
    print(name, surname, year_of_birth, city_of_residence, email, phone)


user_name = input('enter name: ')
user_surname = input('enter surname: ')
user_year_of_birth = input('enter year_of_birth: ')
user_city_of_residence = input('enter city_of_residence: ')
user_email = input('enter email: ')
user_phone = input('enter phone: ')
user_info(
    name=user_name,
    surname=user_surname, 
    year_of_birth=user_year_of_birth,
    city_of_residence=user_city_of_residence,
    email=user_email,
    phone=user_phone
)
