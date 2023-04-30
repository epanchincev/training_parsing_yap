import re

from bs4 import BeautifulSoup
import requests_cache

MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':
    # Загрузка веб-страницы с кешированием.
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, features='lxml')

    sidebar = soup.find('div', class_='sphinxsidebarwrapper')
    ul_tags = sidebar.find_all('ul')
    results = []
    regex_pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'

    for ul in ul_tags:

        if 'All versions' in ul.text:
            # Если текст найден, ищутся все теги <a> в этом списке.
            a_tags = ul.find_all('a')
            for a_tag in a_tags:
                text_match = re.search(regex_pattern, a_tag.text)
                if text_match is not None:
                    results.append((a_tag['href'], *text_match.groups()))
            # Остановка перебора списков.
            break
        # Если нужный список не нашёлся,
        # вызывается исключение и выполнение программы прерывается.
        else:
            raise Exception('Ничего не нашлось')

    for row in results:
        print(*row)
