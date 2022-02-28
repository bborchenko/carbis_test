import api_requests

from db import queries


def main():
    quit_list = ['', 'q', 'quit', 'Q', 'c', 'close', 'exit']
    acceptable_languages = ('ru', 'en')
    api_key = input('Print your api key: ')
    if api_key in quit_list:
        quit()
    language = input('What language do you want to use (ru/en)? ')
    if language in quit_list:
        quit()

    while language not in acceptable_languages:
        language = input('Not supported language, please print ru or en: ')
        if language in quit_list:
            quit()

    db = queries.DB('./db/carbis_test.sqlite')
    db.get_connection()
    exists = db.check_if_exists()
    if not exists:
        db.create_table()

    db.insert_data(api_key, language)

    api = api_requests.APIRequests(api_key, language)
    while True:
        address = input('Print address that you want to find: ')
        if address in quit_list:
            break

        result = api.get_address(address)

        if result == 1:
            print("Can't find the address, please try again")
            continue

        value = input('What address do you want to know about? Please print the number: ')

        if value in quit_list:
            break

        api.get_coordinates(value)


if __name__ == '__main__':
    main()
