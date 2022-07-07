import bs4
import requests
from collections import Counter


def is_ascii(c):
    return ord('a') <= ord(c.lower()) <= ord('z')


def count_of_animal():
    page = requests.get('https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту')
    animal_list = []

    while True:
        soup = bs4.BeautifulSoup(page.text, 'html.parser')

        names = soup.find('div', class_='mw-category mw-category-columns').find_all('a')
        names = [name.text[0] for name in names]
        
        if is_ascii(names[-1]):
            first_ascii = next(
                (
                    i
                    for i, name in enumerate(names)
                    if is_ascii(name)
                ),
                None,
            )

            if first_ascii is not None:
                names = names[:first_ascii]
                animal_list.extend(names)
                break

        animal_list += names

        links = soup.find('div', id='mw-pages').find_all('a')
        for a in links:
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                page = requests.get(url)

    return sorted(Counter(animal_list).items())
        

def print_animals(animal_list):
    for letter, count in animal_list[1:]:
        print(f'{letter}: {count}')


print_animals(count_of_animal())
