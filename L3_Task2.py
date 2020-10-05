def get_person(**kwargs):
    string_list = []
    for k,v in kwargs.items():
        string_list.append(f'{k}: {v}')
    string = ', '.join(string_list)
    print(string)

get_person(name="Артемий", surname="Гаврилов", year=1989, plaсe="Москва", email="123@mail.ru", phone="+71154444")