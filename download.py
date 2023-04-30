import re
from urllib.parse import urljoin
from pathlib import Path

from bs4 import BeautifulSoup
import requests_cache


DOWNLOAD_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    # Загрузка веб-страницы с кешированием.
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOAD_URL)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, features='lxml')

    table_tag = soup.find('table', {'class': 'docutils'})
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    archive_url = urljoin(DOWNLOAD_URL, pdf_a4_tag['href'])
    filename = archive_url.split('/')[-1]

    # Добавьте константу, где будет храниться путь
    # до директории с текущим файлом.
    BASE_DIR = Path(__file__).parent
    # Здесь весь уже написанный код.
    # Сформируйте путь до директории downloads.
    downloads_dir = BASE_DIR / 'downloads'
    # Создайте директорию.
    downloads_dir.mkdir(exist_ok=True)
    # Получите путь до архива, объединив имя файла с директорией.
    archive_path = downloads_dir / filename

    response = session.get(archive_url)

    with open(archive_path, 'wb') as file:
        # Полученный ответ записывается в файл.
        file.write(response.content)

    print(archive_url)
