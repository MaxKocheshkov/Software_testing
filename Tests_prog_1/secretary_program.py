import json
import os

directories, documents = {}, []


def update_date():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    f_directories = os.path.join(current_path, 'fixtures/directories.json')
    f_documents = os.path.join(current_path, 'fixtures/documents.json')
    with open(f_documents, 'r', encoding='utf8') as out_docs:
        documents = json.load(out_docs)
    with open(f_directories, 'r', encoding='utf8') as out_dirs:
        directories = json.load(out_dirs)
    return directories, documents


# поиск имени по номеру доумента (p)
def search_by_number(documents):
    event_doc = input('введите номер документа: ')
    for event in documents:
        if event_doc == event.get('number'):
            print(event['name'])
            return
        else:
            print('Документа по данному номеру не обнаружено')


# вывод всех документов (l)
def all_docs(documents):
    for dict_doc in documents:
        folk_attach = list(dict_doc.values())
        print(f'{folk_attach[0]} "{folk_attach[1]}" "{folk_attach[2]}"')


# поиск полки по номеру документа (s)
def act(directories):
    documents_shelf = 0
    user_ordinal = input('Введите номер документа: ')
    for shelf in directories:
        documents_shelf += 1
        if user_ordinal in directories.get(shelf):
            print('Документ на полке', shelf)
            return
        elif documents_shelf == len(directories):
            print('Документа по данному номеру не обнаружено')
            return


# Добавление нового документа в documents и directories (a)
def extension(documents, directories):
    user_type = input('введите тип документа: ')
    user_number = input('введите номер документа: ')
    user_name = input('введите имя владельца: ')
    user_shelf = input('На какой полке будет храниться? ')

    # добавление в список documents
    new_items = [('type', user_type), ('number', user_number), ('name', user_name)]
    user_dict = dict(new_items)
    j = len(documents)
    documents.insert(j, user_dict)
    print(documents)
    print('###')

    # добавление в directories
    if directories.get(user_shelf) != None:
        (directories.get(user_shelf)).append(user_number)
        print(f"Номер документа добавлен на полку {user_shelf}: ")
        print(directories)
    else:
        add_user_shelf = {user_shelf: []}
        directories.update(add_user_shelf)
        (directories.get(user_shelf)).append(user_number)
        print(f"Номер документа добавлен на новую полку {user_shelf}: ")
        print(directories)


# Task №2

# удаление документа из documents и directories (d)
def exterminate(documents, directories):
    user_delet = input('введите номер документа для удаления: ')

    # удаление из documents
    for delet_value in documents:
        if user_delet == delet_value["number"]:
            documents.remove(delet_value)
            print(f'Документ с номером {user_delet} удален из documents')
            print(documents)

    # удаление из directories
    for delet_ordinal in directories.values():
        for index_del in range(0, len(delet_ordinal)):
            if user_delet == delet_ordinal[index_del]:
                del delet_ordinal[index_del]
                print(f'Документ с номером {user_delet} удален из directories')
                print(directories)
                break


# Перемещение документа (m)
def transfer(directories):
    move_doc = input('Введите номер документа для перемещения: ')
    move_shelf = input('введите номер полки куда переместить: ')
    if move_shelf in directories.keys():
        for old_location, old_value in directories.items():
            for index_move in range(0, len(old_value)):
                if move_doc == old_value[index_move]:
                    (directories.get(move_shelf)).append(move_doc)
                    old_value.pop(index_move)
    print(f'документ перемещен на полку {move_shelf}')
    print(directories)


# создание новой полки (as)
def supplement(directories):
    new_user_shelf = input('введите номер полки для добавления: ')
    for add_shelf_key in directories.keys():
        if int(new_user_shelf) == int(add_shelf_key):
            print('Полка с таким номером уже существует')
            break
        else:
            directories.setdefault(new_user_shelf, [])
            print(directories)
            break


def main():
    """
       p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
       l – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
       s – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
       a – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
       имя владельца и номер полки, на котором он будет храниться.
       d – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
       m – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
       as – команда, которая спросит номер новой полки и добавит ее в перечень;
       q - команда, которая завершает выполнение программы
       """
    print(
        'Вас приветствует программа помошник!\n',
        '(Введите help, для просмотра списка поддерживаемых команд)\n'
    )
    global directories, documents
    directories, documents = update_date()
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            search_by_number(documents)
        elif user_input == 'l':
            all_docs(documents)
        elif user_input == 's':
            act(directories)
        elif user_input == 'a':
            extension(documents, directories)
        elif user_input == 'd':
            exterminate(documents, directories)
        elif user_input == 'm':
            transfer(directories)
        elif user_input == 'as':
            supplement(directories)
        elif user_input == 'help':
            print(main.__doc__)
        elif user_input == 'q':
            print('До свидания!')
            break


if __name__ == '__main__':
    main()
